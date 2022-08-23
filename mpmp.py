import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_login import (
    login_required,
    current_user,
    LoginManager,
    login_user,
    UserMixin,
)
import datetime
from nanoid import generate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlite.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "secret-key-goes-here"
app.config["UPLOAD_FOLDER"] = "./static"
ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif"}
login_manager = LoginManager(app)
db = SQLAlchemy(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


tags = db.Table(
    "postcategories",
    db.Column("post_id", db.Integer, db.ForeignKey("post.id"), primary_key=True),
    db.Column(
        "category_id", db.Integer, db.ForeignKey("category.id"), primary_key=True
    ),
)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(80), nullable=False)
    rating = db.Column(db.Integer(), nullable=False)
    image = db.Column(db.String(120), nullable=False)
    slug = db.Column(db.String(120), unique=True, nullable=False)
    categories = db.relationship("Category", backref="post", lazy=True)
    author = db.relationship("User", backref="post", lazy=True, uselist=False)

    def __repr__(self):
        return "<Post %r>" % self.text


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120))
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))

    def __repr__(self):
        return "<User %r>" % self.username

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(64), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))

    def __repr__(self):
        return "<Category %r>" % self.text


@app.get("/")
def index():
    posts = Post.query.all()
    return render_template("index.html", posts=posts)


@app.get("/p/<path:path>")
def p(path):
    posts = Post.query.filter_by(slug=path)
    return render_template("index.html", posts=posts, name=current_user)


@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        slug = generate(size=6)
        categories = request.form.get("categories")
        rating = request.form.get("rating")
        text = request.form.get("text")

        post = Post(
            text=text,
            date=datetime.datetime.today().strftime("%d/%m/%Y"),
            slug=slug,
            image=f"/static/{slug}.png",
            rating=rating
        )
        db.session.add(post)
        db.session.commit()
        for text in categories.split(" "):
            category = Category(text=text)
            post.categories.append(category)
            post.author = current_user
            db.session.commit()

        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = slug + ".png"
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        return render_template("add.html")


@app.get("/login")
def login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_post():

    username = request.form.get("username")
    password = request.form.get("password")

    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        flash("Please check your login details and try again.")
        return redirect(url_for("login"))
    login_user(user, remember=True)
    return redirect(url_for("index"))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(401)
def page_not_found(e):
    return render_template("401.html"), 401


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

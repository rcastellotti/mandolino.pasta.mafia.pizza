from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
import json

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlite.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

tags = db.Table(
    "postcategories",
    db.Column("post_id", db.Integer, db.ForeignKey("post.id"), primary_key=True),
    db.Column(
        "category_id", db.Integer, db.ForeignKey("category.id"), primary_key=True
    ),
)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(80),nullable=False)
    date = db.Column(db.String(80), nullable=False)
    image = db.Column(db.String(120), unique=True, nullable=False)
    slug = db.Column(db.String(120), unique=True, nullable=False)
    categories = db.relationship("Category", backref="post", lazy=True)
    author = db.relationship("User", backref="post", lazy=True, uselist=False)

    def __repr__(self):
        return "<Post %r>" % self.text


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))

    def __repr__(self):
        return "<User %r>" % self.username


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(512), unique=True, nullable=False)
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
    return render_template("index.html", posts=posts)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


DATABASE = "sqlite.db"


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = dict_factory
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


@app.get("/")
def index():

    cur = get_db().cursor()
    res = cur.execute("SELECT * FROM products")
    products = res.fetchall()
    return render_template("index.html", products=products)


@app.get("/p/<path:path>")
def p(path):
    cur = get_db().cursor()

    res = cur.execute(
        """SELECT * FROM products JOIN productOptions ON productId = products.id WHERE  slug = ? """,
        [path],
    )
    post = res.fetchall()
    return render_template("product.html", post=post)



@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

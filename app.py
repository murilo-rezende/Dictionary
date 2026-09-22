import os
import re

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

# Configure application
app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///dictionary.db")

app.secret_key = "secret"

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

categories = [
    "noun", "verb", "adjective", "adverb",
    "pronoun", "preposition", "conjunction", "interjection",
    "determiner"
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["GET", "POST"])
def add():

    if "user_id" not in session:
        return redirect("/login")

    if request.method == "GET":

        return render_template("add.html", categories=categories)

    elif request.method == "POST":

        word = request.form.get("word")
        meaning = request.form.get("meaning")
        lexical_category = request.form.get("lexical_category")

        if not word:
            flash("Must provide a word", "error")
            return redirect("/add")

        if not meaning:
            flash("Must provide a meaning", "error")
            return redirect("/add")

        if not word.isalpha() :
            flash("Your word should only contain letters")
            return redirect("/add")

        if not re.fullmatch(r"[A-Za-z\s.,!?;:'\"()-]+", meaning):
            flash("Meaning contains invalid characters", "error")
            return redirect("/add")

        if not lexical_category:
            flash("Must select a lexical category", "error")
            return redirect("/add")

        exists = db.execute("SELECT * FROM words WHERE word = ?", word)

        if exists:
            flash("Word is already on the dictionary", "error")
            return redirect("/add")

        db.execute(
            "INSERT INTO words (user_id, word, meaning, lexical_category) VALUES (?, ?, ?, ?)",
            session["user_id"], word, meaning, lexical_category
        )

        flash("Word added successfully!", "success")

        return redirect("/add")

@app.route("/remove", methods=["GET", "POST"])
def remove():

    if "user_id" not in session:
        return redirect("/login")

    if request.method == "GET":

        words = db.execute(
            "SELECT id, word FROM words WHERE user_id = ? ORDER BY word",
            session["user_id"]
        )

        return render_template("remove.html", words=words)

    if request.method == "POST":

        word_id = request.form.get("word_id")

        if not word_id:
            flash("Must select a word", "error")
            return redirect("/remove")

        db.execute(
            "DELETE FROM words WHERE id = ? AND user_id = ?",
            word_id, session["user_id"]
        )

        flash("Word removed successfully!", "success")
        return redirect("/remove")

@app.route("/words")
def words():

    if "user_id" not in session:
        return redirect("/login")

    search = request.args.get("q")

    if search:
        words = db.execute(
            "SELECT * FROM words WHERE user_id = ? AND word LIKE ? ORDER BY word",
            session["user_id"], f"%{search}%"
        )
    else:
        words = db.execute(
            "SELECT * FROM words WHERE user_id = ? ORDER BY word",
            session["user_id"]
        )

    return render_template("words.html", words=words)

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "GET":
        return render_template("register.html")

    username = request.form.get("username")
    password = request.form.get("password")
    confirmation = request.form.get("confirmation")

    if not username:
        flash("Must provide username", "error")
        return redirect("/register")

    if not password or not confirmation:
        flash("Must provide password", "error")
        return redirect("/register")

    if password != confirmation:
        flash("Passwords must match", "error")
        return redirect("/register")

    hash = generate_password_hash(password)

    try:
        user_id = db.execute(
            "INSERT INTO users (username, hash) VALUES (?, ?)",
            username, hash
        )
    except:
        flash("Username already exists", "error")
        return redirect("/register")

    session["user_id"] = user_id

    flash("Registered successfully!", "success")
    return redirect("/")

@app.route("/login", methods=["GET", "POST"])
def login():

    session.clear()

    if request.method == "GET":
        return render_template("login.html")

    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        flash("Must provide username and password", "error")
        return redirect("/login")

    rows = db.execute(
        "SELECT * FROM users WHERE username = ?",
        username
    )

    if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
        flash("Invalid username or password", "error")
        return redirect("/login")

    session["user_id"] = rows[0]["id"]

    flash("Logged in!", "success")
    return redirect("/")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

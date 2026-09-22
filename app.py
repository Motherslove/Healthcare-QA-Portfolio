from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

DATABASE = "healthcare.db"


def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    connection = get_db_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            date_of_birth TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


@app.route("/")
def home():
    search = request.args.get("search", "").strip()

    connection = get_db_connection()

    if search:
        patients = connection.execute("""
            SELECT *
            FROM patients
            WHERE id = ?
               OR LOWER(first_name) LIKE LOWER(?)
               OR LOWER(last_name) LIKE LOWER(?)
               OR LOWER(first_name || ' ' || last_name) LIKE LOWER(?)
            ORDER BY id DESC
        """, (
            search if search.isdigit() else -1,
            f"%{search}%",
            f"%{search}%",
            f"%{search}%"
        )).fetchall()
    else:
        patients = connection.execute("""
            SELECT *
            FROM patients
            ORDER BY id DESC
        """).fetchall()

    connection.close()

    return render_template(
        "index.html",
        patients=patients,
        search=search
    )


@app.route("/register", methods=["POST"])
def register_patient():
    first_name = request.form["first_name"].strip()
    last_name = request.form["last_name"].strip()
    date_of_birth = request.form["date_of_birth"]
    phone = request.form["phone"].strip()
    email = request.form["email"].strip()

    connection = get_db_connection()

    connection.execute("""
        INSERT INTO patients
        (first_name, last_name, date_of_birth, phone, email)
        VALUES (?, ?, ?, ?, ?)
    """, (
        first_name,
        last_name,
        date_of_birth,
        phone,
        email
    ))

    connection.commit()
    connection.close()

    return redirect("/")


if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)
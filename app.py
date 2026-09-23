from flask import Flask, render_template, request, redirect, jsonify
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

@app.route("/api/patients", methods=["GET"])
def get_patients():
    connection = get_db_connection()

    patients = connection.execute("""
        SELECT *
        FROM patients
        ORDER BY id ASC
    """).fetchall()

    connection.close()

    patient_list = []

    for patient in patients:
        patient_list.append({
            "id": patient["id"],
            "first_name": patient["first_name"],
            "last_name": patient["last_name"],
            "date_of_birth": patient["date_of_birth"],
            "phone": patient["phone"],
            "email": patient["email"]
        })

    return jsonify(patient_list)
@app.route("/api/patients/<int:patient_id>", methods=["GET"])
def get_patient(patient_id):
    connection = get_db_connection()

    patient = connection.execute("""
        SELECT *
        FROM patients
        WHERE id = ?
    """, (patient_id,)).fetchone()

    connection.close()

    if patient is None:
        return jsonify({"error": "Patient not found"}), 404

    return jsonify({
        "id": patient["id"],
        "first_name": patient["first_name"],
        "last_name": patient["last_name"],
        "date_of_birth": patient["date_of_birth"],
        "phone": patient["phone"],
        "email": patient["email"]
    })
@app.route("/api/patients", methods=["POST"])
def create_patient():
    data = request.get_json()

    first_name = data.get("first_name")
    last_name = data.get("last_name")
    date_of_birth = data.get("date_of_birth")
    phone = data.get("phone")
    email = data.get("email")

    if not all([first_name, last_name, date_of_birth, phone, email]):
        return jsonify({
            "error": "All patient fields are required"
        }), 400

    connection = get_db_connection()

    cursor = connection.execute("""
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

    patient_id = cursor.lastrowid

    connection.close()

    return jsonify({
        "id": patient_id,
        "first_name": first_name,
        "last_name": last_name,
        "date_of_birth": date_of_birth,
        "phone": phone,
        "email": email
    }), 201
if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)
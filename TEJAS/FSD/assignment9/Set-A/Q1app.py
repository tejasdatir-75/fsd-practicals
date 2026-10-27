
from flask import Flask, request, render_template, redirect
import psycopg2

app = Flask(__name__)

def db_connect():
    return psycopg2.connect(
        dbname="studentdb",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )

def create_table():
    con = db_connect()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS student_records (
            student_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            course VARCHAR(100) NOT NULL
        )
    """)

    con.commit()
    cur.close()
    con.close()

@app.route("/", methods=["GET", "POST"])
def student():
    con = db_connect()
    cur = con.cursor()

    if request.method == "POST":
        name = request.form["name"]
        course = request.form["course"]

        cur.execute(
            "INSERT INTO student_records (name, course) VALUES (%s, %s)",
            (name, course)
        )
        con.commit()

        cur.close()
        con.close()
        return redirect("/")

    cur.execute(
        "SELECT student_id, name, course FROM student_records ORDER BY student_id"
    )
    students = cur.fetchall()

    cur.close()
    con.close()

    return render_template("index.html", students=students)

if __name__ == "__main__":
    create_table()
    app.run(debug=True)

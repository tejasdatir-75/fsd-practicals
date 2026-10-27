
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
        CREATE TABLE IF NOT EXISTS employee (
            emp_id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            department VARCHAR(100)
        )
    """)

    con.commit()
    cur.close()
    con.close()

@app.route("/", methods=["GET", "POST"])
def employee():
    con = db_connect()
    cur = con.cursor()

    if request.method == "POST":
        name = request.form["name"]
        department = request.form["department"]

        cur.execute(
            "INSERT INTO employee (name, department) VALUES (%s, %s)",
            (name, department)
        )

        con.commit()
        cur.close()
        con.close()

        return redirect("/")

    cur.execute("SELECT emp_id, name, department FROM employee ORDER BY emp_id")
    employees = cur.fetchall()

    cur.close()
    con.close()

    return render_template("employee.html", employees=employees)

if __name__ == "__main__":
    create_table()
    app.run(debug=True)

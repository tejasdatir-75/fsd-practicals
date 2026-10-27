from flask import Flask, request, render_template, redirect
import psycopg2

app = Flask(__name__)

# Database Connection
def db_connect():
    return psycopg2.connect(
        dbname="studentdb",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )

# Create Table
def create_table():
    con = db_connect()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS student_update (
            student_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            course VARCHAR(100) NOT NULL
        )
    """)

    con.commit()
    cur.close()
    con.close()

# Display and Add Student
@app.route("/", methods=["GET", "POST"])
def student():
    msg = ""

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        course = request.form.get("course", "").strip()

        if not name or not course:
            msg = "Please fill in all fields!"

        else:
            con = None

            try:
                con = db_connect()
                cur = con.cursor()

                cur.execute("""
                    INSERT INTO student_update (name, course)
                    VALUES (%s, %s)
                """, (name, course))

                con.commit()
                cur.close()

                msg = "Student Added Successfully!"

            except Exception as e:
                if con:
                    con.rollback()

                print("INSERT ERROR:", e)
                msg = "Error saving student. Check VS Code Terminal."

            finally:
                if con:
                    con.close()

    con = db_connect()
    cur = con.cursor()

    cur.execute("""
        SELECT student_id, name, course
        FROM student_update
        ORDER BY student_id
    """)

    students = cur.fetchall()

    cur.close()
    con.close()

    return render_template(
        "student.html",
        students=students,
        msg=msg
    )

# Update Student Course
@app.route("/update", methods=["POST"])
def update_course():
    student_id = request.form.get("student_id", "").strip()
    new_course = request.form.get("new_course", "").strip()

    if not student_id or not student_id.isdigit() or not new_course:
        return "Please enter a valid Student ID and Course!"

    con = db_connect()
    cur = con.cursor()

    cur.execute("""
        UPDATE student_update
        SET course = %s
        WHERE student_id = %s
    """, (new_course, int(student_id)))

    updated = cur.rowcount

    con.commit()
    cur.close()
    con.close()

    if updated == 0:
        return "Student ID not found!"

    return redirect("/")

if __name__ == "__main__":
    create_table()
    app.run(debug=True)
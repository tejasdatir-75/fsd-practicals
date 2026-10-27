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


# Create Student Table
def create_table():
    con = db_connect()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS student (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INTEGER NOT NULL,
            course VARCHAR(50) NOT NULL
        )
    """)

    con.commit()
    cur.close()
    con.close()


# Insert and Display Students
@app.route("/", methods=["GET", "POST"])
def index():
    msg = ""

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        age = request.form.get("age", "").strip()
        course = request.form.get("course", "").strip()

        con = None

        try:
            if not name or not age or not course:
                msg = "Please fill all fields!"
            else:
                age = int(age)

                if age <= 0:
                    msg = "Age must be greater than zero!"
                else:
                    con = db_connect()
                    cur = con.cursor()

                    cur.execute("""
                        INSERT INTO student (name, age, course)
                        VALUES (%s, %s, %s)
                    """, (name, age, course))

                    con.commit()
                    cur.close()

                    msg = "Student added successfully!"

        except ValueError:
            msg = "Please enter a valid age!"

        except psycopg2.Error as e:
            if con:
                con.rollback()

            print("Database Error:", e)
            msg = "Database error! Check Terminal."

        finally:
            if con:
                con.close()

    con = db_connect()
    cur = con.cursor()

    cur.execute("""
        SELECT id, name, age, course
        FROM student
        ORDER BY id
    """)

    students = cur.fetchall()

    cur.close()
    con.close()

    return render_template(
        "Q1.html",
        students=students,
        msg=msg
    )


# Update Student
@app.route("/update", methods=["POST"])
def update():
    student_id = request.form.get("student_id", "").strip()
    name = request.form.get("name", "").strip()
    age = request.form.get("age", "").strip()
    course = request.form.get("course", "").strip()

    if not student_id.isdigit() or not name or not age or not course:
        return "Please enter all valid details!"

    con = None

    try:
        age = int(age)

        if age <= 0:
            return "Age must be greater than zero!"

        con = db_connect()
        cur = con.cursor()

        cur.execute("""
            UPDATE student
            SET name = %s,
                age = %s,
                course = %s
            WHERE id = %s
        """, (name, age, course, int(student_id)))

        updated = cur.rowcount

        con.commit()
        cur.close()

        if updated == 0:
            return "Student ID not found!"

        return redirect("/")

    except ValueError:
        return "Please enter a valid age!"

    except psycopg2.Error as e:
        if con:
            con.rollback()

        print("Database Error:", e)
        return "Database error! Check Terminal."

    finally:
        if con:
            con.close()


# Delete Student
@app.route("/delete", methods=["POST"])
def delete():
    student_id = request.form.get("student_id", "").strip()

    if not student_id.isdigit():
        return "Please enter a valid Student ID!"

    con = None

    try:
        con = db_connect()
        cur = con.cursor()

        cur.execute("""
            DELETE FROM student
            WHERE id = %s
        """, (int(student_id),))

        deleted = cur.rowcount

        con.commit()
        cur.close()

        if deleted == 0:
            return "Student ID not found!"

        return redirect("/")

    except psycopg2.Error as e:
        if con:
            con.rollback()

        print("Database Error:", e)
        return "Database error! Check Terminal."

    finally:
        if con:
            con.close()


# Run Application
if __name__ == "__main__":
    create_table()
    app.run(debug=True)
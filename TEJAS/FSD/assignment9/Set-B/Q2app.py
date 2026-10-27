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
        CREATE TABLE IF NOT EXISTS Book (
            Book_ID SERIAL PRIMARY KEY,
            Book_Name VARCHAR(100) NOT NULL,
            Author VARCHAR(100) NOT NULL,
            Price NUMERIC(10,2) NOT NULL
        )
    """)

    con.commit()
    cur.close()
    con.close()


@app.route("/", methods=["GET", "POST"])
def books():
    msg = ""

    if request.method == "POST":
        book_name = request.form.get("book_name", "").strip()
        author = request.form.get("author", "").strip()
        price = request.form.get("price", "").strip()

        if not book_name or not author or not price:
            msg = "Please fill all fields!"

        else:
            con = None

            try:
                price = float(price)

                if price < 0:
                    msg = "Price cannot be negative!"
                else:
                    con = db_connect()
                    cur = con.cursor()

                    cur.execute("""
                        INSERT INTO Book (Book_Name, Author, Price)
                        VALUES (%s, %s, %s)
                    """, (book_name, author, price))

                    con.commit()
                    cur.close()

                    msg = "Book Added Successfully!"

            except ValueError:
                msg = "Enter a valid price!"

            except psycopg2.Error as e:
                if con:
                    con.rollback()

                print("Database Error:", e)
                msg = "Error saving book! Check Terminal."

            finally:
                if con:
                    con.close()

    con = db_connect()
    cur = con.cursor()

    cur.execute("""
        SELECT Book_ID, Book_Name, Author, Price
        FROM Book
        ORDER BY Book_ID
    """)

    book_list = cur.fetchall()

    cur.close()
    con.close()

    return render_template(
        "Q2.html",
        books=book_list,
        msg=msg
    )


@app.route("/update", methods=["POST"])
def update_book():
    book_id = request.form.get("book_id", "").strip()
    book_name = request.form.get("book_name", "").strip()
    author = request.form.get("author", "").strip()
    price = request.form.get("price", "").strip()

    if not book_id.isdigit() or not book_name or not author or not price:
        return "Please enter all valid details!"

    con = None

    try:
        price = float(price)

        if price < 0:
            return "Price cannot be negative!"

        con = db_connect()
        cur = con.cursor()

        cur.execute("""
            UPDATE Book
            SET Book_Name = %s,
                Author = %s,
                Price = %s
            WHERE Book_ID = %s
        """, (book_name, author, price, int(book_id)))

        updated = cur.rowcount

        con.commit()
        cur.close()

        if updated == 0:
            return "Book ID not found!"

        return redirect("/")

    except ValueError:
        return "Enter a valid price!"

    except psycopg2.Error as e:
        if con:
            con.rollback()

        print("Database Error:", e)
        return "Database error! Check Terminal."

    finally:
        if con:
            con.close()


if __name__ == "__main__":
    create_table()
    app.run(debug=True)
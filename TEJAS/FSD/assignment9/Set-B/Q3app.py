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
        CREATE TABLE IF NOT EXISTS Product (
            Product_ID SERIAL PRIMARY KEY,
            Product_Name VARCHAR(100) NOT NULL,
            Price NUMERIC(10,2) NOT NULL,
            Quantity INTEGER NOT NULL
        )
    """)

    con.commit()
    cur.close()
    con.close()


@app.route("/", methods=["GET", "POST"])
def products():
    msg = ""

    if request.method == "POST":
        name = request.form.get("product_name", "").strip()
        price = request.form.get("price", "").strip()
        quantity = request.form.get("quantity", "").strip()

        con = None

        try:
            if not name or not price or not quantity:
                msg = "Please fill all fields!"
            else:
                price = float(price)
                quantity = int(quantity)

                if price < 0 or quantity < 0:
                    msg = "Price and quantity cannot be negative!"
                else:
                    con = db_connect()
                    cur = con.cursor()

                    cur.execute("""
                        INSERT INTO Product (Product_Name, Price, Quantity)
                        VALUES (%s, %s, %s)
                    """, (name, price, quantity))

                    con.commit()
                    cur.close()

                    msg = "Product added successfully!"

        except ValueError:
            msg = "Enter a valid price and quantity!"

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
        SELECT Product_ID, Product_Name, Price, Quantity
        FROM Product
        ORDER BY Product_ID
    """)

    product_list = cur.fetchall()

    cur.close()
    con.close()

    return render_template(
        "Q3.html",
        products=product_list,
        msg=msg
    )


@app.route("/update", methods=["POST"])
def update_product():
    product_id = request.form.get("product_id", "").strip()
    quantity = request.form.get("quantity", "").strip()

    if not product_id.isdigit() or not quantity.isdigit():
        return "Please enter a valid Product ID and Quantity!"

    con = None

    try:
        con = db_connect()
        cur = con.cursor()

        cur.execute("""
            UPDATE Product
            SET Quantity = %s
            WHERE Product_ID = %s
        """, (int(quantity), int(product_id)))

        updated = cur.rowcount

        con.commit()
        cur.close()

        if updated == 0:
            return "Product ID not found!"

        return redirect("/")

    except psycopg2.Error as e:
        if con:
            con.rollback()

        print("Database Error:", e)
        return "Database error! Check Terminal."

    finally:
        if con:
            con.close()


@app.route("/delete", methods=["POST"])
def delete_product():
    product_id = request.form.get("product_id", "").strip()

    if not product_id.isdigit():
        return "Please enter a valid Product ID!"

    con = None

    try:
        con = db_connect()
        cur = con.cursor()

        cur.execute("""
            DELETE FROM Product
            WHERE Product_ID = %s
        """, (int(product_id),))

        deleted = cur.rowcount

        con.commit()
        cur.close()

        if deleted == 0:
            return "Product ID not found!"

        return redirect("/")

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
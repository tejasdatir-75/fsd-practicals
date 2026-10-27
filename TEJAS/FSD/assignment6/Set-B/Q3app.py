from flask import Flask, render_template

app = Flask(__name__)

products = [
    ["Pen", 10],
    ["Book", 100],
    ["Bag", 800],
    ["Laptop", 50000],
    ["Mouse", 500]
]

@app.route('/')
def expensive():
    costly = max(products, key=lambda p: p[1])

    return render_template('Q3.html', costly=costly)

if __name__ == '__main__':
    app.run(debug=True)
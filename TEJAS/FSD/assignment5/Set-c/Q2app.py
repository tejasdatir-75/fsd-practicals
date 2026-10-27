
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        name = request.form['name']
        quantity = int(request.form['quantity'])
        price = float(request.form['price'])

        return render_template(
            'Q2.html',
            name=name,
            quantity=quantity,
            price=price,
            total=quantity * price,
            submitted=True
        )

    return render_template('Q2.html', submitted=False)

if __name__ == '__main__':
    app.run(debug=True)

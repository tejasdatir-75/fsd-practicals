from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/add', methods=['GET', 'POST'])
def add():
    result = ""
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = num1 + num2

    return render_template('Q2.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
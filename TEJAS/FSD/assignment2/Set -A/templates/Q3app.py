from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def multiply():

    a = ""
    b = ""
    result = ""

    if request.method == 'POST':
        a = request.form['a']
        b = request.form['b']
        result = int(a) * int(b)

    return render_template('index.html', result=result, a=a, b=b)

app.run(debug=True)
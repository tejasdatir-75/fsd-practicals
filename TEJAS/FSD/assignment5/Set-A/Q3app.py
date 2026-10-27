from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def area():
    result = ""
    if request.method == 'POST':
        length = float(request.form['length'])
        breadth = float(request.form['breadth'])
        result = length * breadth

    return render_template('Q3.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
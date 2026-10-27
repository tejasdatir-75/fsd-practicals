from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def search():
    result = ""

    if request.method == 'POST':
        name = request.form['name']
        result = "Student Name: " + name

    return render_template('Q2.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
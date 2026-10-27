from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def employee():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        salary = request.form['salary']

        return f"Name: {name}<br>Age: {age}<br>Salary: {salary}"

    return render_template('Q1.html')

if __name__ == '__main__':
    app.run(debug=True)
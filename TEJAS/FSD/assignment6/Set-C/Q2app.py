from flask import Flask, render_template

app = Flask(__name__)

students = [
    ["Tejas Datir", 86],
    ["Sahil Andhale", 55],
    ["Amit Bhosle", 35],
    ["Tanmay Dhome", 85],
    ["Pramod Gholap", 70]
]

@app.route('/')
def display():
    return render_template('Q2.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
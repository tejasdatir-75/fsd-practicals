from flask import Flask, render_template

app = Flask(__name__)

employees = [
    ["Sahil Andhale", 101, "HR"],
    ["Tejas Datir", 102, "IT"],
    ["Amit Bhosle", 103, "Sales"],
    ["Tanmay Dhome", 104, "Finance"],
    ["Pramod Gholap", 105, "Marketing"]
]

@app.route('/')
def display():
    return render_template('Q2.html', employees=employees)

if __name__ == '__main__':
    app.run(debug=True)
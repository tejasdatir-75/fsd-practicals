from flask import Flask, render_template

app = Flask(__name__)

employees = [
    ["Sahil Andhale", 10000, "HR"],
    ["Tejas Datir", 200000, "IT"],
    ["Amit Bhosle", 130000, "Sales"],
    ["Tanmay Dhome", 104000, "Finance"],
    ["Pramod Gholap", 140000, "Marketing"]
]

@app.route('/')
def display():
    return render_template('Q1.html', employees=employees)

if __name__ == '__main__':
    app.run(debug=True)
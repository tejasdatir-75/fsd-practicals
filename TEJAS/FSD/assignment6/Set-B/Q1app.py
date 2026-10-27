from flask import Flask, render_template

app = Flask(__name__)

student = {
    "name": "Tejas Datir",
    "roll_no": 22,
    "course": "Bsc(It)",
    "marks": 80
}

@app.route('/')
def display():
    return render_template('Q1.html', student=student)

if __name__ == '__main__':
    app.run(debug=True)
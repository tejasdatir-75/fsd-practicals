from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def student():
    name = "Teja Datir"
    marks = [80, 75, 85, 60, 90]

    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    return render_template(
        'Q3.html',
        name=name,
        marks=marks,
        total=total,
        average=average,
        highest=highest,
        lowest=lowest
    )

if __name__ == '__main__':
    app.run(debug=True)
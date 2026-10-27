from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def student():
    if request.method == 'POST':
        name = request.form.get('name', '')
        return "Student Name: " + name

    return render_template('Q2.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/student', methods=['GET', 'POST'])
def student():
    if request.method == 'POST':
        name = request.form['name']
        return "Student Name: " + name

    return render_template('Q1.html')

if __name__ == '__main__':
    app.run(debug=True)
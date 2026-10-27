from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        marks = int(request.form['marks'])

        if marks >= 35:
            return "Pass"
        else:
            return "Fail"

    return render_template('Q4.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def salary():
    total = ""
    if request.method == 'POST':
        basic = float(request.form['basic'])
        allowance = 2000
        total = basic + allowance

    return render_template('Q3.html', total=total)

if __name__ == '__main__':
    app.run(debug=True)
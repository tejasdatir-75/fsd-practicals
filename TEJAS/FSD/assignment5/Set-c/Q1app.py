from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ""

    if request.method == 'POST':
        username = request.form['username']

        if username == "Tejas":
            message = "Valid Username"
        else:
            message = "Invalid Username"

    return render_template('Q1.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
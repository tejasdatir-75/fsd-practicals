from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return "Login Successful"

    return render_template('Q1.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask

app = Flask(__name__)

@app.route('/employee/<name>')
def employee(name):
    return "Welcome " + name + " Welcome to our company."

if __name__ == '__main__':
    app.run(debug=True)
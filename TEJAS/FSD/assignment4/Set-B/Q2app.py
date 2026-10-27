from flask import Flask

app = Flask(__name__)

@app.route('/square/<int:num>')
def square(num):
    return "Square: " + str(num * num)

if __name__ == '__main__':
    app.run(debug=True)
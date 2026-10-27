from flask import Flask

app = Flask(__name__)

@app.route('/course/<name>')
def course(name):
    return "Course Name: " + name + "<br>Course Information: This course provides knowledge and skills."

if __name__ == '__main__':
    app.run(debug=True)
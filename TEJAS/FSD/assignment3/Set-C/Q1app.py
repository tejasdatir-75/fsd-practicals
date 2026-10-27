from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Computer Science Department<br>Our department provides quality education in programming, web development, and computer technology."

if __name__ == '__main__':
    app.run(debug=True)
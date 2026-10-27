from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "Name: Tejas Datir <br> Roll No:22"

app.run(debug=True)
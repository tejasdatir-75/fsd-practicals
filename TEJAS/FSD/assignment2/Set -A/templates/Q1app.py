from flask import Flask

app = Flask(__name__)

@app.route('/student')
def student():
    return "GET request received successfully"

app.run(debug=True)
from flask import Flask
from datetime import date

app = Flask(__name__)

@app.route('/')
def home():
    today = date.today()
    return f"Happy Birthday <br>Current Date: {today}"

if __name__ == '__main__':
    app.run(debug=True)
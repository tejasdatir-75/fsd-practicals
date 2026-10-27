from flask import Flask
from datetime import datetime

app=Flask(__name__)

@app.route('/')
def home():
    return "Current Date and Time:"+ str(datetime.now())

app.run(debug=True)
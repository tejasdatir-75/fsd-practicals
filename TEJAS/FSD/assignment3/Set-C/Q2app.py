from flask import Flask
import platform

app = Flask(__name__)

@app.route('/')
def system_info():
    return "System Information: <br>"\
    "Operating System: " + platform.system() + "<br>"\
    "Machine : " + platform.machine() + "<br>"\
    "Processor : " + platform.processor()

app.run(debug=True)
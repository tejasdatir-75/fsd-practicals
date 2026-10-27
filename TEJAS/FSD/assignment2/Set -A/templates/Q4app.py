from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def feedback():

    if request.method == 'POST':
        name = request.form['name']
        feedback = request.form['feedback']
        return "Thank you " + name + " for your feedback!"

    return render_template('Q4.html')

app.run(debug=True)
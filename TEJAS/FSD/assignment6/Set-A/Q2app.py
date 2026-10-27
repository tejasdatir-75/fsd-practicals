from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def students():
    names = ["Sahil", "Tejas", "Amit", "Tanmay", "Pramod"]
    return render_template('Q2.html', names=names)

if __name__ == '__main__':
    app.run(debug=True)
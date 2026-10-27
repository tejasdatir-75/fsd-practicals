from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def students():
    names = ["Tejas", "Sahil", "Amit", "Tanmay", "Pramod"]
    names.sort()

    return render_template('Q3.html', names=names)

if __name__ == '__main__':
    app.run(debug=True)
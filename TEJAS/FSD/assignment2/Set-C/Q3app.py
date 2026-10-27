from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def search():
    result = ""

    if request.method == 'POST':
        book = request.form['book']
        result = "Book Search Result: " + book

    return render_template('Q3.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
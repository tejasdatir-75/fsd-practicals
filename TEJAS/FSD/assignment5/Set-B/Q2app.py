from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        rating = request.form['rating']
        comments = request.form['comments']

        return render_template(
            'Q2.html',
            name=name,
            rating=rating,
            comments=comments,
            submitted=True
        )

    return render_template('Q2.html', submitted=False)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

name = "Tejas"
roll_no = 22
FSD = 80
JAVA = 75
VB_NET = 85

@app.route('/')
def student():
    total = FSD + JAVA + VB_NET
    average = total / 3

    return render_template(
        'Q1.html',
        name=name,
        roll_no=roll_no,
        FSD=FSD,
        JAVA=JAVA,
        VB_NET=VB_NET,
        total=total,
        average=average
    )

if __name__ == '__main__':
    app.run(debug=True)
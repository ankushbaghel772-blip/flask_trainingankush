from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index1.html')


@app.route('/calculate1', methods=['POST'])
def calculate1():

    a = float(request.form['a'])
    b = float(request.form['b'])

    addition = a + b
    subtraction = a - b
    multiplication = a * b

    if b != 0:
        division = a / b
    else:
        division = "Cannot divide by zero"

    return render_template(
        'index1.html',
        a=a,
        b=b,
        addition=addition,
        subtraction=subtraction,
        multiplication=multiplication,
        division=division,
    )


if __name__ == '__main__':
    app.run(debug=True)
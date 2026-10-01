from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello I am Ankush Baghel</h1>"

@app.route('/welcome')
def welcome():
    return "<h1>Welcome to Flask Training Class</h1>"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/sucess/<float:a>')
def sucess(a):
    return "the person is pass and the score is "+str(a)

@app.route('/fail/<float:a>')
def fail(a):
    return "the person is fail and the score is "+str(a)


@app.route('/calculate', methods=['POST', 'GET'])
def calculate():
    if request.method == 'GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])
        avg=(maths+science+history)/3
        result=""
        if avg>=80:
            result="sucess"
        else:
            result="fail"
        return redirect(url_for(result, a=avg))
             
        
    
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask,render_template


app = Flask(__name__)
comments={"thing","not a thing"}
#Chapter 3 Miguel Grinberg

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',comments=comments,user=name)
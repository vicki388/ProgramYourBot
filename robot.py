from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('layout.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)

@app.route('/robot/go/')
@app.route('/robot/go/<x>')
def StraightLine(x=1):
	x = int(x)
	return render_template('straight.html', x=x)

@app.route('/robot/square/')
@app.route('/robot/square/<x>')
def Square(x=1):
	x = int(x)
	return render_template('square.html', x=x)

@app.route('/robot/trick/')
def Trick(x=1):
	x = int(x)
	return render_template('trick.html', x=x)

@app.route('/robot/hexagon/')
def Hexagon(x=1):
	x = int(x)
	return render_template('hexagon.html', x=x)

@app.route('/robot/super/')
def Super(x=1):
	x = int(x)
	return render_template('super.html', x=x)

if __name__ == '__main__':
	app.debug = True
	app.run()
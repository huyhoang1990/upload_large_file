#! coding: utf-8


from flask import (Flask, jsonify, request,
                   render_template, url_for, redirect)



app =  Flask(__name__, static_folder='blueimp')

app.config['SECRET_KEY'] = '123342345345'

@app.route('/', methods=['GET','POST'])
def home():
	if request.method == 'GET':
		return render_template('index.html')
	else:
		print request.form	
		return "thanh cong cmnr"


@app.route('/upload', methods=['GET','POST'])
def upload():
	if request.method == 'GET':
		return render_template('index.html')
	else:
		print request.form	
		return "thanh cong cmnr"


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)



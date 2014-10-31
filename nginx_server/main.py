

#! coding: utf-8


from flask import (Flask, jsonify, request,
                   render_template, url_for, redirect)



app =  Flask(__name__, static_folder='blueimp')

app.config['SECRET_KEY'] = '123342345345'


@app.route('/internal_upload', methods=['GET','POST'])
def upload():

        if request.method == 'GET':
                return render_template('index.html')
        else:  
		print request.form.get('.path')
                return "thanh cong cmnr"


if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000, debug=True)



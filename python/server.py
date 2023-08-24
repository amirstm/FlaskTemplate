import pandas as pd
import numpy as np
import jdatetime, datetime, json
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
import os

print("Hello world!")

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "/uploaded/"
UPLOAD_PATH = "uploaded/"
if not os.path.exists(UPLOAD_PATH):
    os.makedirs(UPLOAD_PATH)

@app.route('/')
def hello_world():
   return render_template('index.html')

@app.route('/simple/<int:userId>')
def simple_userId(userId):
   return f'''
   <h1>A simple web page for user number {userId} :)</h1>
   '''

@app.route('/simple/<string:username>')
def simple_username(username):
   return f'''
   <h1>A simple web page for user {username} :)</h1>
   '''

@app.route('/simple')
def simple():
   name = request.cookies["input-name"]
   if name.isdigit():
      return redirect(url_for('simple_userId', userId = name))
   else:
      return redirect(url_for('simple_username', username = name))
   
@app.route('/cookie',methods = ['POST', 'GET'])
def cookie():
   if request.method == 'POST':
      user = request.form['name']
      resp = redirect(url_for('simple'))
      resp.set_cookie("input-name", user)
      return resp
   else:
      return render_template('cookie.html', time_display = datetime.datetime.now())

@app.route('/upload')
def upload_file_page():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['POST'])
def upload_file():
   f = request.files['file']
   f.save(f"{UPLOAD_PATH}{secure_filename(f.filename)}")
   return 'File uploaded successfully!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

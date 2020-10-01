from flask import Flask, render_template,request,redirect,url_for
import cv2
import numpy as np
from PIL import Image
import os
import threading
from werkzeug import secure_filename

def thread2():
      os.system('python "obdt img batch".py')
      
t1 = threading.Thread(target=thread2, args=[])

def thread4():
      os.system('python "obdt video inst".py')
      
t2 = threading.Thread(target=thread4, args=[])


app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd()+'\\ServerUploads'


@app.route('/')
def home():
    return render_template("html1.html")

@app.route('/detect')
def detect():
    return render_template("html2.html")

@app.route('/webcam')
def webcam():
    os.system('python object_detection_webcam_new.py')
    return render_template("html2.html")

@app.route('/ajax', methods = ['POST'])
def ajax_request():
    print('1')
    username = request.form['username']
    print(username)
    return

@app.route('/action_page.php', methods = ['POST'])
def request_1():
    global t1
    im1=Image.open(request.files['pic'])
    im=np.asarray(im1)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    cv2.imwrite('ServerUploads\\'+request.files['pic'].filename,im)
    t1.start()
    return render_template("html2.html")
    #return redirect(url_for('home'))


@app.route('/action_page1.php', methods = ['POST'])
def request_2():
    global t2
    app.config['UPLOAD_FOLDER'] = os.getcwd()+'\\ServerUploads'
    request.files['pic'].save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(request.files['pic'].filename)))
    t2.start()
    return render_template("html2.html")
    #return redirect(url_for('home'))

if __name__=="__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = None
    app.run(debug=True, host='0.0.0.0',port=1199)

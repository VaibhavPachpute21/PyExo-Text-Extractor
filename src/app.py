from flask import Flask
from flask import Flask, render_template, request, session
import os
from PyExo import PyExo
import json



app = Flask(__name__, template_folder='templates')

 
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/ProcessDoc/<string:url>', methods=['POST'])
def ProcessDoc(url):
    url=json.loads(url)
    print("URL:",url)
    return('/')

 
if __name__=='__main__':
    app.run(debug = True)
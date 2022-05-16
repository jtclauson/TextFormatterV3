from flask import render_template, redirect, url_for, request
from app import app
from format import Format
from format import Formatted
import logging

@app.route('/', methods=['GET', 'POST'])
def index():
    # logging.basicConfig(filename="std.log", 
					# format='%(asctime)s %(message)s', 
					# filemode='w') 
    # logger=logging.getLogger() 

    #Now we are going to Set the threshold of logger to DEBUG 
    # logger.setLevel(logging.DEBUG) 

    #some messages to test
    # logger.debug("here01") 

    if request.method == 'POST':
        # text = request.form["text"]
        input = request.form
        formatted = Format(input)
        return redirect(url_for('formatted', testvar="toast"))
        # return redirect(url_for('formatted', text=text))
    return render_template('index.html')

@app.route("/formatted", methods=['GET', 'POST'])
def formatted(testvar):
    # testvar="jam"
    # text = request.form.get('text')
    # input = request.form.get('formatted')
    return render_template('formatted.html', testvar=testvar)
    # return render_template('formatted.html')
    # return render_template('formatted.html', text=text)
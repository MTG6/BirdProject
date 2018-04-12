from flask import Flask, render_template, request, redirect, url_for, flash
from app import app
from develop.eda_functions import top5_bird
from develop.data_input import *
import pandas as pd


#Homepage
@app.route('/')
def index():
	res = 'Bird Paradise'
	
	#Code
	df = read_data('Oregon')
	top5 = top5_bird(df, year = 2010)
	
	#return variables
	return render_template("landing.html" , output1=res , output2=top5)

@app.route('/stateSelect', methods=['POST'])
def stateSelect():
	states = request.form['States']
	return states

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0")
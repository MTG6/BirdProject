from flask import Flask, render_template, request, redirect, url_for, flash
from app import app
from develop.eda_functions import top5_bird
from develop.data_input import *
import pandas as pd


#Homepage
@app.route('/')
def index():
	res = 'Bird Paradise'
	
	#return variables
	return render_template("landing.html" , output1=res)

@app.route('/stateSelect', methods=['POST'])
def stateSelect():
	states = request.form['States']
	df = read_data(states)
	top5 = top5_bird(df, year = 2010)
	
	return render_template("result.html", output2 = str(states+str(len(top5))))

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0")
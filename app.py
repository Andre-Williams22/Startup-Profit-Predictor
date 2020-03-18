from flask import Flask, render_template, requests, request
from sklearn.externals import joblib
import pandas as pd 
import numpy as np 


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
        # implement pickle file here

        except ValueError: 


    return render_template('predict.html', )

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, requests, request
from sklearn.externals import joblib
import pandas as pd 
import numpy as np 


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


# Model Processing
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # implement pickle file here
        try:
            # grabs data from form input from the user on home page
            NewYork = float(request.form['NewYork'])
            California = float(request.form['California'])
            Florida = float(request.form['Florida'])
            RnDSpend = float(request.form['RnDSpend'])
            AdminSpend = float(request.form['AdminSpend'])
            MarketSpend = float(request.form['MarketSpend'])
            # create a list of these values
            pred_args = [NewYork,California,Florida,RnDSpend,AdminSpend,MarketSpend]
            # convert list values into an array 
            pred_args_array = np.array(pred_args)
            # reshape the array for onehotencoding 
            new_pred_args_array = pred_args_array.reshape(1, -1)
            # grab model from jupyter notebook from pkl file
            mlr_model = open('multiple_linear_regression.pkl', 'rb')
            multiple_linear_regression_model = joblib.load(mlr_model)
            # make prediction on data from form
            model_prediction = mlr_model.predict(new_pred_args_array)
            model_prediction = round(float(model_prediction), 2)

        except ValueError: 
            return "Please Enter Values for the Required fields"
            
    return render_template('predict.html', prediction=model_prediction)


if __name__ == '__main__':
    app.run(debug=True)
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 16:55:57 2021

@author: sai kumar
"""

from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import pickle
import os
app = Flask(__name__)
model = pickle.load(open('PCA_modelm.pkl', 'rb'))
@app.route('/')
def home():
    return render_template("pca.html")
@app.route('/predict',methods=["POST","GET"])

def predict():
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]
    
    features_name = ['Global_reactive_power', 'Global_intensity','sub_metering_1',
                     
                    
                     'sub_metering_2', 'sub_metering_3']
    
    df = pd.DataFrame(features_value,columns=features_name)
    output = model.predict(df)
    
    
    
    return render_template('result1.html', prediction_text=output)
if __name__=="__main__":
    #port = int(os.getenv('PORT', 8080))
    #app.run(host='0.0.0.0', port=port,debug=False)
    app.run(debug=True)
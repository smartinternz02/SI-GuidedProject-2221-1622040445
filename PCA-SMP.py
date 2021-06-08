# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 17:56:27 2021

@author: sai kumar
"""

import requests
import json 


API_KEY = "EiDUIP3-cahKLT7xxJ4ud8z_vx3l_25y9Sq8K690YmC1"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}


payload_scoring ={"input_data":[{"field":[["Global_reactive_power","Global_intensity","Sub_metering_1","Sub_metering_2","Sub_metering_3"]],
                   "values": [[0.418,18.4,0.0,1.0,17.0]]    }]}
response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/a4eb25d4-1299-4693-b8b9-203e95b41705/predictions?version=2021-06-05', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})


predictions= response_scoring.json()
pred= predictions["predictions"][0]['values'][0][0]
print("The Global Active Power is " + str(pred))
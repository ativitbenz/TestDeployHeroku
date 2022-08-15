from io import TextIOBase
import pickle
import numpy as np

#################
import requests
import oci
from oci.signer import Signer

from flask import Flask, render_template, request
# from werkzeug.datastructures import Authorization
#################

# Authentication # 
config = oci.config.from_file("~/.oci/config") # replace with the location of your oci config file
auth = Signer(
  tenancy=config['tenancy'],
  user=config['user'],
  fingerprint=config['fingerprint'],
  private_key_file_location=config['key_file'],
  pass_phrase=config['pass_phrase'])

##################
# endpoint # 
endpoint_model = "https://modeldeployment.ap-sydney-1.oci.customer-oci.com/ocid1.datasciencemodeldeployment.oc1.ap-sydney-1.amaaaaaan3rf7taatzoaygvcic5cenavowsuponomnvwfsmisqdfmzl573iq/predict"
##################


app = Flask(__name__)
# model = pickle.load(open('churn_model.pkl', 'rb')) # when use model deploy 

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])

def getPredict():
    x1 = request.form['x1']
    x2 = request.form['x2']
    x3 = request.form['x3']
    x4 = request.form['x4']
    x5 = request.form['x5']
    x6 = request.form['x6']
    x7 = request.form['x7']
    x8 = request.form['x8']
    x9 = request.form['x9']
    x10 = request.form['x10']
    x11 = request.form['x11']
    x12 = request.form['x12']
    x13 = request.form['x13']
    x14 = request.form['x14']
    x15 = request.form['x15']
    x16 = request.form['x16']
    x17 = request.form['x17']
    # x18 = request.form['x18']
    # x19 = request.form['x19']

    # body = {"gender":{"0":x1},"SeniorCitizen":{"0":x2},
    #     "Partner":{"0":x3},"Dependents":{"0":x4},
    #      "tenure":{"0":x5}, "PhoneService":{"0":x6}, "MultipleLines":{"0":x7},
    #     "InternetService":{"0":x8},"OnlineSecurity":{"0":x9},
    #     "OnlineBackup":{"0":x10},"DeviceProtection":{"0":x11},
    #     "TechSupport":{"0":x12},"StreamingTV":{"0":x13},
    #     "StreamingMovies":{"0":x14},"Contract":{"0":x15},
    #     "PaperlessBilling":{"0":x16},"PaymentMethod":{"0":x17},
    #     "MonthlyCharges":{"0":x18},"TotalCharges":{"0":x19}}

    body = {"gender":{"0":x1},"SeniorCitizen":{"0":x2},
        "Partner":{"0":x3},"Dependents":{"0":x4},
         "tenure":{"0":x5}, "MultipleLines":{"0":x6},
        "InternetService":{"0":x7},"OnlineSecurity":{"0":x8},
        "OnlineBackup":{"0":x9},"DeviceProtection":{"0":x10},
        "TechSupport":{"0":x11},"StreamingTV":{"0":x12},
        "StreamingMovies":{"0":x13},"Contract":{"0":x14},
        "PaperlessBilling":{"0":x15},"PaymentMethod":{"0":x16},
        "MonthlyCharges":{"0":x17}}



    # XTest = np.array([[x1, x2, x3, x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19]], dtype = np.float64)
    # XTest = [[x1, x2, x3, x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19]]
    
    predicted = requests.post(endpoint_model, json=body, auth=auth).json()
    # result = list(predicted.values())[0]
    # result_str = str(result)
    # if result_str == '[True]':
    #     print('True')
    # else :
    #     print('False')
    pred = predicted.get('prediction')
    pred = str(pred)
    if pred == '[1]':
        return render_template('index.html', prediction_text = f'Customer churn')
    else :
        return render_template('index.html', prediction_text = f'Customer not churn')
 
if __name__ == '__main__':
    app.run(debug = True)
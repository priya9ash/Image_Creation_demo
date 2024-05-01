from flask import Flask, request
import pickle
import pandas as pd

app=Flask(__name__)

model=pickle.load(open('classifier.pkl',mode="rb"))

@app.route('/ping')
def printmyname():
    return('hello debapriya')


@app.route('/predict',methods=["POST"])
def prediction():
    loan_req=request.get_json()
    loan_req=pd.DataFrame(loan_req,index=[0])
    loan_req['Gender']=loan_req["Gender"].map({"Male":0,"Female":1})
    loan_req["Married"]=loan_req['Married'].map({"No":0,"Yes":1})
    loan_req=loan_req[["Gender",'Married',"ApplicantIncome","Credit_History"]]
    prediction=model.predict(loan_req)
    if prediction==0:
        pred="Rejected"
    else:
        pred="Accepted"

    return{"prediction":pred}        


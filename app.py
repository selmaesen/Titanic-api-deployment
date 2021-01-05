import pandas as pd 
import numpy as np
import re
from flask import Flask, request, jsonify, render_template
import pickle 


from pipeline.predict.predict import predict
from pipeline.preprocessing.preproccessing import preprocess
import pipeline.model as model

app = Flask(__name__)


@app.route("/", methods = ["GET"])
def home():
    return "Alive!"

@app.route("/predict", methods = ["POST"])
def predict_api():

    if request.method == "POST":
        input_data = request.get_json()
        print (type(input_data["Embarked"]))
        
        
        if input_data["Pclass"] not in [1, 2, 3]:
            return "Pclass must be 1, 2 or 3"
        elif re.search(' ([A-Za-z]+)\.', input_data["Name"]).group(1) not in ['Don','Lady', 'Sir','Countess','Jonkheer', 'Mr', 'Mrs', 'Mme', 'Ms', 'Miss', 'Master','Mlle', 'Major', 'Dr', 'Col', 'Capt', 'Rev']:
            return "The name must contain an title of the person. the available titles: 'Don.','Lady.', 'Sir.','Countess.','Jonkheer.', 'Mr.', 'Mrs.', 'Mme.', 'Ms.', 'Miss.', 'Master.','Mlle.', 'Major.', 'Dr.', 'Col.', 'Capt.', 'Rev.' . The name must contain one of them"
        elif input_data["Age"] > 89 or input_data["Age"] < 0:
            return "The age must be in range of 0 - 89. If there is no age information, please type - NaN - without dashes."
        elif type(input_data["SibSp"]) != int:
            return "SibSp is the number of siblings/spouses sboard so it must be intiger"
        elif type(input_data["Parch"]) != int:
            return "SibSp is the number of parents/children aboard so it must be intiger"
        elif input_data["Embarked"] is None:
            
            input_df = pd.DataFrame(input_data, index=[0, ])
            print (input_df["Embarked"])

            prp_df = preprocess(input_df)
                
            if predict(prp_df)[0].item() == 0:
                    return "sorry"
            else:
                    return "alive!"

        elif input_data["Embarked"] in ["S", "C", "Q"]:
            
            input_df = pd.DataFrame(input_data, index=[0, ])
            print (input_df["Embarked"])

            prp_df = preprocess(input_df)
                
            if predict(prp_df)[0].item() == 0:
                    return "sorry"
            else:
                    return "alive!"
        else:   
            return "Embarked can be only S, C or Q. If you don't have the information, please type - null - without dashes."

if __name__ == '__main__':
    app.run()

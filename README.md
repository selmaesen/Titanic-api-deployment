# Titanic-api-deployment

### Date

29.12.2020

### Introduction:

This project assumes that the Titanic disaster happens again in a parallel universe. You can check wather someone would survive or not if she/he was in Titanic in this parallel universe. I have created an API to get new passanger information and return a prediction. The API Wrapped by a Docker file and deployed by Heroku.

### Input:
```json
{
    "PassengerId": [int], 
    "Pclass": 1 / 2 / 3, 
    "Name": [str] (must contain a title of the passanger), 
    "Sex": "male" / "female", 
    "Age": [int] / NaN, 
    "SibSp":[int], 
    "Parch":[int],
    "Ticket":[str], 
    "Fare":[int], 
    "Cabin":[str], 
    "Embarked":"S" / "Q" / "C" / null
}
 ```
 
 ### Output:
 If your passanger predicted as alive, the response will be "Alive!"
 If your passanger predicted as dead, the response will be "Sorry"
 If your input is invalid you will get an error massage according to your input.
 
 ### File structure:

    .
    ├── ...
    ├── docker                    
    │   ├── Dockerfile                           
    ├── pipeline                    
    │   ├── model
    │       ├── model.py
    │       ├── model.pkl
    │       ├── ready_to_model_df.csv
    │   ├── predict
    │       ├── predict.py
    │   ├── preprocessing 
    │       ├── preprocessing.py
    │       │── test-dataframe.csv
    ├── Procfile
    ├── app.py
    ├── requirements.txt
    ├── README.md
 
### Details:

The ***model.py*** file makes use of KNN machine learning model and dumps it into a pickle file.

The ***predict.py*** file imports and loads the pickle file with data for the prediction and executes the prediction.

The ***preprocessing.py*** file deals with cleaning and preprocessing. Processing the data ready to feed the model and make predictions.

The ***app.py*** file creates an API with Flask and dealing with the error massages

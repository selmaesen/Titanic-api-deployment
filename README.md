# Titanic-api-deployment

### Date

29.12.2020

### Introduction:

This project assumes that the Titanic disaster happens again in a parallel universe. You can check wather someone would survive or not if she/he was in Titanic in this parallel universe. I have created an API to get new passanger information and return a prediction. The API Wrapped by a Docker file and deployed by Heroku.

### Input:
{
    "PassengerId": int, 
    "Pclass": 1 / 2 / 3, 
    "Name": str (must contain a title of the passanger), 
    "Sex": "male" / "female", 
    "Age": int / NaN, 
    "SibSp":int, 
    "Parch":int,
    "Ticket":str, 
    "Fare":int, 
    "Cabin":str, 
    "Embarked":"S" / "Q" / "C" / null
}
 

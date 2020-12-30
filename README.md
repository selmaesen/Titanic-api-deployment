# Titanic-api-deployment

### Date

29.12.2020

### Introduction:

This project assumes that the Titanic disaster happens again in a parallel universe. You can check wather someone would survive or not if she/he was in Titanic in this parallel universe. I have created an API to get new passanger information and return a prediction. The API Wrapped by a Docker file and deployed by Heroku. This project is another version of well-known Kaggle Titanic challange. The datasets are also istalled from the kaggle website.

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

The ***model.py*** file makes use of KNN machine learning model and dumps it into a pickle file. This model has chosen because it has given the most efficient accuracy from kaggle website. 

The ***predict.py*** file imports and loads the pickle file with data for the prediction and executes the prediction.

The ***preprocessing.py*** file deals with cleaning and preprocessing. Processing the data ready to feed the model and make predictions.

The ***app.py*** file creates an API with Flask and dealing with the error massages.

### To Run:
There are two most afficient ways to run the model. The first one is on your local machine and the second one is using the Heroku application.

#### 1. Local:

### Docker File

After you clone the repo to your local machine:

#### image creation
docker build -f docker/Dockerfile . -t image_name:tag_name

#### docker run
docker run -it image_name:tag_name

#### run
Run the app.py file. Copy the provided link and paste on Postman application to try.


## Heroku 

### You can find the link [here](https://titanic-deployment-api.herokuapp.com/)

#### run
- You can input the information of your passanger and get the result by adding */predict* after the link.
- You can use Postman. * POST: Returns the prediction or an error message in case of error.

#### Input Example:
You can directly copy this to play around on Postman. (The data below is not real)

```json
{
    "PassengerId": 2, 
    "Pclass": 1, 
    "Name": "Futrelle, Mrs. Jacques Heath (Lily May Peel)", 
    "Sex": "female", 
    "Age": 67, 
    "SibSp":2, 
    "Parch":0,
    "Ticket":"PC 17599", 
    "Fare":71.2833, 
    "Cabin":"C85", 
    "Embarked":null
}
´´´



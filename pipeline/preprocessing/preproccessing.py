import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder
import category_encoders as ce
import re


train_df = pd.read_csv("pipeline/preprocessing/train.csv")

def title2(df):
    """This fuction extracts the titles from the passangers' names and 
    coverts them under five different categories and saves under title2 column"""
    
    def get_title(name):
        title_search = re.search(' ([A-Za-z]+)\.', name)
        if title_search:
            return title_search.group(1)
        return ""
    
    df["title"] = df["Name"].apply(get_title)
    
    def title_group(title):
        royal = ['Don','Lady', 'Sir','Countess','Jonkheer']
        ordinary = ['Mr', 'Mrs', 'Mme', 'Ms']
        minor = ['Miss', 'Master','Mlle']
        officer = ['Major', 'Dr', 'Col', 'Capt']
        religious = ["Rev"]
        if title in royal:
            return "royal"
        elif title in ordinary:
            return "ordinary"
        elif title in minor:
            return "minor"
        elif title in religious:
            return "religious"
        else:
            return "officer"
    
    df["title2"] = df["title"].apply(title_group)
    
    return(df)

def age_imp(df):
    #imputting missing ages by mean value which astimated according to gender and class
    Sex = ["female", "male"]
    Pclass = [1,2,3]
    
    for s in Sex:
        for c in Pclass:
            df.loc[(df["Pclass"] ==c)& 
                   (df["Sex"] == s)& 
                   (df["Age"].isnull()), "Age"] = round(df.loc[(df["Pclass"] == c)&(df["Sex"] == s)].Age.mean())
            
    return df

def embarked_imp(df):
    #imputting missing embarked coumn values
    df.Embarked.fillna(df.Embarked.mode().iloc[0], inplace = True)
    return df

def age_group_2(df):
   
    age_labels = ['0-14',"15-29","30-44","45-59", '60-74', "75-89"]
    df['age_group_2'] = pd.cut(df.Age, range(0, 92, 15), right=False, labels=age_labels)
    return df

def family(df):
    df["family_size"] = df["Parch"]+df["Parch"] + 1
    return df

def drop_cols(df):
    df = df.drop(columns=["Parch", "SibSp", "Fare", "Ticket", "Cabin", "Name", "PassengerId", "Age", "title"])
    return df

def to_numeric(df):
    ohe = ce.OneHotEncoder(handle_unknown="ignore", use_cat_names=True)
    df = ohe.fit_transform(df)
    return df

func_list = [title2, age_imp, embarked_imp, age_group_2, family, drop_cols, to_numeric]

for f in func_list:
    train_df = f(train_df)

train_df.to_csv('preprocessed_train_df.csv', index=False)

def preprocess(df):
    test_df = pd.read_csv("pipeline/preprocessing/test.csv")
    test_df = pd.concat([test_df, df])
    
    
    func_list = [title2, age_imp, embarked_imp, age_group_2, family, drop_cols, to_numeric]

    for f in func_list:
        test_df = f(test_df)

    for column in [x for x in train_df.columns.tolist() if x not in test_df.columns.tolist()]:
        if column != "Survived":
            test_df[column] = 0

    df = test_df.tail(1)

    return df
    


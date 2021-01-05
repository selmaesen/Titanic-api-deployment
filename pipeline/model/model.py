import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import pickle

if __name__ == "__main__":
    train_df= pd.read_csv("preprocessed_train_df.csv")
    X_train = train_df.drop(columns=["Survived"])
    y_train = train_df["Survived"] 

    knn = KNeighborsClassifier(n_neighbors = 5)
    knn.fit(X_train, y_train)

    print (knn.score(X_train, y_train)) 
    pickle.dump(knn, open('pipeline/model/model.pkl', 'wb'))

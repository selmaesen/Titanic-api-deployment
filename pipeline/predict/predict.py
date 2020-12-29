import pickle

model_pkl = pickle.load(open('pipeline/model/model.pkl', 'rb'))

def predict(df):
    print (df.shape)
    return model_pkl.predict(df)
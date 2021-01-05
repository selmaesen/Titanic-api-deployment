import pickle


def predict(df):
    model_pkl = pickle.load(open('pipeline/model/model.pkl', 'rb'))
    print (df.shape)
    return model_pkl.predict(df)

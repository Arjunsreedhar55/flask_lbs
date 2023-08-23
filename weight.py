import pickle

def prediction(height):
    model=pickle.load(open('model.pkl','rb'))
    weigh=model.predict(height)
    print(weigh)
    return weigh
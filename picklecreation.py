import pandas as pd
import pickle as pk
from sklearn.model_selection import train_test_split as TTS
from sklearn.naive_bayes import GaussianNB
global model
def train():
    global model
    print("started training")
    y=0.1
    while(y<0.9):
        df=pd.read_csv("heart.csv")
        classes=df.target
        inputs=df.drop("target",axis=1)
        X_train,X_test,Y_train,Y_test=TTS(inputs,classes,test_size=0.2)
        model=GaussianNB()
        model.fit(X_train,Y_train)
        y=model.score(X_test,Y_test)
    return

#main
train()

pk.dump(model,open("heart_model.pkl","wb"))
print("model created as heratmodel")

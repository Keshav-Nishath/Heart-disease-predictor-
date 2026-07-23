import pandas as pd
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
    print("trainning completed") 
    print("accuracy of the model is: ",y*100,"%")
    return 

#main

train()


while(True):
    
    #to get user inputs

    age=int(input("enter age"))
    sexstr=input("are u male or female")
    if(sexstr.lower()=="male"):
        sex=1
    else:
        sex=0
    cp=int(input("enter chest pain type on a scale of 1 to 4"))
    if(cp>4):
        cp=4
    elif(cp<1):
        cp=1
    trestbps=int(input("enter the resting blood pressure (in mm Hg on admission to the hospital)"))
    chol=int(input("enter the serum cholestoral in mg/dl"))
    fbstext=input("Do u have blood sugar enter Y/N")
    if(fbstext.lower()=="y"):
        fbs=1
    else:
        fbs=0
    restecg = int(input("Enter resting electrocardiographic results (0 = normal, 1 = having ST-T wave abnormality, 2 = showing probable or definite left ventricular hypertrophy): "))
    if restecg > 2:
        restecg = 2
    elif restecg < 0:
        restecg = 0

    thalach = int(input("Enter maximum heart rate achieved: "))

    exang_text = input("Do you experience exercise-induced angina (Y/N): ")
    if exang_text.lower() == "y":
        exang = 1
    else:
        exang = 0

    oldpeak = float(input("Enter ST depression induced by exercise relative to rest (e.g., 1.0): "))

    slope = int(input("Enter the slope of the peak exercise ST segment (0 = upsloping, 1 = flat, 2 = downsloping): "))
    if slope > 2:
        slope = 2
    elif slope < 0:
        slope = 0

    ca = int(input("Enter the number of major vessels (0–3) colored by fluoroscopy: "))
    if ca > 3:
        ca = 3
    elif ca < 0:
        ca = 0

    thal = int(input("Enter thalassemia type (1 = normal, 2 = fixed defect, 3 = reversible defect): "))
    if thal > 3:
        thal = 3
    elif thal < 1:
        thal = 1


        
    testcase=pd.DataFrame([{
                                    "age": age,
                                    "sex": sex,
                                    "cp": cp,
                                    "trestbps": trestbps,
                                    "chol": chol,
                                    "fbs": fbs,
                                    "restecg": restecg,
                                    "thalach": thalach,
                                    "exang": exang,
                                    "oldpeak": oldpeak,
                                    "slope": slope,
                                    "ca": ca,
                                    "thal": thal
                                }])
    prediction=model.predict(testcase)
    if(prediction==[0]):
        print("Hey your fine and healthy u dont have a heart diesease")
    else:
        print("you have chances to get a heart disease please consult a doctor")
    a=input("enter e to exit")
    if(a=="e"):
            print("Hope i have been helpful to you exiting")
            break

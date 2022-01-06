import pickle
import json
import numpy as np
import pandas as pd


__diseases = None
__data_columns = None
__model = None

df1 = pd.read_csv("D:/actimi/deployment/PredictDiseases/server/Symptom-severity.csv")
desc = pd.read_excel("D:/actimi/deployment/PredictDiseases/server/symptom_Description.xlsx")
prec = pd.read_excel("D:/actimi/deployment/PredictDiseases/server/symptom_precaution.xlsx")
def predict_disease(S1,S2,S3,S4,S5=0,S6=0):


    psymptoms = [S1, S2, S3, S4, S5, S6]


    #print(psymptoms)
    a = np.array(df1["Symptom"])
    b = np.array(df1["weight"])
    for j in range(len(psymptoms)):
        for k in range(len(a)):
            if psymptoms[j] == a[k]:
                psymptoms[j] = b[k]

    psy = [psymptoms]

    with open('D:/actimi/deployment/PredictDiseases/server/artifacts/SympDetector.pkl', 'rb') as f:
        __model = pickle.load(f)

    pred2 = __model.predict(psy)
    #print(pred2[0])
    global __a
    __a = desc.index[desc['diseases'] == str(pred2[0])][0]
    print(pred2[0])
    return (pred2[0])


def description():

   return(desc.loc[__a, 'description'])


def precaution():

    return (prec.loc[__a, 'Precaution_1'],prec.loc[__a, 'Precaution_2'],prec.loc[__a, 'Precaution_3'],prec.loc[__a, 'Precaution_4'])

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __diseases

    with open("D:/actimi/deployment/Predict_Disease/server/artifacts/columns_symptom.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        print(__data_columns)


    with open("D:/actimi/deployment/Predict_Disease/server/artifacts/columns_diseases.json", "r") as ff:
        __diseases = json.load(ff)['data_columns']


    global __model
    if __model is None:
        with open('D:/actimi/deployment/PredictDiseases/server/artifacts/SympDetector.pkl', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_diseases_names():
    global __diseases
    load_saved_artifacts()

    return __diseases

def get_data_columns():
    global __data_columns
    load_saved_artifacts()
    return __data_columns


if __name__ == '__main__':


    #get_diseases_names()
    #get_data_columns()

    predict_disease('chills', 'skin_rash', 'shivering', 'weight_gain', 'muscle_wasting', 'loss_of_appetite')
    predict_disease('chills', 'skin_rash', 'shivering', 'weight_gain')
    predict_disease('chills', 'skin_rash', 'shivering', 'weight_gain', 'muscle_wasting')
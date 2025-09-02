import os
import sys

import numpy as np 
import pandas as pd
import pickle
import dill
from src.exception import CustomException
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
def save_object(file_path, obj):
   try:
    path = os.path.dirname(file_path)
    os.makedirs(path, exist_ok=True)
    with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

   except Exception as e:
        raise CustomException(str(e), sys)
def evaluate_models(xtrain,ytrain,xtest,ytest,models,params):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            param = params[list(models.keys())[i]]
            gs = GridSearchCV(model,param,cv=3)
            gs.fit(xtrain,ytrain)
            model.set_params(**gs.best_params_)
            model.fit(xtrain,ytrain)
            y_test_pred = model.predict(xtest)
            y_train_pred = model.predict(xtrain)
            test_model = r2_score(ytest,y_test_pred)
            train_model = r2_score(ytrain,y_train_pred)
            report[list(models.keys())[i]] = test_model
        return report 
    except Exception as e:  
                raise CustomException(str(e), sys)
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(str(e), sys)




   
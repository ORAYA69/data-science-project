import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging
import os
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"proprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    def data_transformation_function(self):
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]
            logging.info("Numerical columns and categorical columns defined")
            cat_p = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ('onehot',OneHotEncoder()),
                    ("scaler",StandardScaler(with_mean=False))

                ]
            )
            num_p = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="mean")),
                    ("scaler", StandardScaler())
                ]
            )
            logging.info("Pipeline created for numerical and categorical columns")
            preprocessor = ColumnTransformer(
                transformers=[
                    ("num", num_p, numerical_columns),
                    ("cat", cat_p, categorical_columns)
                ]
            )
            return preprocessor
        except Exception as e:
            raise CustomException(str(e), sys)
    def initiate_data_transformation(self, train_path, test_path):
            try:
                train = pd.read_csv(train_path)
                test = pd.read_csv(test_path)
                logging.info("Train and test data read successfully")
                preprocessing_obj = self.data_transformation_function()
                target_column_name="math_score"
                numerical_columns = ["writing_score", "reading_score"]

                input_feature_train_df=train.drop(columns=[target_column_name],axis=1)
                target_feature_train_df=train[target_column_name]

                input_feature_test_df=test.drop(columns=[target_column_name],axis=1)
                target_feature_test_df=test[target_column_name]

                logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

                input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
                input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

                train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
                test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

                logging.info(f"Saved preprocessing object.")
                save_object(
                    file_path=self.data_transformation_config.preprocessor_obj_file_path,
                    obj=preprocessing_obj
                )
                return (
                    train_arr,
                    test_arr,
                    self.data_transformation_config.preprocessor_obj_file_path
                )
            except Exception as e:
                raise CustomException(str(e), sys)
if __name__ == "__main__":
    obj = DataTransformation()
    obj.initiate_data_transformation(
        train_path="artifacts/train.csv",
        test_path="artifacts/test.csv"
    )












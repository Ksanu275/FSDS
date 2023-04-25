import os
import sys
from  dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder,StandardScaler
from src.exception import CustomException
from src.logger import logging

@dataclass
class  DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')

class DataTranformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
    def get_data_tranformation_object(self):
        try:
            logging.info('Data Transformation Initiated')
            #define which columns should be ordinal -encoded and which should be scaled
            categorical_cols=['cut','color','clarity']
            numerical_cols=['carat','depth','table','x','y','z']


            #define the custom ranking for each ordinal variable
            cut_categories=['Fair','Good','Very Good','Premium','Ideal']
            color_categories=['D','F','E','G','H','I','J']
            clarity_categories=['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']
            
            
            #Numerical Pipline
            num_pipline=Pipeline(
                setp=[
                ('imputer',SimpleImputer(strategy='median')),
                ('scaler',StandardScaler())
                ]
            )

            preprocessor=ColumnTransformer([
            ('num_pipline',num_pipline,numerical_cols),
            ('cat_pipline',cat_pipline,categorical_cols)
            ])

            return preprocessor
            logging.info("pipline Completed")
        except Exception as e:
            logging.info('Error in the data transformation')
            raise CustomException(e,sys)





#!/usr/bin/env python
# coding: utf-8

import pandas as pd 
import numpy as np
from itertools import chain
from sklearn.preprocessing import StandardScaler, OneHotEncoder, MinMaxScaler
from sklearn.impute import SimpleImputer

from src.clean import app_train_clean, app_test_clean
from src.variables import target, id_var, categoric, numeric


def process_categoric(train:pd.DataFrame, test:pd.DataFrame, categoric:list):
  
    train, test = cat_na_assign(train, test, categoric)

    train, test, ohe_cols = one_hot_encoding(train, test, categoric)

    return train.drop(categoric, axis = 1), test.drop(categoric, axis = 1)

def cat_na_assign(train:pd.DataFrame, test:pd.DataFrame, categoric):
    for i in categoric :
        train[i] = train[i].replace(['','nan', np.nan], 'no asignado')       
        test[i] = test[i].replace(['','nan', np.nan], 'no asignado')       

    return train, test

def one_hot_encoding(train:pd.DataFrame, test:pd.DataFrame, categoric):
    enc = OneHotEncoder(handle_unknown='ignore')
    train_cat = enc.fit_transform(train[categoric].astype(str))
    test_cat = enc.transform(test[categoric])
    ohe_cols = [] 
    for i,j in zip(categoric, enc.categories_):
        ohe_cols.extend([i + '_' + j])
    res = [list(item) for item in ohe_cols]
    ohe_cols = list(chain(*res))
    train[ohe_cols] =  pd.DataFrame(train_cat.toarray(), columns = ohe_cols, index=train.index)
    test[ohe_cols] =  pd.DataFrame(test_cat.toarray(), columns = ohe_cols, index=test.index)

    return train, test, ohe_cols



def impute_scale(app_train, app_test):
    # Drop the target and id from the training data
    train = app_train.copy()
    # Feature names
    features = list(train.columns)
    # Copy of the testing data
    test = app_test.copy()
    # Median imputation of missing values
    imputer = SimpleImputer(strategy = 'median')
    # Scale each feature to 0-1
    scaler = MinMaxScaler(feature_range = (0, 1))

    imputer.fit(train)
    train = imputer.transform(train)
    scaler.fit(train)
    train = scaler.transform(train)
    test = scaler.transform(test)
    
    return train, test , features

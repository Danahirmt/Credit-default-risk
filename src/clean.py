#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from src.read_data import app_train, app_test

def clean(df):
    df.columns= df.columns.str.lower()
    df = df.apply(lambda x: x.str.lower() if(x.dtype == 'object') else x)
    df = df.apply(lambda x: x.str.replace(' ', '_') if(x.dtype == 'object') else x)
    return df

app_train_clean = clean(app_train)
app_test_clean = clean(app_test)
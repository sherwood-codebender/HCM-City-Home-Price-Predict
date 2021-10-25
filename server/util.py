# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 10:48:28 2021

@author: Sherwood
"""

import pickle
import json
import numpy as np

__locations = None
__status = None
__data_columns = None
__model = None

def get_estimated_price(vitri, dientich, sophong, wc, giayto):
    try:
        loc_index_vitri = __data_columns.index(vitri.lower())
        loc_index_giayto = __data_columns.index(giayto.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = dientich
    x[1] = sophong
    x[2] = wc
    
    if loc_index_vitri >=0 & loc_index_giayto >=0:
        x[loc_index_vitri] = 1
        x[loc_index_giayto] = 1
        
    return round(__model.predict([x])[0],2)
    

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations
    global __status

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:-3]  
        __status  = __data_columns[-3:]

    global __model
    if __model is None:
        with open('./artifacts/HCMCity_Home_Prices_Model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_status_names():
    return __status

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    # print(get_status_names())
    # print(__data_columns)
    # print(get_estimated_price('Quận 7', 57, 2, 1, 'Chưa có sổ'))

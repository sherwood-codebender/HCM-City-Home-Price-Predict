# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 10:42:56 2021

@author: Sherwood
"""

from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

# def get_status_name

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    dientich = float(request.form['dientich'])
    vitri = request.form['vitri']
    sophong = int(request.form['sophong'])
    wc = int(request.form['wc'])
    giayto = request.form['giayto']
    
    response = jsonify({
        'estimated_price': util.get_estimated_price(vitri, dientich, sophong, wc, giayto)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
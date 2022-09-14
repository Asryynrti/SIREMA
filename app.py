# Import modules and packages
from flask import (
    Flask,
    request,
    render_template,
    url_for )
import pickle
import numpy as np
from scipy.spatial import distance

app = Flask(__name__, template_folder = 'template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/kbk')
def kbk():
    return render_template('pilihkbk.html')

@app.route('/tentang')
def tentang():
    return render_template('tentang.html')

@app.route('/info')
def info():
    return render_template('informasi.html')

@app.route('/', methods=['POST'])
def get_input_values():
    val = request.form['my_form']


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'GET':
        return 'The URL /predict is accessed directly. Go to the main page firstly'

    if request.method == 'POST':
        input_val = request.form

        if input_val != None:
            # collecting values
            vals = []
            for key, value in input_val.items():
                vals.append(float(value))

        # Calculate Euclidean distances to freezed centroids   
        with open('telkom_centroid.pkl', 'rb') as file:
            telkom_centroid = pickle.load(file)


        assigned_clusters = []
        l = []  # list of distances

        for i, this_segment in enumerate(telkom_centroid):
            dist = distance.euclidean(vals, this_segment)
            l.append(dist)
            index_min = np.argmin(l)
            assigned_clusters.append(index_min)

        return render_template(
            'predict.html', result_value=f'  {index_min}'
            )


@app.route('/predict1', methods=['POST', 'GET'])
def predict1():
    if request.method == 'GET':
        return 'The URL /predict is accessed directly. Go to the main page firstly'

    if request.method == 'POST':
        input_val = request.form

        if input_val != None:
            # collecting values
            vals = []
            for key, value in input_val.items():
                vals.append(float(value))

        # Calculate Euclidean distances to freezed centroids   
        with open('sib_centroid.pkl', 'rb') as file:
            sib_centroid = pickle.load(file)


        assigned_clusters = []
        l = []  # list of distances

        for i, this_segment in enumerate(sib_centroid):
            dist = distance.euclidean(vals, this_segment)
            l.append(dist)
            index_min = np.argmin(l)
            assigned_clusters.append(index_min)

        return render_template(
            'predict1.html', result_value1=f' {index_min}'
            )

@app.route('/predict2', methods=['POST', 'GET'])
def predict2():
    if request.method == 'GET':
        return 'The URL /predict is accessed directly. Go to the main page firstly'

    if request.method == 'POST':
        input_val = request.form

        if input_val != None:
            # collecting values
            vals = []
            for key, value in input_val.items():
                vals.append(float(value))

        # Calculate Euclidean distances to freezed centroids   
        with open('ti_centroid.pkl', 'rb') as file:
            ti_centroid = pickle.load(file)


        assigned_clusters = []
        l = []  # list of distances

        for i, this_segment in enumerate(ti_centroid):
            dist = distance.euclidean(vals, this_segment)
            l.append(dist)
            index_min = np.argmin(l)
            assigned_clusters.append(index_min)

        return render_template(
            'predict2.html', result_value2=f' {index_min}'
            )

@app.route('/predict3', methods=['POST', 'GET'])
def predict3():
    if request.method == 'GET':
        return 'The URL /predict is accessed directly. Go to the main page firstly'

    if request.method == 'POST':
        input_val = request.form

        if input_val != None:
            # collecting values
            vals = []
            for key, value in input_val.items():
                vals.append(float(value))

        # Calculate Euclidean distances to freezed centroids   
        with open('vokasi_centroid.pkl', 'rb') as file:
            vokasi_centroid = pickle.load(file)


        assigned_clusters = []
        l = []  # list of distances

        for i, this_segment in enumerate(vokasi_centroid):
            dist = distance.euclidean(vals, this_segment)
            l.append(dist)
            index_min = np.argmin(l)
            assigned_clusters.append(index_min)

        return render_template(
            'predict3.html', result_value3=f' {index_min}'
            )

if __name__ == '__main__':
    app.run(debug=True)

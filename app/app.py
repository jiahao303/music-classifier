import os 
from flask import Flask, current_app, g, render_template, redirect, request, flash, url_for
import pickle



import pandas as pd
import json


app = Flask(__name__)

import tensorflow as tf 
from tensorflow import keras
import numpy as np 

# from tensorflow.keras.models import load_model 
# from tensorflow.keras.backend import set_session
# from skimage.transform import resize 


@app.route("/")
def main():
    return render_template('base.html')
# def main_page():
#     if request.method == 'POST':
#         file = request.files['file']
#         filename = secure_filename(file.filename)
#         file.save(os.path.join('uploads', filename))
#         return redirect(url_for('prediction', filename=filename))
#     return render_template('base.html')


# def hello():
    # return render_template("hello.html")

@app.route("/submit/", methods = ["POST", "GET"])
def submit():
    if request.method == "GET":
        return render_template("submit.html")
    else:
        try:
            lyrics = request.form["lyrics"]

            size_vocabulary = 2000

            vectorize_layer = TextVectorization(
                standardize=standardization,
                max_tokens= size_vocabulary, # only consider this many words
                output_mode='int',
                output_sequence_length=500) 

            vectorize_layer.adapt(train.map(lambda x, y: x["lyrics"]))

            scalars_input = keras.Input(
                shape = (len(scalars),), 
                name = "scalars",
                dtype = "float64"
            )
            lyrics_input = keras.Input(
                shape = (1,), 
                name = "lyrics",
                dtype = "string"
            )

            lyrics_features = vectorize_layer(lyrics_input)
            lyrics_features = keras.layers.Embedding(size_vocabulary, 7, name = "embedding")(lyrics_features)
            lyrics_features = keras.layers.Dropout(0.2)(lyrics_features)
            lyrics_features = keras.layers.GlobalAveragePooling1D()(lyrics_features)
            lyrics_features = keras.layers.Dropout(0.2)(lyrics_features)
            lyrics_features = keras.layers.Dense(64, activation='relu')(lyrics_features)

            scalar_features = keras.layers.Dense(64, activation='relu')(scalars_input)
            main = keras.layers.concatenate([lyrics_features, scalar_features], axis = 1)
            main = keras.layers.Dense(256, activation='relu')(main)
            main = keras.layers.Dense(64, activation='relu')(main)
            main = keras.layers.Dense(32, activation='relu')(main)
            output = keras.layers.Dense(num_genres, name = "genre", activation = 'softmax')(main)

            model = keras.Model(
                inputs = [lyrics_input, scalars_input],
                outputs = output)

            model.compile(optimizer = "adam",
                loss = losses.SparseCategoricalCrossentropy(from_logits=False),
                metrics=['accuracy'])


   
            model.load_weights("mnist-model/fake_model")

            prediction = model.predict(lyrics)[0]

            return render_template("submit.html", prediction = prediction)
        except:
            return render_template("submit.html", error = True)

# @app.route('/prediction/<filename>') 

# def prediction(filename):
#     #Step 1
    
#     with graph.as_default():
#       set_session(sess)
#       probabilities = model.predict(lyrics)[0,:]
#       print(probabilities)
#       #Step 4
#       number_to_class = ['blues', 'country', 'hip hop', 'jazz', 'pop', 'reggae', 'rock']
#       index = np.argsort(probabilities)
#       predictions = {
#         "class1":number_to_class[index[6]],
#         "class2":number_to_class[index[5]],
#         "class3":number_to_class[index[4]],
#         "prob1":probabilities[index[6]],
#         "prob2":probabilities[index[5]],
#         "prob3":probabilities[index[4]],
#       }
#     #Step 5
#     return render_template('predict.html', predictions=predictions)

# app.run(host='0.0.0.0', port=80)
# @app.route('/predict',methods=['POST'])
# def predict():
#     #For rendering results on HTML GUI
#     int_features = [float(x) for x in request.form.values()]
#     final_features = [np.array(int_features)]
#     prediction = model.predict(final_features)
#     output = round(prediction[0], 2) 
#     return render_template('index.html', prediction_text='The Predicted result is :{}'.format(output))

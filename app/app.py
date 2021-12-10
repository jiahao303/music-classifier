import os 
from flask import Flask, current_app, g, render_template, redirect, request, flash, url_for
import pickle
import sys
print(sys.path)


import pandas as pd
import json
import spotipy
import spotipy.oauth2
import requests

import numpy as np

import re
import string

app = Flask(__name__)

import tensorflow as tf
import numpy as np 
from tensorflow import keras 


import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')


@app.route("/")
def main():
    return render_template('base.html')



# def hello():
    # return render_template("hello.html")
def get_track_features(track_id):
    """
    Access the input of a song's Spotify ID,
    output the features in a dataframe
    """
    # use Client ID and Client Secret for Spotify Developer
    CLIENT_ID = "8e256a7b32f845ec9aebf81ae0feadb4"
    CLIENT_SECRET = '928d1a35600041eea6c69f97205fac6c'
    
    AUTH_URL = 'https://accounts.spotify.com/api/token'

    # POST
    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })

    # convert the response to JSON
    auth_response_data = auth_response.json()

    # save the access token
    access_token = auth_response_data['access_token']
    
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    
    # base URL of all Spotify API endpoints
    BASE_URL = 'https://api.spotify.com/v1/'

    # Track ID from the URI
    track_id = track_id

    # actual GET request with proper header
    r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
    r = r.json()
    
    # r is a dictionary with our desired feature and values
    # transform the dictionary into a dataframe
    # drop the unnecessary columns
    features = pd.DataFrame(r,index = [0])
    features = features.drop(["uri","track_href","analysis_url","type","id","key","mode","speechiness","tempo","duration_ms","time_signature","liveness"],axis = 1)
    print(features.columns)
    
    return features.astype(np.float32)

@tf.keras.utils.register_keras_serializable()
def custom_standardization(input_data):
  lowercase = tf.strings.lower(input_data)
  stripped_html = tf.strings.regex_replace(lowercase, '<br />', ' ')
  return tf.strings.regex_replace(stripped_html,
                                  '[%s]' % re.escape(string.punctuation),
                                  '')

@app.route("/submit/", methods = ["POST", "GET"])
def submit():
    if request.method == "GET":
        return render_template("submit.html")
    else:
        try:
            output = get_track_features(request.form['song'])
            lyrics = request.form["lyrics"]           

            
            dictionary = {'lyrics':[lyrics]}
            lyrics = lyrics.lower()
            
            lyrics = re.sub(r'[^\w\s]', "", lyrics)
            stop_words = set(stopwords.words("english"))
            lyrics = lyrics.split()
            lyrics = " ".join([w for w in lyrics if w not in stop_words])
            lyrics = pd.DataFrame(dictionary,index=[0])

            lyrics = tf.constant(lyrics)
            lyrics = lyrics[None,:]
            output = tf.constant(output, 'float64')
            output = output[None,:]

            test = tf.data.Dataset.from_tensor_slices(
                {
                    "lyrics" : lyrics, 
                    "scalars" : output
                }
            )

            print(len(test), test)

            # with keras.utils.CustomObjectScope({'custom_standardization':custom_standardization}):
            model = tf.keras.models.load_model("/Users/yiningliang/Desktop/PIC16B-Gitthub/music-classifier/app/mnist-model/fake_model4")
            genre = {0 : "blues", 1 : "country", 2 : "hip hop", 3: "jazz", 4: "pop", 5: "reggae", 6: "rock"}
            prediction = np.argmax(model.predict(test))


            return render_template("submit.html", prediction = genre[prediction])
        except Exception as e:
            print(e)
            return render_template("submit.html", error = True)



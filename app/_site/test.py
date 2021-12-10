import os 
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

import tensorflow as tf
import numpy as np 
# from tensorflow.keras.backend import set_session
# from skimage.transform import resize 



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


output = get_track_features("7qiZfU4dY1lWllzX7mPBI3?si=058bcde867c24a5e")
lyrics = "The club isn't the best place to find a lover So the bar is where I go Me and my friends at the table doing shots Drinking fast and then we talk slow And you come over and start up a conversation with just me And trust me I'll give it a chance now Take my hand, stop, put Van the Man on the jukebox And then we start to dance, and now I'm singing like Girl, you know I want your love Your love was handmade for somebody like me Come on now, follow my lead I may be crazy, don't mind me Say, boy, let's not talk too much Grab on my waist and put that body on me Come on now, follow my lead Come, come on now, follow my lead I'm in love with the shape of you We push and pull like a magnet do Although my heart is falling too I'm in love with your body And last night you were in my room And now my bedsheets smell like you Every day discovering something brand new I'm in love with your body Oh-I-oh-I-oh-I-oh-I I'm in love with your body Oh-I-oh-I-oh-I-oh-I I'm in love with your body Oh-I-oh-I-oh-I-oh-I I'm in love with y"
dictionary = {'lyrics':[lyrics]}
lyrics = pd.DataFrame(dictionary,index=[0])

print("hi")

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
print("hi3")
prediction = model.predict(test)
print("hi4")
    #def result():


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
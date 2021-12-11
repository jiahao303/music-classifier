# What Genre is Your Song? 


Thank you for using our music classifier! The Jupyter notebook detailing the model and dataset is in the file Music_Classifier_FINAL.ipynb, and our web app lives in the `app` folder. To run the web app, navigate to the app folder and run `flask run`.

Make sure to change the path of the model(in line 128) to the correct path on your local computer. 

From there, you can view our web app. Here is a screenshot of how our webapp looks.
![applook1.png](/images/applook1.png)

After clicking on *Input song lyrics and Song ID*, you will see the section for you to input lyrics and the song ID (where it says "Your song:").
![applook2.png](/images/applook2.png)


Input your song's lyrics in plain text where indicated. Be careful to copy your lyrics as plain text! Sites like genius.com may have annotations for the lyrics, which are copied along with the lyrics. Make sure to avoid these sites!

Navigate to your song's Spotify page and copy the song's ID. Below is a screenshot showing where a song's ID is.

![Spotify song ID](/images/spotify_id.png)

Input this ID where indicated. Then predict the song and see what genre our model predicts!

# Limitations

We haven't run into any limitations with our web app as of yet—it should be able to interact with a song with lyrics of any length and with any song on Spotify.

For our model, we have three limitations: our dataset, songs that are in other languages, and songs that don't have lyrics.

Our dataset was found on the internet, and while it did have relatively equal distributions between genre classes, it tended to predict hip-hop songs correctly more often than songs from other genres. More research is needed to see why this happens; we hypothesize that perhaps the lyrics of hip-hop songs are more distinct or that our dataset's selection of songs is skewed.

We also don't consider songs in other languages, as well as NLP models in other languages. Finally, there are songs that don't have lyrics; we don't consider using soundwave data to classify these songs.
---
layout: post
title: "Music Classifier Project by Group Spec-Taco-Lar"
authors: Jiahao Huang, Stella Wang, Tiana Liang
date: 2021-10-14 19:00:00
---

*tic-tac-toe game for a try*
```python
..O
.X.
..O
```

*This proposal aims to guide our group throughout the project, ensuring everything to be on the right track.*

## Abstract

The project aims to classify the genre and sentiments present in a song based off of the song’s lyrics and (potentially) its soundwave composition. A problem I’ve faced when downloading music into my phone is the lack of automatic genre detection; the manual inputting of a song’s genre can get tiring, especially when a lot of songs are downloaded. We hope to choose and train a supervised learning classification model to solve our problem and classify a song’s genre/sentiments from its metadata. Additionally, we hope to employ natural language processing techniques to process our lyrical text data and transform it. 

## Planned Deliverables

We are aiming to create a webapp finally to classify the genre and identify the sentiments of a song. The webapp will be able to classify the genre and sentiments of a song by reviewing the lyrics. A classification model would be trained by us and implemented to the webapp.

If we achieve full success, the webapp will have a nice interface for the users to input the lyrics of the songs to be analyzed, and through our trained model, the webapp will classify the genre and analyze the sentiments. If we achieve partial success, the model would be generated and there would be a blog post and code repository detailing our machine learning pipeline, which would offer hints and support for further improvement of the model and the development of the webapp. 

The interface would be a form based one. To be specific, the interface would include a text area for the users to input the lyrics. Furthermore, the output would present the genre and sentiment identification result analyzed from the lyrics.

## Resources Required

We require a dataset of song metadata with lyrics, genre, sentiments present throughout the song, and potentially other data, such as artist, time period, producer, and label. A potential data source is linked here: https://data.mendeley.com/datasets/3t9vbwxgr5/2. Should online data sources not fit our need, we plan to web scrape websites with lyrics, such as genius.com. If web scraping these websites require an API, we plan to use one. We do not plan to spend any money on the data acquisition process. Once our data is gathered, we plan to perform data analysis and train our model on our local computers; if higher computing power is necessary, then we will look into computing resources available to UCLA students.

## Tools and Skills Required

Machine learning is the fundamental tool for our project since our classification of genre and sentiments bases on the training datasets. Also, as our potential dataset consists of different additional information such as time period, artist, producer, etc., we need to manage the database before proceeding with the data analysis. Our final webapp also requires interactive graphics and graphical user interface that allows users to input songs, so we need skills in web development. We would like to utilize Python packages such as Django and Tkinter. Libraries that we have learned in class, for example, Pandas, Numpy, Sklearn, and Matplotlib are also expected for filtering the data and generating plots.

## What You Will Learn

By completing this project, we could learn deeper about machine learning, which allows us to utilize software packages such as sklearn and panda more skillfully. This project requires a vast utilization of data manipulation and model building, which are important skills in many fields. Moreover, by planning the project schedule and collaborating with team members on github, all of us could learn the project management principles better. Group working skills could be learned throughout the whole process. 

## Risks

One risk is that we possibly could not find soundwaves data of songs or we do not have enough computational power to analyze soundwaves and therefore couldn’t incorporate such a factor to our genre classification. The other risk is that some songs that we adopt as the dataset may be subject to copyright issues.

## Ethics

As our model trains on English songs, the machine learning algorithm will be biased towards English songs, and song lyrics in other languages will have to become translated to be inputted in our model. Our model will be biased towards emotions, certain words, and other song metadata only applicable to English songs. Since all three of our group members are Chinese, we are also interested in natural language processing for Chinese song lyrics, as well as lyrics in other languages. This may be something we explore after creating our model for English songs. Additionally, songs without lyrics are not considered, even if they have plenty of emotional content. Cultures that produce songs without lyrics could feel alienated as well. 

People with access to a computer, people who are not deaf, and people who are familiar with English songs will be able to use our product. While not being directly harmed, people who do not speak English could potentially feel alienated by our product. Additionally, record companies may have issues with our product should the songs be copyrighted. The world will be, overall, better as people will have access to a product that provides convenience.

## Tentative Schedule
1. After two weeks, we hope to have a cleaned dataset ready for our model, as well as have learned the basics of natural language processing. 
2. After four weeks, we hope to have chosen a classification model and have a minimum viable product. 
3. After six weeks, we hope to have fine tuned our model and have created a webapp, as well as explore songs in other languages.



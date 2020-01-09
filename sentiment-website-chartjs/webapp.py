#!/usr/bin/env python

import requests
import flask
import pandas as pd
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
app.config['SECRET_KEY'] = '3141592653589793238462643383279502884197169399'

# data
purpose = pd.read_excel('data/purpose.xlsx')
emotion = pd.read_excel('data/emotion_count.xlsx')
positive = pd.read_excel('data/positive_count.xlsx')
negative = pd.read_excel('data/negative_count.xlsx')
sentiment = pd.read_excel('data/sentiment_count.xlsx')

emotion_post = pd.read_excel('data/emotion_post.xlsx')
positive_post = pd.read_excel('data/positive_post.xlsx', header=None)
negative_post = pd.read_excel('data/negative_post.xlsx', header=None)

# =========================================== WEB ================================================================

@app.route('/', methods=['GET', 'POST'])
def home():
    if "sentiment" in request.form:
        return render_template('sentiment.html')
    elif "emotion" in request.form:
        return render_template('emotion.html')
    return render_template('index.html')

# @app.route('/purpose', methods=['GET', 'POST'])
# def purpose():
#     return render_template('purpose.html')

@app.route("/sentiment")
def sentiment_route():
    sentiment_labels = sentiment['Sentiment']
    sentiment_values = sentiment['Count']
    
    positive_labels = positive['Emotion']
    positive_values = positive['Count']

    negative_labels = negative['Emotion']
    negative_values = negative['Count']

    return render_template('sentiment.html',
        sentiment_values=sentiment_values, sentiment_labels=sentiment_labels,
        positive_labels = positive_labels, positive_values = positive_values,
        negative_labels = negative_labels, negative_values = negative_values,
        positive_posts = positive_post.iloc[:,0],
        negative_posts = negative_post.iloc[:,0])



@app.route("/emotion")
def emotion_route():
    labels = emotion['Emotion']
    values = emotion['Count']
    return render_template('emotion.html', values=values, labels=labels,
        # posts = emotion_post)
        posts = emotion_post['Post'], emotions = emotion_post['Emotion'])

@app.route("/purpose")
def purpose_route():
    labels = purpose['Purpose']
    values = purpose['Count']
    return render_template('purpose.html', values=values, labels=labels)

if __name__ == '__main__':
   app.run(debug=True, host='127.0.0.1', port=5000)
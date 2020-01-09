#!/usr/bin/env python

import os
import flask
import pandas as pd
from flask import Flask, render_template, redirect, url_for, request, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = '3141592653589793238462643383279502884197169399'

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
purpose = pd.read_excel(os.path.join(THIS_FOLDER, 'data/purpose.xlsx'))
emotion = pd.read_excel(os.path.join(THIS_FOLDER, 'data/emotion_count.xlsx'))
positive = pd.read_excel(os.path.join(THIS_FOLDER, 'data/positive_count.xlsx'))
negative = pd.read_excel(os.path.join(THIS_FOLDER, 'data/negative_count.xlsx'))
sentiment = pd.read_excel(os.path.join(THIS_FOLDER, 'data/sentiment_count.xlsx'))

emotion_post = pd.read_excel(os.path.join(THIS_FOLDER, 'data/emotion_post.xlsx'))
positive_post = pd.read_excel(os.path.join(THIS_FOLDER, 'data/positive_post.xlsx'), header=None)
negative_post = pd.read_excel(os.path.join(THIS_FOLDER, 'data/negative_post.xlsx'), header=None)


# =========================================== WEB ================================================================

@app.route('/', methods=['GET', 'POST'])
def home():
    # if "sentiment" in request.form:
    #     return render_template('sentiment.html')
    # elif "emotion" in request.form:
    #     return render_template('emotion.html')
    return render_template('index.html')

@app.route("/sentiment")
def sentiment_route():
    # positive = pd.read_excel(os.path.join(THIS_FOLDER, 'data/positive_count.xlsx'))
    # negative = pd.read_excel(os.path.join(THIS_FOLDER, 'data/negative_count.xlsx'))
    # sentiment = pd.read_excel(os.path.join(THIS_FOLDER, 'data/sentiment_count.xlsx'))

    # positive_post = pd.read_excel(os.path.join(THIS_FOLDER, 'data/positive_post.xlsx'), header=None)
    # negative_post = pd.read_excel(os.path.join(THIS_FOLDER, 'data/negative_post.xlsx'), header=None)

    sentiment_labels = sentiment['Sentiment']
    sentiment_values = sentiment['Count']
    sentiment_class = sentiment_labels.str.lower()

    Sum = sum(sentiment_values)
    sentiment_labels = [sentiment_labels[i] + " " + str(int(sentiment_values[i] / Sum * 100)) + '%' for i in range(len(sentiment_values))]
    
    positive_labels = positive['Emotion']
    positive_values = positive['Count']

    negative_labels = negative['Emotion']
    negative_values = negative['Count']

    return render_template('sentiment.html',
        sentiment_values = sentiment_values, sentiment_labels = sentiment_labels,
        sentiment_class = sentiment_class,
        positive_labels = positive_labels, positive_values = positive_values,
        negative_labels = negative_labels, negative_values = negative_values,
        positive_posts = positive_post.iloc[:,0],
        negative_posts = negative_post.iloc[:,0])



@app.route("/emotion")
def emotion_route():
    # emotion = pd.read_excel(os.path.join(THIS_FOLDER, 'data/emotion_count.xlsx'))
    # emotion_post = pd.read_excel(os.path.join(THIS_FOLDER, 'data/emotion_post.xlsx'))

    labels = emotion['Emotion']
    values = emotion['Count']
    color_code = []
    for i in labels:
        if i in ["Anticipation", "Trust", "Joy"]:
            color_code.append("positive")
        else:
            color_code.append("negative")

    return render_template('emotion.html', values=values, labels=labels,
        # posts = emotion_post)
        posts = emotion_post['Post'], emotions = emotion_post['Emotion'],
        color_code = color_code)

@app.route("/purpose")
def purpose_route():
    # purpose = pd.read_excel(os.path.join(THIS_FOLDER, 'data/purpose.xlsx'))

    labels = purpose['Purpose']
    values = purpose['Count']
    return render_template('purpose.html', values=values, labels=labels)

if __name__ == '__main__':
    # global purpose
    # global emotion
    # global positive
    # global negative
    # global sentiment
    # global emotion_post
    # global positive_post
    # global negative_post

    # purpose = pd.read_excel(os.path.join(THIS_FOLDER, 'data/purpose.xlsx'))
    # emotion = pd.read_excel(os.path.join(THIS_FOLDER, 'data/emotion_count.xlsx'))
    # positive = pd.read_excel(os.path.join(THIS_FOLDER, 'data/positive_count.xlsx'))
    # negative = pd.read_excel(os.path.join(THIS_FOLDER, 'data/negative_count.xlsx'))
    # sentiment = pd.read_excel(os.path.join(THIS_FOLDER, 'data/sentiment_count.xlsx'))
    # emotion_post = pd.read_excel(os.path.join(THIS_FOLDER, 'data/emotion_post.xlsx'))
    # positive_post = pd.read_excel(os.path.join(THIS_FOLDER, 'data/positive_post.xlsx'), header=None)
    # negative_post = pd.read_excel(os.path.join(THIS_FOLDER, 'data/negative_post.xlsx'), header=None)

    # purpose = pd.read_excel(dirpath + 'data/purpose.xlsx')
    # emotion = pd.read_excel(dirpath + 'data/emotion_count.xlsx')
    # positive = pd.read_excel(dirpath + 'data/positive_count.xlsx')
    # negative = pd.read_excel(dirpath + 'data/negative_count.xlsx')
    # sentiment = pd.read_excel(dirpath + 'data/sentiment_count.xlsx')
    # emotion_post = pd.read_excel(dirpath + 'data/emotion_post.xlsx')
    # positive_post = pd.read_excel(dirpath + 'data/positive_post.xlsx', header=None)
    # negative_post = pd.read_excel(dirpath + 'data/negative_post.xlsx', header=None)
    app.run()
   # app.run(debug=True, host='127.0.0.1', port=5000)
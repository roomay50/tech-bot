import json
import random

from keras.models import load_model
import nltk
from nltk.stem import WordNetLemmatizer
import numpy as np
import pickle

intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))

model = load_model('tech_bot_model.py.h5')

lemmatizer = WordNetLemmatizer()


def sentence_clean_up(sentence):
    words_in_sentence = nltk.word_tokenize(sentence)
    words_in_sentence = [lemmatizer.lemmatize(word.lower()) for word in words_in_sentence]
    return words_in_sentence


# func that returns bag of words as arrya of 0 and 1 for each word in the bag that exists in the sentence

def bag_of_words(sentence, words, show_details=True):
    # tokenize the pattern
    words_in_sentence = sentence_clean_up(sentence)
    # bag of words
    bag = [0] * len(words)
    for wis in words_in_sentence:
        for i, w in enumerate(words):
            if w == wis:
                # assign 1 if the current word is in the vocab position
                bag[i] = 1
                if show_details:
                    print("found in bag: %wis" % w)
    return np.array(bag)


def predict_class(sentence, model):
    # filter out predictions below a specific threshold
    prediction = bag_of_words(sentence, words, show_details=False)
    response = model.predict(np.array([prediction]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(response) if r > ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


def get_response(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result


def techbot_response(msg):
    ints = predict_class(msg, model)
    response = get_response(ints, intents)
    return response


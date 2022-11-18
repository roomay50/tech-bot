import nltk
from nltk.stem import WordNetLemmatizer
import json
import pickle
import numpy as np
import random

# downloading nltk packages
nltk.download('punkt')
nltk.download('wordnet')
# nltk.download('omw-1.4')

# creating a lemmatizer object
lemmatizer = WordNetLemmatizer()

# initialize chatbot training
words = []
classes = []
documents = []
ignore_words = ['?', '!']
data_file = open('intents.json').read()
intents = json.loads(data_file)

for intent in intents['intents']:
    for pattern in intent['patterns']:

        # tokenize each word and adding it to the word list
        tokenized_word = nltk.word_tokenize(pattern)
        words.extend(tokenized_word)

        # adding to our document list each pair of patterns and their tags
        documents.append((tokenized_word, intent['tag']))

        # adding tags to our class list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

#lemmatizing the words list, amd putting it in lower case
words = [lemmatizer.lemmatize((tokenized_word.lower()))
         for tokenized_word in words if tokenized_word not in ignore_words]

# sort our lists and print them
words = sorted(list(set(words)))

classes = sorted(list(set(classes)))

print(len(documents), "documents")

print(len(classes), "classes", classes)

print(len(words), "unique lemmatized words", words)

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

# building th e deep learning model
# initializing training data

training = []
output_empty = [0] * len(classes)
for doc in documents:
    # initializing bag of words
    bag = []
    # list of tokenized worsd for the pattern
    pattern_words = doc[0]
    # lemmatize each word
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    # create our bag of words with array of 1
    for word in words:
        bag.append(1) if word in pattern_words else bag.append(0)

    # output = 0 for each tag. output = 1 for current tag. for each pattern
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

    # shuflfe and turn features into np array
random.shuffle(training)
training = np.array(training, dtype=list)

# create test and train list. X = patterns, y= intents
X = list(training[:, 0])
y = list(training[:, 1])

print("created training set")

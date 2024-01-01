import string
import pickle
import pandas as pd
import numpy as np
import tensorflow as tf







stop_words = {
    'a', 'about', 'above', 'after', 'again', 'against', 'ain', 'all', 'am', 'an', 'and', 'any', 'are', 'aren',
    "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by',
    'can', 'couldn', "couldn't", 'd', 'did', 'didn', "didn't", 'do', 'does', 'doesn', "doesn't", 'doing', 'don',
    "don't", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', 'hadn', "hadn't", 'has', 'hasn',
    "hasn't", 'have', 'haven', "haven't", 'having', 'he', 'her', 'here', 'hers', 'herself', 'him', 'himself',
    'his', 'how', 'i', 'if', 'in', 'into', 'is', 'isn', "isn't", 'it', "it's", 'its', 'itself', 'just', 'll', 'm',
    'ma', 'me', 'mightn', "mightn't", 'more', 'most', 'mustn', "mustn't", 'my', 'myself', 'needn', "needn't", 'no',
    'nor', 'not', 'now', 'o', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out',
    'over', 'own', 're', 's', 'same', 'shan', "shan't", 'she', "she's", 'should', "should've", 'shouldn', "shouldn't",
    'so', 'some', 'such', 't', 'than', 'that', "that'll", 'the', 'their', 'theirs', 'them', 'themselves', 'then',
    'there', 'these', 'they', 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 've', 'very', 'was',
    'wasn', "wasn't", 'we', 'were', 'weren', "weren't", 'what', 'when', 'where', 'which', 'while', 'who', 'whom',
    'why', 'will', 'with', 'won', "won't", 'wouldn', "wouldn't", 'y', 'you', "you'd", "you'll", "you're", "you've",
    'your', 'yours', 'yourself', 'yourselves'
}


# Custom Standardization

@tf.keras.utils.register_keras_serializable()
def custom_standardization(input_string):
    # Convert to lowercase
    no_uppercased = tf.strings.lower(input_string, encoding='utf-8')

    # Replace '*' characters with a space
    no_stars = tf.strings.regex_replace(no_uppercased, "\*", " ")

    # Remove the phrase "devamını oku"
    no_repeats = tf.strings.regex_replace(no_stars, "devamını oku", "")

    # Replace the HTML line-break tag "<br />" with a space
    no_html = tf.strings.regex_replace(no_repeats, "<br />", "")

    # Remove digits
    no_digits = tf.strings.regex_replace(no_html, "\w*\d\w*", "")

    # Replace punctuation characters with spaces
    no_punctuations = tf.strings.regex_replace(no_digits, f"([{string.punctuation}])", r" ")

    # Remove stop words
    no_stop_words = ' ' + no_punctuations + ' '
    for each in stop_words:
        no_stop_words = tf.strings.regex_replace(no_stop_words, ' ' + each + ' ', r" ")

    # Remove extra spaces
    no_extra_space = tf.strings.regex_replace(no_stop_words, " +", " ")

    # Replace Turkish characters with their corresponding Latin characters
    no_I = tf.strings.regex_replace(no_extra_space, "ı", "i")
    no_O = tf.strings.regex_replace(no_I, "ö", "o")
    no_C = tf.strings.regex_replace(no_O, "ç", "c")
    no_S = tf.strings.regex_replace(no_C, "ş", "s")
    no_G = tf.strings.regex_replace(no_S, "ğ", "g")
    no_U = tf.strings.regex_replace(no_G, "ü", "u")

    return no_U

path="app/id_to_target (2).pkl"
loaded_end_to_end_model = tf.keras.models.load_model("app/model_FNN")
pkl_file = open(path,"rb")
id_to_target= pickle.load(pkl_file)

def classify (text):
  pred=loaded_end_to_end_model.predict([text])
  return id_to_target[np.argmax(pred)]
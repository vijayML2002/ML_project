import tensorflow as tf
import unicodedata
import os
import re


def get_raw_data(path):
    english_sentence = []
    spanish_sentence = []
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read()
    data = data.strip().split("\n")
    for sentence in data:
        words = sentence.split("\t")
        english_sentence.append(words[0])
        spanish_sentence.append(words[1])

    return spanish_sentence, english_sentence

def clean_text(text):
    text = text.lower().strip()
    text = unicodedata.normalize('NFD', text)
    text = ''.join([ch for ch in text if unicodedata.category(ch) != 'Mn'])
    text = re.sub('([?.!,¿])', r' \1 ', text)
    text = re.sub('[" "]+', ' ', text)
    text = re.sub('[^a-zA-Z?.!,¿]+', ' ', text)
    text = text.strip()
    return text

def add_token(text):
    start_token = "<start>"
    end_token = "<end>"
    text = "{} {} {}".format(start_token, text, end_token)
    return text

def tokenizer(data, num):
    unknown_str = "<ukn>"
    mapper = tf.keras.preprocessing.text.Tokenizer(num_words=num, filters="", oov_token=unknown_str)
    mapper.fit_on_texts(data)
    data = tokenizer.texts_to_sequences(data)
    data = tf.keras.preprocessing.sequence.pad_sequences(data, padding='post')
    return data, mapper
    
def prepare_text(text1, text2):
    ctext1 = []
    ctext2 = []

    for sentence in text1:
        clean_sentence = clean_text(sentence)
        se_token = add_token(clean_sentence)
        ctext1.append(se_token)
        
    for sentence in text2:
        clean_sentence = clean_text(sentence)
        se_token = add_token(clean_sentence)
        ctext2.append(se_token)
    
    return ctext1, ctext2







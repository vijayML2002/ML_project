import os
import unicodedata
import re

path = "./spa.txt"

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

def tokenizer():
    pass

sp, en = get_raw_data(path)



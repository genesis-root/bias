import sys

import textblob
from textblob import TextBlob


def tokenize(text_file):
    text = text_file.read()
    return text.split()


def bias(text_file):
    bias = 0
    tokenized = tokenize(text_file)
    red_flags = ["alien", 'evil', 'monster', 'good', 'aliens']
    for w in range(len(tokenized)):
        word = TextBlob(tokenized[w])
        if word.sentiment.polarity < -.5:
            bias = bias + .5
        if word.sentiment.polarity > .5:
            bias = bias + .5
        if word.sentiment.polarity > -.5 and word.sentiment.polarity < 0:
            bias = bias + .25
        if word.sentiment.polarity < .5 and word.sentiment.polarity > 0:
            bias = bias + .25
        if word.sentiment.polarity > .5:
            bias = bias + 1
        if word.sentiment.polarity < -.5:
            bias = bias + 1
        if word.lower() in red_flags:
            bias = bias + 2
            print(word)
    return (bias / len(tokenized)) * 100

if __name__ == "__main__":
    with open(sys.argv[1], encoding='utf-8', errors='ignore') as infile:
        bias_data = bias(infile)
        print(bias_data)

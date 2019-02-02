import textblob
from textblob import TextBlob

def tokenized(text_file):
    with open(text_file, encoding='utf8', errors='ignore') as f:
        text = f.read()
        return text.split()

def bias(text_file):
    bias = 0
    list = tokenized(text_file)
    for w in range(len(list)):
        word = TextBlob(list[w])
        if word.sentiment.polarity < 0:
            bias = bias + 1
        if word.sentiment.polarity > 0:
            bias = bias + 1
    return (bias/len(tokenized(text_file))) * 100


economist = bias("out.txt")
breitbart = bias("economist.txt")
print(economist)
print(breitbart)


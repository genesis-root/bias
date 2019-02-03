import textblob
from textblob import TextBlob


def tokenized(text_file):
    with open(text_file, encoding='utf8', errors='ignore') as f:
        text = f.read()
        return text.split()


def bias(text_file):
    bias = 0
    list = tokenized(text_file)
    print(text_file)
    red_flags = ["alien", 'evil', 'monster', 'good', 'aliens']
    for w in range(len(list)):
        word = TextBlob(list[w])
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
    return (bias / len(tokenized(text_file))) * 100

breitbart = bias("breitbart.txt")
economist = bias("economist.txt")
bbc = bias("bbc.txt")

print('Breitbart News:')
print(breitbart)
print('The Economist:')
print(economist)
print('BBC:')
print(bbc)

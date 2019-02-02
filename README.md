# bias
bias.py tokenizes a text file, then gives a sentiment polarity score (-1:1) to every word in the document. If any word has a score above or below 0, the variable **bias** = **bias + 1**. Once the for loop completes, I divide bias.py by the total number of words in the document. The returned output represents the percentage of biased language, based on the python **textblob** package. 

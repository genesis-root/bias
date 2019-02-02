# bias
bias.py tokenizes a text file, then gives a sentiment polarity score (-1:1) to every word in the document. If any word has a score above or below 0, the variable **bias** = **bias + 1**. Once the for loop completes, bias.py divides **bias** by the total number of words in the document. The returned output represents the percentage of biased language in said *.txt, based on the python **textblob** package. 

https://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis

# Directions
1.  Install the **textblob** package with **pip install textblob**.
2.  When you call the function **bias()** be sure to change 'economist.txt' to 'whatevertextfile.txt' you want to use. And make sure this txt file is in the same folder as bias.py
3. Run it!

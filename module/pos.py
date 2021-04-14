# Part-of-Speech Tagging
import nltk
from nltk import word_tokenize
text = word_tokenize("I enjoy biking on the trails")
output = nltk.pos_tag(text)
print(output)
# [('I', 'PRP'), ('enjoy', 'VBP'), ('biking', 'VBG'), ('on', 'IN'), ('the', 'DT'), ('trails', 'NNS')]

# Natural language generation is a growing field in NLP that entails writing code in such a way that it will generate new text

# When we're building datasets for NLP, we need to consider how our program will interact with the text document we provide. If we create a bag-of-words (BoW) model

# In NLP, there is an n-gram method, which is a sequence of items from a given text.

# N-grams can be used for a variety of NLP tasks, but most involve text mining or extraction. 

##
## NLP Analyses
##

# Syntactic analysis is essentially checking the dictionary definition
# Sentiment analysis pertains to what the text means.
# Semantic analysis entails extracting the meaning of the text.

# 1 Raw Text: Start with the raw data.
# 2 Tokenization: Separate the words from paragraphs, to sentences, to individual words.
# 3 Stop Words Filtering: Remove common words like "a" and "the" that add no real value to what we are looking to analyze.
# 4 Term Frequency-Inverse Document Frequency (TF-IDF): Statistically rank the words by importance compared to the rest of the words in the text.
# 5 Machine Learning: Put everything together and run through the machine learning model to produce an output.


# named-entity recognition (NER) is the concept of taking a document and finding all of the important terms therein. By "important," we mean names of places and people, government organizations, and so forth. Many names are already recognized, but you can always add more names to the list of recognized entities, as necessary.
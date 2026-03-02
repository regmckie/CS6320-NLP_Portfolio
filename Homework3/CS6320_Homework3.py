# FILENAME: CS6320_Homework3.py
# DUE DATE: 10/8/2024
# AUTHOR:   Reg Gonzalez
# EMAIL:    rdg170330@utdallas.edu (school) or regmckie@gmail.com (personal)
# COURSE:   CS 6320.002, Fall 2024


# *************************************************************************
# * PART 1: Word2vec - the good                                           *
# * Provide working examples of vector "meaning" manipulation             *
# *************************************************************************

import gensim.downloader as api

print("PART 1: Word2vec - the good")

# Get a pre-trained Word2vec model
w2v_model = api.load('word2vec-google-news-300')

# Make sure that the vector model was successfully loaded
print("Word2vec model successfully loaded")

# Perform vector arithmetic. This'll "add" and "subtract" the terms
# from each other and then return the most similar word
# E.g., king - man + woman = queen
def calculate_most_similar_word(positive_terms, negative_terms, w2v_model):
    result = w2v_model.most_similar(positive=positive_terms, negative=negative_terms, topn=1)
    most_similar_word = result[0][0]
    return most_similar_word

# Example #1 - countries & continents
examples_country_continent = [
    (['France', 'Asia'], ['Europe']),
    (['Philippines', 'Africa'], ['Asia']),
    (['Egypt', 'Australia'], ['Africa']),
]

# Example #2 - countries & currencies
examples_country_currency = [
    (['USA', 'Yuan'], ['Dollar']),
    (['Mexico', 'Rupee'], ['Peso']),
    (['Japan', 'Pound'], ['Yen']),
]

# Do vector arithmetic on the different examples to see Word2vec's
# ability to manipulate "meaning" in vectors

print()
print("Example #1 - countries & continents")
for positive_terms, negative_terms in examples_country_continent:
    most_similar_word = calculate_most_similar_word(positive_terms, negative_terms, w2v_model)
    print(f"{positive_terms[0]} - {negative_terms[0]} + {positive_terms[1]} = {most_similar_word}")

print()
print("Example #2 - countries & currencies")
for positive_terms, negative_terms in examples_country_currency:
    most_similar_word = calculate_most_similar_word(positive_terms, negative_terms, w2v_model)
    print(f"{positive_terms[0]} - {negative_terms[0]} + {positive_terms[1]} = {most_similar_word}")


# *****************************************************************************
# * PART 2: Word2vec - the bad                                                *
# * Provide a non-working example of vector "meaning" manipulation            *
# *****************************************************************************

print()
print("******************************************************")
print("PART 2: Word2vec - the bad")

# Example - musicians & genres
examples_musician_genre = [
    (['Beethoven', 'pop'], ['classical']),
    (['Mozart', 'rock'], ['classical']),
    (['Bach', 'jazz'], ['classical']),
]

print()
print("Example - biases in politics")
for positive_terms, negative_terms in examples_musician_genre:
    most_similar_word = calculate_most_similar_word(positive_terms, negative_terms, w2v_model)
    print(f"{positive_terms[0]} - {negative_terms[0]} + {positive_terms[1]} = {most_similar_word}")


# ****************************************************
# * PART 3: Word2vec - the ugly                      *
# * Provide an example of bias in Word2vec           *
# ****************************************************

print()
print("******************************************************")
print("PART 3: Word2vec - the ugly")

# Example - bias in politics
examples_bias_in_politics = [
    (['scandal', 'Republican'], ['Democrat']),
    (['honest', 'Republican'], ['Democrat']),
    (['democracy', 'China'], ['USA']),
]

print()
print("Example - musicians & genres")
for positive_terms, negative_terms in examples_bias_in_politics:
    most_similar_word = calculate_most_similar_word(positive_terms, negative_terms, w2v_model)
    print(f"{positive_terms[0]} - {negative_terms[0]} + {positive_terms[1]} = {most_similar_word}")


# *************************************************************************
# * PART 4: Spacy                                                         *
# * Come up with your own sentence and do the following steps:            *
# * - Tokenization                                                        *
# * - POS tagging                                                         *
# * - Named entities                                                      *
# * - Dependency parsing                                                  *
# *************************************************************************

print()
print("******************************************************")
print("PART 4: spaCy")

import spacy

nlp = spacy.load("en_core_web_sm")

# Create and process the sentence
my_sentence = "I want to be best friends with a witch and clown named Agatha and Harley, respectively."
doc = nlp(my_sentence)

# Output the different steps

# I - Tokenization
print()
print("I - Tokenization:")
for t in doc:
    print(f"Token: {t.text}")

# II - POS Tagging
print()
print("II - POS Tagging:")
for t in doc:
    print(f"Token: {t.text}, POS: {t.pos_}, Tag: {t.tag_}")

# III - Named Entities
print()
print("III - Named Entities:")
for t in doc.ents:
    print(f"Named entity: {t.text}, NE Label: {t.label_}")

# IV - Dependency Parsing
print()
print("IV - Dependency Parsing:")
for t in doc:
    print(f"Token: {t.text}, Dependency: {t.dep_}")

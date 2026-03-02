# FILENAME: CS6320_Homework2.py
# DUE DATE: 9/10/2024
# AUTHOR:   Reg Gonzalez
# EMAIL:    rdg170330@utdallas.edu (school) or regmckie@gmail.com (personal)
# COURSE:   CS 6320.002, Fall 2024


# ************************************************
# * PART 1:                                      *
# * Use spaCy to tokenize the corpus             *
# ************************************************

import spacy

print("PART 1 - USE SPACY TO TOKENIZE THE CORPUS")

# Load the language model for Greek in order to process the corpus
greek_lm = spacy.load("el_core_news_sm")

greek_corpus = "Τρώω φρούτα κάθε μέρα Τρώω ψωμί με βούτυρο Τρώω ένα μήλο το πρωί Τρώω σαλάτα με ντομάτα Τρώω ζυμαρικά για μεσημεριανό Τρώω κοτόπουλο για δείπνο Τρώω αυγά το Σαββατοκύριακο Τρώω ρύζι με λαχανικά Τρώω γιαούρτι με μέλι Τρώω τυρί και ελιές Αγαπώ τα φρούτα, ειδικά τα μήλα Έχεις ψωμί Κάθε πρωί τρώω ένα μήλο Θέλω να φάω σαλάτα με ντομάτες Η σούπα έχει κοτόπουλο και λαχανικά Πόσο κοστίζει το ψωμί Πίνω γάλα με το μήλο μου Μετά το δείπνο, τρώμε συχνά φρούτα Στη σαλάτα, βάζω πάντα ντομάτες Ποιος έφαγε το ψωμί Το κοτόπουλο είναι το αγαπημένο μου φαγητό Μπορώ να έχω λίγο περισσότερο ψωμί, παρακαλώ Αυτή η μηλόπιτα είναι πολύ νόστιμη Πού αγόρασες αυτά τα φρέσκα φρούτα Φτιάχνω σαλάτα με ντομάτες και αγγούρια Θα πιείτε γάλα ή χυμό Τα παιδιά δεν τρώνε πολύ ψωμί Αυτές οι ντομάτες είναι πολύ ώριμες Στο πρωινό μου πάντα έχω ένα μήλο Τα φρούτα είναι καλά για την υγεία"

# Tokenize the Greek corpus and output the tokens
document = greek_lm(greek_corpus)
tokens = [t.text for t in document]
print("Tokens: ", tokens)
print()

# ********************************************
# * PART 2:                                  *
# * Count unigrams and bigrams               *
# ********************************************

print("PART 2 - COUNT UNIGRAMS AND BIGRAMS")

counts_of_unigrams = {}
counts_of_bigrams = {}

# Count unigrams in the tokenized corpus and print them out
for t in tokens:
    if t in counts_of_unigrams:
        counts_of_unigrams[t] = counts_of_unigrams[t] + 1
    else:
        counts_of_unigrams[t] = 1

print("Unigrams count: ", counts_of_unigrams)

# Count bigrams in the tokenized corpus and print them out
tokenized_text_size = len(tokens)

for counter in range(tokenized_text_size - 1):
    bigram = (tokens[counter], tokens[counter + 1])
    if bigram in counts_of_bigrams:
        counts_of_bigrams[bigram] = counts_of_bigrams[bigram] + 1
    else:
        counts_of_bigrams[bigram] = 1

print("Bigrams count: ", counts_of_bigrams)
print()


# ******************************************************************
# * PART 3:                                                        *
# * Calculate probabilities and perplexities of two sentences        *
# ******************************************************************

import math

print("PART 3 - CALCULATE PROBABILITIES AND PERPLEXITIES OF TWO SENTENCES")

# Compute the probability of the sample sentences
def compute_probability(sample_sentence, size_of_vocabulary, counts_of_unigrams, counts_of_bigrams):
    total_prob = 0  # Start probability off w/ 0
    tokens_of_sample_sent = sample_sentence.split()    # Tokenize the sample sentence
    length_of_tokens = len(tokens_of_sample_sent)

    for counter in range(length_of_tokens - 1):
        # Get unigram and bigram counts from the sample sentence
        word1, word2 = tokens_of_sample_sent[counter], tokens_of_sample_sent[counter + 1]
        count_of_unigram = counts_of_unigrams.get(word1, 0)
        count_of_bigram = counts_of_bigrams.get((word1, word2), 0)

        # Calculate the prob of bigrams using this formula:
        # P(w_n | w_{n-1}) = [C(w_{n-1} * w_n) + 1] / [C(w_{n-1}) + V)
        # Here, we're using log(p) and add-one smoothing when facing 0's
        bigram_probability = math.log((count_of_bigram + 1) / (count_of_unigram + size_of_vocabulary))

        # Finally, compute total prob by adding the log(p)'s of the bigram probabilities
        total_prob = total_prob + bigram_probability

    return total_prob

# Compute perplexity of the sample sentences
def compute_perplexity(sample_sentence, size_of_vocabulary, counts_of_unigrams, counts_of_bigrams):
    # Get the number of tokens from sample sentence
    # and the probability of the sample sentence
    sample_sent_tokens_size = len(sample_sentence.split())
    sample_sent_probability = compute_probability(sample_sentence, size_of_vocabulary,
                                                  counts_of_unigrams, counts_of_bigrams)
    # Calculate perplexity using this formula:
    # Perplexity(S) = P(S)^(-1/N)
    perplexity = math.exp(-sample_sent_probability / sample_sent_tokens_size)

    return perplexity

# Vocabulary size
size_of_vocabulary = len(counts_of_unigrams)

# Sample sentences (from homework instructions)
sample_sentence1 = "Τρώω τυρί και ελιές τα σαββατοκύριακα."
sample_sentence2 = "Στην Ελλάδα, οι άνθρωποι απολαμβάνουν μια πλούσια ποικιλία τροφίμων που περιλαμβάνει φρέσκα θαλασσινά, λαχταριστά παραδοσιακά πιάτα όπως μουσακά και σουβλάκι, αρωματικά μπαχαρικά και βότανα, καθώς και μια εκπληκτική ποικιλία τυριών και ελιών, απολαμβάνοντας το φαγητό τους με καλό κρασί ή ούζο."

# Calculate probabilities and perplexities
prob_sample_sent1 = compute_probability(sample_sentence1, size_of_vocabulary, counts_of_unigrams, counts_of_bigrams)
prob_sample_sent2 = compute_probability(sample_sentence2, size_of_vocabulary, counts_of_unigrams, counts_of_bigrams)

perp_sample_sent1 = compute_perplexity(sample_sentence1, size_of_vocabulary, counts_of_unigrams, counts_of_bigrams)
perp_sample_sent2 = compute_perplexity(sample_sentence2, size_of_vocabulary, counts_of_unigrams, counts_of_bigrams)

print(f"Sample Sentence 1: Sum of Log-Probability: {prob_sample_sent1}, Perplexity: {perp_sample_sent1}")
print(f"Sample Sentence 2: Sum of Log-Probability: {prob_sample_sent2}, Perplexity: {perp_sample_sent2}")
print()


# *******************************************************
# * PART 4:                                             *
# * Generate a new sentence in Greek                    *
# *******************************************************

import random

print("PART 4 - GENERATE A NEW SENTENCE IN GREEK")

# Get the total number of unigrams from the given Greek corpus
total_num_of_unigrams = sum(counts_of_unigrams.values())

# Sample the first word according to unigram probability
def get_first_word(counts_of_unigrams, total_num_of_unigrams):
    unigrams = list(counts_of_unigrams.keys())
    unigram_probabilities = [count / total_num_of_unigrams for count in counts_of_unigrams.values()]

    # Select the first word of the new sentence randomly based on unigram probability
    first_word = random.choices(unigrams, unigram_probabilities)[0]
    return first_word

# Sample the next word for the new sentence using conditional (bigram) probability
def get_next_word(current_word, total_num_of_unigrams, counts_of_unigrams, counts_of_bigrams):
    # Get all the bigrams that begin with the current word
    potential_bigrams = [(bigram, count_of_bigram) for bigram, count_of_bigram in counts_of_bigrams.items()
                         if bigram[0] == current_word]

    # If there are no bigrams that begin with our current word,
    # then randomly sample from the unigram distribution
    if not potential_bigrams:
        next_word = get_first_word(counts_of_unigrams, total_num_of_unigrams)
        return next_word

    # Extract the next words and their conditional probabilities
    # Get the next words and their conditional (bigram) probabilities
    size_of_unigrams = len(counts_of_unigrams)
    next_words = [bigram[1] for bigram, count_of_bigram in potential_bigrams]
    bigram_probabilities = [(count_of_bigram + 1) / (counts_of_unigrams[current_word] + size_of_unigrams)
                     for bigram, count_of_bigram in potential_bigrams]

    # Select the next word of the new sentence randomly based on conditional (bigram) probability
    next_word = random.choices(next_words, bigram_probabilities)[0]
    return next_word

# Generate the new Greek sentence
def generate_new_sentence(total_num_of_unigrams, counts_of_unigrams, counts_of_bigrams, max_words_for_sentence):
    new_greek_sentence = []

    # Get the first word of the new sentence and append it
    word_for_sent = get_first_word(counts_of_unigrams, total_num_of_unigrams)
    new_greek_sentence.append(word_for_sent)

    # Continue getting the next word for the new sentence until a period (.) is reached
    # or until you reach the max word limit
    while word_for_sent != '.' and len(new_greek_sentence) < max_words_for_sentence:
        word_for_sent = get_next_word(word_for_sent, total_num_of_unigrams, counts_of_unigrams, counts_of_bigrams)
        new_greek_sentence.append(word_for_sent)

    # End the sentence with a period if it doesn't already have one
    if new_greek_sentence[-1] != '.':
        new_greek_sentence[-1] = '.'

    return ' '.join(new_greek_sentence)

# Generate a new sentence in Greek
generated_sentence = generate_new_sentence(total_num_of_unigrams, counts_of_unigrams,
                                       counts_of_bigrams, max_words_for_sentence=12)

print("Newly Generated Greek Sentence:", generated_sentence)

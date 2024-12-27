# CS 6320 (Natural Language Processing) Portfolio
This is a portfolio for CS 6320.002 (Natural Language Processing). This portfolio is for the Fall 2024 semester at the University of Texas at Dallas, taught by Tatiana Erekhinskaya.

### Assignment 1: Basic Basic Concepts & Questions
Answer/complete the three following questions:
1. Ambiguity is the central concept in NLP. Please come up with an original
sentence that can be (partially) ambiguous. Explain the two meanings that you can see.
Add context that helps resolve the ambiguity.
2. Come up with an original prompt demonstrating Chatgpt 3.5 shortcomings. If
you could break it, show your three best attempts and explain your intentions.
Some ideas: long and convoluted context with irrelevant details, using multiple
messaging and abruptly switching the task so that it is (mis)interpreted given previous
context.
3. Find 3 favorite commercial NLP companies or products. Give a brief explanation
of why you like them.

The folder for the assignment is located [here.]()

### Assignment 2: Tokenization, Unigram & Bigram Count, and Computing Probabilities and Perplexities using a Greek Corpus
Use a corpus about food in the Greek language to do the following:
1. Use the spaCy Python library to tokenze the corpus
2. Write your own code to count unigrams and bigrams
3. Compute the probabilities and perplexities of two sentences—provided in the instructions (use add one smoothing and log(p) when encountering zeros)
4. Generate a sentence in Greek. Sample the first word according to the unigram probabilitiy, sample the next word using conditional probability, and then repeat until you get a dot as your token.

The folder for the assignment is located [here.]()

### Assignment 3: Word2vec Exploration and spaCy
Use Word2vec to do the following:
* Come up with two types of vector manipulation (e.g., king - man + woman = queen). For each type, provide at least three examples
* Come up with a relationship that is not captured by Word2vec. Give three examples.
* Come up with your own specific example of bias in Word2vec.

Come up with your own sentence and use spaCy to do the following:
* Tokenization
* Part of speech tagging
* Named entity recognition
* Dependency parsing

The folder for the assignment is located [here.]()

### Assignment 4: Protege Exploration
Take this sentence/story: "John has a sister Jane. Jane has an older brother Mark. Jane is 21 years old." and complete the following:
1. Represent main classes, instances and relations from the story in RDF/OWL
using Protege. Find 2 possible facts that can be inferred from the text - consider family
relations and age restrictions for drinking, marrying, etc. Write axioms in Protege to
make the inference.
2. Come up with a question to the story and write a SPARQL query that answers the question. Also, use Protege to load the RDF into the graph and visualize the sentence.
3. Using RDFLib (an open-source Python library), load the RDF into the graph and run the same SPARQL query. Again, feel free to use GPT for API calls.

The folder for the assignment is located [here.]()

### Project: NLP-Based Recipe Recommendation System
Our project’s goal is to develop a suggestion system that uses NLP to understand user input and suggests recipes based on meal type such as breakfast, lunch or dinner. If the user input is unclear, then it will suggest a recipe based on the current time of day. Additionally, we will create a user profile for each person's likes and dislikes, which will be taken into account when suggesting new recipes.

The project’s goal involved implementing an individualized recipe recommendation system that leverages the power of NLP and utilizes dynamic weighting. The focus was to deliver a solution that adjusts to users’ inputs, which are typically highly dynamic in user-interactive projects such as recommendation systems. Dynamic feature weighting was utilized since the application entailed context-sensitive outputs, chatting AI, and individualized recommendations.

The folder for the project is located [here.]()

FILENAME: README.txt (for Homework 3)
DUE DATE: 10/8/2024
AUTHOR:   Reg Gonzalez
EMAIL:    rdg170330@utdallas.edu (school) or regmckie@gmail.com (personal)
COURSE:   CS 6320.002, Fall 2024


DESCRIPTION:
Use Word2vec for the following:
1.) Provide working examples of vector "meaning" manipulation
2.) Provide non-working examples of vector "meaning" manipulation
3.) Provide evidence of bias 

Use spaCy for the following:
1.) Tokenization
2.) POS tagging
3.) Named entity recognition
4.) Dependency parsing


HOW TO COMPILE AND RUN:
I developed this code through the PyCharm IDE, so it can be run there or any other IDE.
Alternatively, you can run it through the command prompt terminal with a command like "python CS6320_Homework2.py".

To see a sample of what the output would look like, please refer to the document "SampleOutput.txt".


EXPLANATION OF OUTPUT:
PART 1: Word2vec - the good:
	I took a random country, removed the continent it's in, and replaced it with a different
	continent. The goal was to have Word2vec find another country in the new continent. For example,
	for the equation, France - Europe + Asia, you'd expect something like "China" or "Japan." Likewise,
	I also did this for countries and their currencies. I took a random country, remove its currency,
	and replaced it with a different country's currency. The goal was to have Word2vec find the country
	associated with the new currency. For example, for the equation, Mexico - Peso + Rupee, you'd 
	expect "India" as the output.

PART 2: Word2vec - the bad:
	I took a classical musician, removed the "classical" label, and replaced it with another genre.
	The goal was to have Word2vec find another artist that fits that genre. For example, for the
	equation, Beethoven - classical + pop, you'd expect someone like "Lady Gaga" as the output.
	However, in these instances, I got no such output. 

PART 3: Word2vec - the ugly:
	The goal was to exploit Word2vec's political biases. For the first two equations, I wanted 
	to see what words would be associated with "Republican." The first equation output "scandals,"
	which could showcase the Republican Party's propensity for scandalous behavior—particuarly 
	in recent years. The next equation output "frank," which could be a word many people choose to 
	describe Republicans—again, particularly in recent years. The last equation output "democratization,"
	which could show bias towards westernization and many western governments.

PART 4: spaCy:
	The outputs for tokenization, POS tagging, named entity recognition, and dependency parsing
	are showed. The sentence I used was "I want to be best friends with a witch and clown named
	Agatha and Harley, respectively."
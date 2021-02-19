#Question: Write a program that accepts a sequence of whitespace separated words as input and 
# prints the words after removing all duplicate words and sorting them alphanumerically. 
# Suppose the following input is supplied to the program: hello world and practice makes perfect and hello world again 
# Then, the output should be: again and hello makes perfect practice world

words = [x.lower() for x in input().split(" ")]
words = set(words)
print(" ".join(sorted(list(words))))
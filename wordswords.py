# duplicate adjacent words?
import string

input_file = open(test.txt, 'r')

words = []
duplicates = []

line_number = 1
for line in input_file:
    lines = line_str.split()
    previous_word = None
    for word in lines:
        if word != "'\n'":
            words.append(word)
        if word == previous_word:
            duplicates.append([word, line_number])
        previous_word = word
    line_number += 1

for index, word in enumerate(words):
    print(index, word)
    if words[index] == words[index + 1]:
        duplicates.append(word)
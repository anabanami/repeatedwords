# duplicate adjacent words?
import string

input_file = open("test.txt", 'r')

words = []
duplicates = []
line_list = []

for line in input_file:
    line_list.append(line)
    split_lines = line.split()

    for word in split_lines:
        if word != "'\n'":
            words.append(word)

word_number = 1
previous_word = None

# I also want to find the line where the duplicate word is....

for i in range(len(words)):
    if i == len(words) - 1:
        break      
    if words[i] == previous_word:
        # print("duplicate word found, word appended in duplicates list.")
        duplicates.append([word_number, words[i]])
        previous_word = words[i]

    else:
        previous_word = words[i]

    word_number += 1

# print(line_list)
# print(words)
# print('\n')
print("Duplicate word list")
print("[word number, word]")
for j in duplicates:
    print(j)

# duplicate adjacent words?
import string

input_file = open("test.txt", 'r')

words = []
duplicates = []
line_number_list = []

for line_number, line in enumerate(input_file, 1):
    line_number_list.append(line_number)
    split_lines = line.split()

    for word in split_lines:
        if word != "'\n'":
            lowercase_word = word.lower()
            words.append(lowercase_word)

word_number = 1
previous_word = None
for i in range(len(words)):

    if i == len(words) - 1:
        break
    
    if words[i] == previous_word:
        # print("duplicate word found, word appended in 'duplicates'.")
        duplicates.append([line_number, word_number, words[i]])
        previous_word = words[i]

    else:
        previous_word = words[i]

    word_number += 1


# print(words)
# print('\n')
print("Duplicate word list")
print("[line, word number, word]")
for k in duplicates:
    print(k)

# I want to find the line where the duplicate word is....
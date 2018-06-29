# duplicate adjacent words?
import string

input_file = open("test.txt", 'r')

words = []
duplicates = []
line_number_list = []

for line_number, line in enumerate(input_file, 1):
    split_lines = line.split()

    for word in split_lines:
        if word != "'\n'":
            lowercase_word = word.lower()
            words.append(lowercase_word)
            line_number_list.append(line_number)

# print(len(line_number_list))
# print(len(words))

word_number = 1
previous_word = None
for i in range(len(words)):

    if i == len(words) - 1:
        break
    
    if words[i] == previous_word:
        # print("duplicate word found, word appended in 'duplicates'.")
        duplicates.append([line_number_list[i], word_number, words[i]])
        previous_word = words[i]

    else:
        previous_word = words[i]

    word_number += 1

print("Duplicate word list")
print("[line, word number, word]")
for k in duplicates:
    print(k)
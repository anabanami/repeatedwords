# duplicate adjacent words?
import glob, os
import string


def find_tex():
    tex_files = []
        for file in glob.glob('*.tex'):
            tex_files.append(file)
    return tex_files

def repeat(filename):
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



if __name__ == '__main__':
    
    os.chdir('/home/ana/thesis')
    find_tex()
    for file in tex_files:
        input_file = open("file", 'r')
        repeat(input_file)
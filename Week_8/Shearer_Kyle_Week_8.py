# DSC 510
# Week 8
# Programming Assignment Week 8
# Author Kyle Shearer
# 02/04/24

#function for adding words to an empty dictionary, wd is short for word dictionary.
def add_word(word, wd):
    if word in wd:
       wd[word] = wd.get(word) +1
    else:
        wd[word] = 1


#ensuring lower or uppercase words don't make things problematic. This also includes number, punctuation, spaces, etc.
def process_line(line, word_dictionary):
    word_list = line.split()
    for word in word_list:
        word = ''.join([i for i in word if i.isalpha()])
        if word != '':
            add_word(word.lower(), word_dictionary)

#ensuring a clean and readable print, both organized and ordered from highest to lowest
def pretty_print(word_dictionary):
    print('Length of dictionary: ', len(word_dictionary))
    print("{:<25} {:<25}".format("Word","Count"))
    print('______________________________________')
    for w in sorted(word_dictionary, key=word_dictionary.get, reverse=True):
         print("{:<25} {:<25}".format(w, word_dictionary[w]))


def main():
    word_dictionary = dict()

    gba_file = open('gettysburg.txt', 'r')
    for line in gba_file:
        process_line(line, word_dictionary)
    pretty_print(word_dictionary)
if __name__ == '__main__':
    main()
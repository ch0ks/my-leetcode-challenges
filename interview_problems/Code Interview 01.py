#!/usr/bin/env python3

# Imagine you are given a plain text, ASCII, English document, something like a book from Project Gutenberg.
# Develop a concordance for the book -- the number of times each word appears -- and then print the top N most
# frequent words and how many times they occur. N can be either hardcoded or a parameter.
import string
import collections


def countWords(text, max_top_words):
    """
    This function counts the words in a text

    param text: long string
    param N: number of words

    retun: the list of most used words
    """

    word_list = collections.Counter()
    for word in text.split(' '):
        simple_word = word.lower()
        if simple_word != "":
            if simple_word not in word_list.keys():
                word_list[simple_word] = 1
            else:
                word_list[simple_word] += 1

    most_common_list = word_list.most_common(max_top_words)
    most_common_final = []
    for value in most_common_list:
        most_common_final.append(value[0])
    return most_common_final


def main():
    """
    This is the main of the program
    """
    translator = str.maketrans('', '', string.punctuation)
    top_num_words = 10
    text = ""
    with open('pg128.txt') as f:
        line = f.read()
    text += line.translate(translator).replace("\n", " ").replace("\r", "")

    list_words = countWords(text, top_num_words)
    print("The most used words:")
    for word in list_words:
        print("* " + word)


if __name__ == "__main__":
    main()

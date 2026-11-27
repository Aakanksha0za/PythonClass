# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 21:51:29 2026

@author: Admin
6. Word Frequency Counter

Write a function that receives a sentence, converts it into a list of words, and returns a dictionary containing the frequency of each word.
"""

def word_frequency(sentence):
    words = sentence.lower().split()
    print(words)
    frequency_dict = {}

    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1
        print(frequency_dict.get(word,0))

    return frequency_dict


text = "the quick brown fox jumps over the lazy dog the quick fox"
result = word_frequency(text)

print(result)


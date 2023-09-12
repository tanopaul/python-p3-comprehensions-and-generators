#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = [n for n in num_list if n % 2 == 0]
    print(even_numbers)
    return even_numbers

def make_exclamation(sentence_list):
    exclamations = [n + '!' for n in sentence_list]
    print(exclamations)
    return exclamations


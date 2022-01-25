# Author: JD 01/24/2022
# Detect Pangram, 6 kyu

"""
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

"""

import string

def is_pangram(s):
    # create a new list for later appending letters.
    new = []
    # using a for loop to go through each individual character in the sentence.
    for x in s:
        # the if statement will check if the letter that the loop is currently working on is in the list created, i.e., it will append all the letters used in the sentence into the list.
        # the first if statement will filt out all the non english letters
        if x.isalpha() == True:
            # the second if statement will append the letter to the list if it is not already in the list
            if x.lower() not in new:
                new.append(x.lower())
    # if the list contains all the characters, or it is a pangram, the list should have a length of 26 because it has all the 26 English letters. The if statement will then determine if True or False should be returned.
    if len(new) == 26:
        return True
    else:
        return False
      

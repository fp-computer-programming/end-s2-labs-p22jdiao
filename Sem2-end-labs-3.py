# Author: JD 01/24/2022
# Your order, please 6 kyu

"""
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
"""

def order(sentence):
    # Split the string into list, so each word can be used as element in the list.
    sentence = sentence.split()
    # The variable counter is created so that the time that the while loop runs will not be out of the numbers of words in the sentence.
    counter = 0
    # This variable keeps track of the serial number of the word that the loop is currently working on.
    det = 1
    # This list is created to save put the words in order.
    new = []
    # Using a while loop so that the loop runs exactly as the time that equals to the length of the sentence.
    while counter <= len(sentence):
        # Using a nested for loop to check each letter within each word.
        for x in sentence:
            for y in x:
                # if the number within the word equal to det, which is the number of order, then the word will be appended to the new list.
                if y == str(det):
                    new.append(x)
                    break
        # Then det will add 1 to be the next number of order, and counter will also add 1 so that the loop does not run out of range.
        det += 1
        counter += 1
    # Finally, join the list together seperated by a space to form a new sentence.
    new = " ".join(new)
    return new

# Author: JD 01/24/2022
# Sum of Digits / Digital Root 6 kyu

"""
Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
"""

def digital_root(n):
    while n >= 10: # check if n is a 1 digit number
        sum = 0 
        for x in str(n): # go through each digit within the number
            sum += int(x) # create the new number after adding
            
        n = sum # let n equal to the new number created so the process can be repeated again if it is still not a single digit number
        
    return n # if n is a single digit number its value will be returned

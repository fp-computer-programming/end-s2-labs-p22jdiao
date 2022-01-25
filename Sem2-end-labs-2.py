# Author: JD 01/24/2022
# Persistent Bugger. 6 kyu

"""

Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

For example (Input --> Output):

39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number)

"""
def persistence(n):
    # This variable counter is created to count the number of times multiply the digits in num until it reaches a single digit.
    counter = 0
    while True:
        # This variable is created for multiplication of each digit of the number.
        check = 1
        # When n is a single digit, its value will be returned.
        if n < 10:
            return counter
        # Using a for loop so each digit of the number will be used to mutiply.
        for x in str(n):
            check *= int(x)
        # Reset the value of n so it equals to the new value that results from the multiplication.
        n = check
        # After one calculation is completed, the counter will increase one.
        counter += 1

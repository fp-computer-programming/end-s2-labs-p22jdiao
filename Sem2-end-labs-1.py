# Author: JD 01/24/2022
# Break camelCase, 6 kyu

def solution(s):
    # Make the word into list for checking each individual letter.
    s = list(s)
    # This list is created to save the index of the capitalcase letter.
    lst = []
    # Using a for loop with .isupper() method to find the uppercase letters and save their index into the new list created.
    for i,v in enumerate(s):
        if v.isupper() == True:
            lst.append(i)
    # This for loop is used to add space before each capital letter. Because when inserting a space into the original s list, the index of all the following letters will add one,
    # so adding the index of the the number of index of s to the number itself will solve this problem.
    for i,x in enumerate(lst):
        s.insert(x+i," ")
    # The final step is to join the letters back together by using a .join() method.
    s = "".join(s)
    return str(s)
    pass

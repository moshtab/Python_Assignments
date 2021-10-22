'''
@Author: Mohsin
@Date: 2021-10-19 18:00:30
@Last Modified by: Mohsin
@Last Modified time: 2021-10-19 18:00:30
@Title : Palindrome Checker”
'''
def palindromeChecker(string):
    reverse = string[::-1]   #String Slicing Method
    if(string==reverse):
        print("String is a plindrome")
    else:
        print("String is not a palindrome")
string=str(input("Enter a string"))
palindromeChecker(string)
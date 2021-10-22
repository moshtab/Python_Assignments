'''
@Author: Mohsin
@Date: 2021-10-19 18:00:30
@Last Modified by: Mohsin
@Last Modified time: 2021-10-19 18:00:30
@Title : Anagram (listen = silent)
'''
def anagram(string1,string2):
    if(sorted(string1)==sorted(string2)):
        print("The Strings are Anagram")
    else:
        print("Strings are not anagram")
string1 = str(input("Enter a string"))
string2 = str(input("Enter a string"))
anagram(string1,string2)
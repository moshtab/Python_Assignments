'''
@Author: Mohsin
@Date: 2021-10-19 18:00:30
@Last Modified by: Mohsin
@Last Modified time: 2021-10-19 18:00:30
@Title : User Input and Replace String Template “Hello <<UserName>>, How are you?”
'''
def printUsername():
    name = input("Enter your proper name")
    if len(name) > 3:
        print("Hello " + name + ",How are you")
    else:
        print("You have entered incorrect name")

printUsername()
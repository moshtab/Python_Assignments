'''
@Author: Mohsin
@Date: 2021-10-19 18:00:30
@Last Modified by: Mohsin
@Last Modified time: 2021-10-19 18:00:30
@Title : Unorderd Linked List”
'''
def linkedList():
    x = "hello how are you"
    arr=[x.split(" ")]
    list=[]
    size =len(arr)
    for i in range(size):
        list.append(arr[i])
    print(list)
    word = str(input("Enter the word you are searching for"))
    if(list.__contains__(word)):
        list.remove(word)
    else:
        list.append(word)
    print(list)
linkedList()


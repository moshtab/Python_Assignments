'''
@Author: Mohsin
@Date: 2021-10-19 18:00:30
@Last Modified by: Mohsin
@Last Modified time: 2021-10-19 18:00:30
@Title : Binary Search
'''
def binarySearch(list,searchName):
    low = 0
    high = len(list) - 1
    mid = 0
    while low<=high:
        mid =(low+high)//2
        if(list[mid]<searchName):
            low=mid+1
        elif(list[mid]>searchName):
            high=mid-1
        else:
            return mid
    return -1

list = []
length = int(input("enter the size of list"))
for i in range(length):
    list.append(str(input("Enter the words")))
print(list)
list.sort()
print(list)
searchName=str(input("Enter the word u want to search"))
result =binarySearch(list,searchName)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
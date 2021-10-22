'''
@Author: Mohsin
@Date: 2021-10-19 18:00:30
@Last Modified by: Mohsin
@Last Modified time: 2021-10-19 18:00:30
@Title : Insertion Sort
'''
def bubbleSort(arr):
    for j in range(len(arr)-1):
        for i in range(len(arr)-1):
            if(arr[i]>arr[i+1]):
                arr[i],arr[i+1]=arr[i+1],arr[i]
arr =[2,5,3,1,6,7]
print(arr)
bubbleSort(arr)
print(arr)

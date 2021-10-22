'''
@Author: Mohsin
@Date: 2021-10-19 18:00:30
@Last Modified by: Mohsin
@Last Modified time: 2021-10-19 18:00:30
@Title : Sum of three Integer adds to ZERO”
'''
def findTriplets(arr,m):
    found = False
    for i in range(0,m):
        for j in range(i+1,m):
            for k in range(j+1,m):
                if (arr[i]+arr[j]+arr[k]==0):
                    print(arr[i],arr[j],arr[k])
                    found=True
    if (found==False):
        print("No Triplets found")

arr=[]
n = int(input("Enter the length of array"))
for i in range(n):
    arr.append(int(input("Enter a number")))
print(arr)
m=len((arr))
findTriplets(arr, m)

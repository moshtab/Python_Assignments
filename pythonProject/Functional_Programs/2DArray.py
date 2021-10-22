'''
@Author: Mohsin
@Date: 2021-10-19 18:00:30
@Last Modified by: Mohsin
@Last Modified time: 2021-10-19 18:00:30
@Title : 2D Array”
'''
def array2D():
    mrows = int(input("Enter the number of rows"))
    ncolumns = int(input("Enter the number of columns"))
    arr = []
    for i in range(mrows):
        col = []
        for j in range(ncolumns):
            col.append(int(input("Enter the number")))
        arr.append(col)
    print(arr)
array2D()
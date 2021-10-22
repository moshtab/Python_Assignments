'''
@Author: Mohsin
@Date: 2021-10-19 18:00:30
@Last Modified by: Mohsin
@Last Modified time: 2021-10-19 18:00:30
@Title : Insertion Sort
'''

def insertion_sort(fruits):
    for i in range(1, len(fruits)):
        j = i
        while (fruits[j - 1] > fruits[j] and j > 0):
            fruits[j - 1],fruits[j] = fruits[j],fruits[j - 1]
            j -= 1
fruits = ['grape', 'banana', 'strawberry', 'apple', 'peach', 'cherry']
insertion_sort(fruits)
print(fruits)
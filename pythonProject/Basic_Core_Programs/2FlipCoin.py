'''
@Author: Mohsin
@Date: 2021-10-19 18:00:30
@Last Modified by: Mohsin
@Last Modified time: 2021-10-19 18:00:30
@Title : Flip Coin and print percentage of Heads and Tails”
'''
import random

total_heads = 0
total_tails = 0
count = 0


for x in range(100):
    coin = random.randint(0, 1)
    if coin == 0:
        total_heads += 1


    elif coin == 1:
        total_tails += 1


print("Okay, you flipped heads", total_heads, "times ")
print("and you flipped tails", total_tails, "times ")
print("\nheads percentage", (total_heads / (total_heads + total_tails)) * 100, "%")
print("tails percentage ", (total_tails / (total_heads + total_tails)) * 100, "%")

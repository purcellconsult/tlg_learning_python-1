###### Variables and Types ######


# 1) integers, and floating point numbers

# 2) integers

# 3)

pi = 3.14
radius = 5
print(pi * radius ** 2)

# 4)

name = 'Gregory'
surname = 'Green'
# i) A string
# ii)
print(name + " " + surname)
# iii)
print(name.lower() + " " + surname.upper())

###### Controll Flow ######


# 5)

question = input('Is basic training difficult? ')

if question == "y":
    print("No it's not, you're just soft. ")
if question == "n":
    print("Oh ok.")

# 6)

budget = 0
amount = int(input("How much money do you have this month to spend on Groceries? (do not enter a $) "))

if amount == 0:
    print("ERROR: please enter a value that is greater than one")
elif amount >= 1000:
    print("ERROR: pleas enter a value that is less than 1000")
elif amount >= 550:
    budget = str(amount + budget)
    print("You're budget is " + "$" + budget + " looks like you're eating this month")
else:
    budget = str(amount + budget)
    print("You're broke bruh! You're budget is only " + "$" + budget + " better get in line for some foodstamps.")

# loops and structures

# 7)

g = 0

while g < 100:
    print("g i now equal to {}".format(g))
    g += 2
# i)

for num in range(0, 101, 2):
    print(num)

# 8)

import random

nums = ()

for k in range(100):
    nums = (random.randint(1,100))
    print(nums)

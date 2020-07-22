# variable

x = 5
y = 1.2636
z = 'python'

print(x)
print(y)
print(z)

# determine the type of variable

print(type(x))
print(type(y))
print(type(z))

# basic mathematical operators
# + - * / () ** %

print(5 // 3)

a = (5 * 9 / 3) + 10 ** 2
print(a)

# strings

a = 'python'
b = 'JavaScript'
c = """This is a docstring"""

# ways too format a sting in python

print('The language is', a)
print('{} and {} are programming languages'.format(a.capitalize(), b))

x = [] # empty list
x.append(10) # adds 10
x.append(20)
x.append(30)
x.append(40)

# removes items from list each time it is presented
x.pop()

print(x)

#tuples
# ------
# immutable data structures
# once created in memory, can't reassign it
# use tuple when you wan't to store data
# tuple is efficient

laptop = ('apple', 'dell', 'hp', 'sony', 'lenovo')

# index
print(latop[0]) #apple
print(laptop[-1]) #lenovo

# slice tuple
print(laptop[2:]) # (hp, sony, lenovo)

#list indexes can be reassinged
odds = [1, 3, 5]
odds[2] = 7 # [1,3,7]



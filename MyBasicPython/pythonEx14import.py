import random

print(random.choice(range(40, 50)))

mylist = ['a', 'b', 'c', 'd', 'e', 'f']

print(random.choice(mylist))

print(random.sample(range(5), 3))
# print(random.sample(range(5), 6)) error

print(random.sample(mylist, 2))

print(random.randint(9, 500))

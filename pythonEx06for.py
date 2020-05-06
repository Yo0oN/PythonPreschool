mylist = ['a', 'b', 'c', 'd', 'e']
for alp in mylist :
    print(alp)

for i, v in enumerate(mylist) :
    print(i, v)

a = range(3)
b = range(3, 10, 2)
print(a)
print(b)

for n in range(0, 3) :
    print(n)

print()

for n in range(2, 3) :
    print(n)

print()

for n in range(0, 10, 2) :
    print(n)

print()

for n in range(0, 4, 2) :
    print(mylist[n])

print()

mydict = {'일' : 1, '이': 2, '삼' : 3, '사' : 4, '오' : 5, '육' : 6, '칠' : 7}

for dict in mydict :
    print(dict)

print()

for dict in mydict.values() :
    print(dict)

print()

for dictindex, dictkey in mydict.items() :
    print(dictindex, dictkey)

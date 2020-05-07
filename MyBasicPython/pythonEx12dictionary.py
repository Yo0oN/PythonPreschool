mydict = {}
mydict['key1'] = 'value1'
mydict['key2'] = 'value2'
mydict['key3'] = 'value3'
mydict['key4'] = 'value4'

print(mydict)

print(mydict['key4'])

del mydict['key3']

print(mydict)

print()

print(mydict.values())

print()

# dictionary를 반복문으로 그냥 출력하면 키가 나온다.
for val in mydict :
    print(val)

print()

# 값을 뽑고싶다면 values()를 이용해 값을 반복문에 넣어야한다.
for val in mydict.values() :
    print(val)

print()

print(mydict.keys())

print()

for val in mydict.keys() :
    print(val)

print()

print(mydict.items())

print()

for val in mydict.items() :
    print(val)

print()

for key, val in mydict.items() :
    print(key, val)

print()

# print(mydict['key3'])error

mytuple = 1, 2, 3
print(mytuple)
print(mytuple[2])

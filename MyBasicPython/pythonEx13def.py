def add (num1, num2) :
    return num1 + num2

print(add(3, 5))

def addmi (num1, num2) :
    return num1 + num2, num1 - num2

test = addmi(3, 5)
print(test, type(test))
print(test[0], test[1])

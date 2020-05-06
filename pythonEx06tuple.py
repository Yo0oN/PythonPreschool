mytuple = ()
print(mytuple, type(mytuple))
mytuple = 1, 2, 3 # mytuple에 1, 2, 3이 각각 packing 되어 들어간다.
num1, num2, num3 = mytuple # mytuple에 있는 값들이 각 변수에 unpacking 된다.
print(mytuple)
print(num1)
print(num2)
print(num3)
# num1, num2, num3, num4 = mytuple
# 수가 맞지 않으면 error


numbers = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]
for number in numbers :
    if number % 2 == 0 :
        print(number, '이것은 짝수입니다.')

print()

for number in numbers :
    if number % 2 == 0 :
        print(number, '이것은 짝수입니다.')
    elif number % 2 == 1 :
        print(number, '이것은 홀수입니다.')
    else : 
        print(number, '이것은 소수입니다.')

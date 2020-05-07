a = 0
while a < 5 :
    print(a, ': 5보다 작습니다.')
    a += 1

print()

b = 0
while True :
    if b % 2 == 0 :
        print(b, '짝수입니다.')
        b += 1
        continue
    if b == 5 :
        print(b, '입니다. 종료합니다.')
        break  
    print(b, '홀수입니다.')
    b += 1



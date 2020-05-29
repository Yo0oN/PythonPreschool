import random

def selection_sort(list1) :
    # 배열의 처음부터 마지막 - 1만큼 반복
    for pivot in range(0, len(list1) - 1) :
        # 가장 작은 값의 인덱스가 들어갈 lowest
        lowest = pivot
        # 기준점 다음부터, 마지막까지 반복
        for index in range(pivot + 1, len(list1)) :
            # 만약 확인중인 곳의 값이 현재 lowest값보다 작다면 넣기
            if list1[lowest] > list1[index] :
                lowest = index
        # 마지막에는 자리 바꿔주기.
        list1[pivot], list1[lowest] = list1[lowest], list1[pivot]
    return list1


list1 = random.sample(range(100), 10)

print(list1)
selection_sort(list1)
print(list1)

import random

def insertion_sort (list1) :
    # 기준점은 1부터 시작이다.
    for pivot in range(1, len(list1)) :
        # 기준점과 그 아래의 값들을 비교한다.
        for index in range(pivot, 0, -1) :
            # 기준점이 더 작으면 자리를 바꾼다.
            if list1[index] < list1[index - 1] :
                list1[index], list1[index - 1] = list1[index - 1], list1[index]
            # 기준점이 비교중인 값보다 크거나 같으면 다음 기준점으로 넘어간다.
            else :
                break
    return list1

list1 = random.sample(range(100), 10)
print(list1)
print(insertion_sort(list1))

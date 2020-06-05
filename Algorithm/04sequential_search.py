from random import *

rand_data_list = list()

# 1부터 100까지 수를 하나 뽑아 list에 넣기.
for num in range(10) :
    rand_data_list.append(randint(1, 100))

def sequential_search(rand_data_list, search_data) :
    # 순서대로 확인하다가 값이 있다면 해당 인덱스를
    for index in range(len(rand_data_list)) :
        if rand_data_list[index] == search_data :
            return index
    # 없다면 -1 반환
    return -1

print(rand_data_list)
rand_int = randint(1, 100)
print(sequential_search(rand_data_list, rand_int), rand_int)

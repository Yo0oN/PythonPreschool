import random

def binary_search(list1, search) : # 배열과, 원하는 수를 받음.
    # 만약 배열의 길이가 1이고, 찾는값이 맞다면 True
    if len(list1) == 1 and list1[0] == search :
        return True
    # 만약 배열의 길이가 1이고, 찾는값이 아니라면 False 또는 길이가 0이어도 False
    elif (len(list1) == 1 and list1[0] != search) or len(list1) == 0:
        return False
    

    point = int(len(list1) / 2) # 포인트, 중앙값

    if list1[point] == search : # 만약 중앙값이 찾는값과 같다면 True
        return True
    
    # 찾는값이 중앙값보다 작다면 0부터 포인트까지 다시 탐색
    elif list1[point] > search :
        return binary_search(list1[:point], search)

    # 찾는값이 중앙값보다 크다면 포인트부터 마지막까지 다시 탐색
    elif list1[point] < search :
        return binary_search(list1[point:], search)

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(binary_search(list1, 30))

list2 = random.sample(range(100), 10)
print(list2)
list2.sort()
print(list2)
print(binary_search(list2, 30))

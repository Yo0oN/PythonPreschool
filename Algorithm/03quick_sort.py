import random

def quick_sort (list1) :
    if len(list1) <= 1 : # 길이가 1이 되면 그대로 list1을 반환.
        return list1
    
    pivot = list1[0] # 기준점은 첫번째수

    left = list() # 기준점보다 작은 수들의 배열
    right = list() # 기준점보다 큰 수들의 배열
    
    for i in range(1, len(list1)) :
        if list1[i] < pivot : # 기준점보다 작다면 왼쪽
            left.append(list1[i])
        else : # 크거나 같다면 오른쪽
            right.append(list1[i])
    
    return quick_sort(left) + [pivot] + quick_sort(right)


list1 = random.sample(range(100), 10)

print(list1)
list1 = quick_sort(list1)
print(list1)

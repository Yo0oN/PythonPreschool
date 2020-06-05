import random

# 병합정렬
def merge_sort (list1) :
    if len(list1) <= 1 : # 길이가 1이라면 그대로 
        return list1
    splitpoint = len(list1) // 2
    left = merge_sort(list1[:splitpoint])
    right = merge_sort(list1[splitpoint:])
    
    return merge1(left, right)

def merge1 (left, right) :
    leftpoint, rightpoint = 0, 0
    resultlist = list()
    # 만약 양쪽 다 남아있을 경우
    while len(left) > leftpoint and len(right) > rightpoint :
        if left[leftpoint] > right[rightpoint] :
            resultlist.append(right[rightpoint])
            rightpoint += 1
        else :
            resultlist.append(left[leftpoint])
            leftpoint += 1
    # 왼쪽만 남아있을 경우
    while len(left) > leftpoint :
        resultlist.append(left[leftpoint])
        leftpoint += 1
    # 오른쪽만 남아있을 경우
    while len(right) > rightpoint :
        resultlist.append(right[rightpoint])
        rightpoint += 1
    return resultlist

list1 = random.sample(range(100), 10)

print(list1)
list1 = merge_sort(list1)
print(list1)

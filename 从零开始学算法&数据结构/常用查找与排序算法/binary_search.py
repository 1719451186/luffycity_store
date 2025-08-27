def binary_search(list, val):
    left = 0
    right = len(list) - 1
    while left <= right:      #说明候选区域有值存在
        mid = (left+right)//2 # mid 就是候选区中间的值
        if list[mid] == val:
            return mid
        elif list[mid] > val: # 说明val在mid的左边
            right = mid - 1   # 要把right移动到mid的左边
        else:                 # list[mid] < val说明val在mid的右边
            left = mid + 1
    else:
        return None           # 说明候选区没有值了，没找到
    
list = [1,3,5,7,9,11,13,15]
print(binary_search(list, 11))
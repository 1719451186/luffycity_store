

import random

# 升序 list[j] > list[j+1]
# 降序 list[j] < list[j+1]

# 初始版本
def bubble_sort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j] # 交换

# 改进版本
def bubble_sort_2(list):
    for i in range(len(list)-1):
        if_exchange = False
        for j in range(len(list)-i-1):
            if list[j] < list[j+1]:
                list[j], list[j+1] = list[j+1], list[j] # 交换
                if_exchange = True  
        if not if_exchange: # 如果没有交换，说明已经有序，直接退出
            return 


# 验证
list1 = [random.randint(1, 1000) for _ in range(10)]
list2 = [random.randint(1, 1000) for _ in range(10)]
print(list1)
print(list2)

print("------------------")
# 正序 倒序实验
bubble_sort(list1)
bubble_sort_2(list2)
print(list1)
print(list2)



def redix_sort(li):
    max_num = max(li)
    iter = 0 # 迭代次数
    while 10**iter < max_num:
        bucket = [[] for _ in range(10)] # 十个桶
        for val in li:
            digit = val // (10**iter) % 10
            bucket[digit].append(val)
        li.clear()
        for buc in bucket:
            li.extend(buc)
        iter += 1

# 测试代码
import random

li = list(range(100000))
random.shuffle(li)
print(li)
redix_sort(li)
print(li)
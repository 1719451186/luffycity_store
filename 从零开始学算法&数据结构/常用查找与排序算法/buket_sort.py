def buket_sort(li, n = 100, max_num = 10000):
    # n个桶，最大的数是10000
    buckets = [[] for _ in range(n)] # 创建n个空桶
    for var in li:
        i = min(var // (max_num // n), n-1) # 计算var应该放入哪个桶
        buckets[i].append(var)
        # 这里借鉴冒泡排序进行排序
        for j in range(len(buckets[i])-1, 0, -1):
            if buckets[i][j] < buckets[i][j-1]:
                buckets[i][j], buckets[i][j-1] = buckets[i][j-1], buckets[i][j]
            else:
                break
    sorted_result = []
    for bucket in buckets:
        sorted_result.extend(bucket)
    return sorted_result

# 测试
import random
li = [random.randint(0, 10000) for _ in range(10000)]
print("排序前：", li)
li = buket_sort(li)
print("排序后：", li)
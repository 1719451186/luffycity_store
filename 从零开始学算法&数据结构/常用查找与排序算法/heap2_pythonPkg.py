import heapq # q-->queue 优先队列
import random

li = list(range(100))
random.shuffle(li)

print(li)

heapq.heapify(li)  # 原地建堆，时间复杂度O(n)
li_result = []
for i in range(len(li)):
    li_result.append(heapq.heappop(li))  # 每次弹出堆顶元素，时间复杂度O(logn)
print(li_result)

# python的队列的内置模块
from collections import deque # 双向队列

# q = deque([1, 2, 3], 5) # 创建一个空的双向队列
# q.append(5) # 在队列的右侧(队尾)添加元素1
# print(q.popleft()) # 从队列的左侧(队首)删除并返回一个元素

# 另一个方向
# q.appendleft(2) # 在队列的左侧(队首)添加元素2
# print(q.pop()) # 从队列的右侧(队尾)删除并返回一个

# 可以利用这个特性实现一个类似linux的tail命令

def tail(n):
    with open('test.txt', 'r') as f:
        q = deque(f, n)
        return q
print(tail(4)) # 返回文件的最后4行
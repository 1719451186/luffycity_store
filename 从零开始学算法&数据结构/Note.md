1. 更高效,在应聘的时候更有优势；
为什么要考算法题，因为算法好的程序员思维非常敏捷，代码会很高效；

1.2 时间复杂度：
- 时间复杂度：用来评估算法运行效率的一个式子；
- for循环中n代表问题的规模，会影响代码的运行时间；
- 不同的n会得到不同的时间，所以要用时间复杂度这个概念去估计不同代码的运行时间；
``` python
print('Hello World') # O(1)  常数时间复杂度

for i in range (n):
    print("Hello World") # O(n)  线性时间复杂度

for i in range (n):
    for j in range (n):
        print("Hello World") # O(n*n)  平方时间复杂度

for i in range (n):
    for j in range (n):
        for k in range (n):
            print("Hello World") # O(n*n*n)  立方时间复杂度

print('Hello World')
print('Hello Python')
print('Hello Algorithm')
# 以上三个式子的时间复杂度加起来时O(1)+O(1)+O(1)=O(1)

for i in range (n):
    print("Hello World")
    for j in range (n):
        print("Hello World") # O(n*n)  平方时间复杂度

while n>1:
    print(n)
    n = n//2
# 上面这个式子的时间复杂度 = O(logn) 用对数形式表示这个的时间复杂度
# 当算法出现循环问题规模缩小一半的时候，会出现对数情况的时间复杂度

```

- 时间复杂度时用来估算算法运行时间的式子
- 一般来说，时间复杂度高的算法比时间复杂度低的算法的运算时间慢
- 常见的时间复杂度
    - ```O(1) < O(logn) < O(n) < O(n^2) < O(n^2*logn) < O(n^3)```

1.3 简单判断时间复杂度的方法：
- 快速判断算法复杂度（适用于绝大多数简单情况）：
    - 确定问题规模n（之前是循环次数）;
    - 判断循环是否有循环减半过程 --> O(logn);
    - 判断有几层循环 3 层就是 n^3;

1.4 空间复杂度：
- 用来评估算法占内存大小的一个式子
- 空间复杂度的表示方式与时间复杂度完全一样 
    - 算法使用了整数个标量：O(1)
    - 算法使用了长度为n的一位列表 ：O(n)
    - 算法使用了m行n列的二位列表：O(n*m)
- **时间比空间重要很多**

1.5 递归
- 特点
    - 调用自身
    - 结束条件


```python 
# 合法递归
def func3(x):
    if x > 0:
        print(x)
        func3(x-1)

# 不合法递归
def func2(x):
    if x> 0 :
        print(x)
        func2(x+1)
```

2. 常用查找与排序算法
- 查找：在一些数据元素中，通过一定方法查找出与给定关键字相同的数据元素的过程
- 列表查找：从列表中找
    - 输入：列表、带查找的元素
    - 输出：被查找元素的下表
2.1 顺序查抄(Linear Search)：
- 线性查找，从第一个开始找，找到为止，如果到最后一个也没找到，就返回-1 or null
``` python
def linear_search (list, val):
    for index, v in enumerate(list):
        if v == val:
            return index
    else :
        return None
```
- 时间复杂度 O(n)

2.2 二分查找(Binary Search)介绍
- 又叫折半查找，从**有序**列表中的一半开始找，如果列表中间这个值对比待选值，判断往上找还是往下找。
- 从列表中查找元素3：
    - list = 1,2,3,4,5,6,7,8,9
    - left = 0, right = n-0
    - mid = (left+right)/2
    - while mid > 3 then right = mid -1
``` python
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
```
- 二分查找的时间复杂度 = O(logn)
- 所以二分查找比线性查找的效率高

- python的内置列表函数：index()就是线性查找，没有用二分查找，主要是二分查找的输入列表一定要是有序列表；

2.3 列表排序：
- 排序：将一组**无序**的记录序列调整为**有序**的记录序列；
    - 输入：列表
    - 输出：有序列表
- 升序与降序
- 内置排序函数：sort()

2.4 冒泡排序(Bubble Sort)
- 列表每两个相邻的数，如果前面比后面大，则交换这两个数；
```python
def bubble_sort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j] # 交换
```
- 时间复杂度是 ：O(n^2) 

2.5 选择排序(Selection Sort)
- 每次从无序列表中选择最小的元素，放到有序列表的末尾；
```python
def select_sort_simple(list):
    list_result = []
    for i in range(len(list)):
        min_vla = min(list)
        list_result.append(min_vla) # 按值添加
        list.remove(min_vla) # 按值删除
    return list_result
```
- 这个算法有致命缺点：
  - 空间复杂度翻倍，用了两个列表
  - remove()函数的时间复杂度是O(n)，所以这个算法的时间复杂度是O(n^2) + O(n^2) = O(n^2)，**时间复杂度非常的高**

- 改进版选择排序
```python 
def select_sort(list):
    for i in range(len(list)-1):
        min_loc = i # 最小值位置
        for j in range(i, len(list)): # 为了找到无序区的最小值
            if list[j] < list[min_loc]:
                min_loc = j
        list[i], list[min_loc] = list[min_loc], list[i] # 交换最小值和这个队列的第一个值
    return list
```
- 算法关键点：有序区和无序区`range(i, len(list))`、无序区最小数的位置`min_loc`
- 这个改进版的时间复杂度就是 **O(n^2)**

2.9 插入排序(insert_sort)
- 通过按顺序将无序区的元素插入到有序区中
``` python
def insert_sort(ls):
    for i in range(1, len(ls)): # i 表示摸到的牌的下标
        j = i-1 # j 表示手里牌的下标
        tmp = ls[i]
        while ls[j] > tmp and j>= 0:
            ls[j+1] = ls[j]
            j -= 1
        ls[j+1] = tmp
        print(ls)
```
- 时间复杂度为：O(n^2)
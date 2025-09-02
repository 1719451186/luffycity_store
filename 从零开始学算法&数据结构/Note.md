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

2.10 快速排序法(quick_sort)
- 思路：
    - 取第一个元素p，是元素p归为
    - 列表被p分为两部分，左边比p小，右边比p大
    - 递归完成排序
- 这是一个对称的代码，比较好背，一个while套着两个while
``` python
def partition(ls,left,right):
    tmp = ls[left] # 设定基准值（pivot）
    while left < right:
        while ls[right] >= tmp and left < right:
            right -= 1
        ls[left] = ls[right]
        while ls[left] <= tmp and left < right:
            left += 1
        ls[right] = ls[left]
    ls[left] = tmp

def quick_sort(ls, left, right):
    if left < right:
        mid = partition(ls, left, right)
        quick_sort(ls, left, mid - 1)
        quick_sort(ls, mid + 1, right)
```
- 快速排序的效率
    - 时间复杂度： O(nlogn) # 比冒泡排序要快，冒泡排序的时间复杂度是n^2
- 问题：
    - 递归的问题， 递归最大深度，最大深度可以改，但是会消耗超级多的系统资源；
    - 快速排序有一个最坏情况出现：
        - list = [9,8,7,6,5,4,3,1]  ;
        - 每次都只排序一个数，这样时间复杂度就扩大成为了n^2;

2.13 堆排序前置知识-树
- 树结构：一种数据结构
- 树是由n个节点组成的集合：
    - n = 0 ，空树；
    - n > 0 , 存在1个节点作为树的的根节点，其他节点可以分为m个集合，每个集合又是一颗树；
- 一些概念：
    - 树的根节点、叶子节点；
    - 树的深度（高度）
    - 树的度（最多分叉的那个节点有多少个分叉，就是多少度）
    - 孩子节点/父节点
    - 子树

2.14 堆排序前置知识-二叉树&堆：
- 概念：不超过2的树（每个节点最多有两个分叉）
    - 满二叉树：每层节点，要不有两个孩子节点，要不没有孩子节点，是叶子节点
    - 完全二叉树

- 二叉树的存储方式（表示方式，计算机里面是怎么存储的）
    - 链式存储方式
    - **顺序存储方式**
        - 若父亲节点的编号是 i 那么左孩子节点的编码就是 2i+1
        - 若父亲节点的编号是 i 那么右孩子节点的编码就是 2i+2
        - 若孩子节点的编号是 i 那么父亲节点的编号就是 (i-1)%2

2.15 堆排序
- 堆： 一种特殊的完全二叉树结构：
    - 大根堆：一棵完全二叉树，满足任一节点都比其孩子节点大；
    
      ![大根堆](D:\work_space\luffycity\从零开始学算法&数据结构\img\大根堆.png)
    
    - 小根堆：一颗完全二叉树，满足任一节点都比其孩子节点小；
    
      ![小根堆](D:\work_space\luffycity\从零开始学算法&数据结构\img\小根堆.png)
- 后续主要以大根堆为例子
- 堆的向下调整性质：

    - 假设如果，节点的左右子树都是堆，但是自身不是堆


2.17 向下调整函数的实现：

- 堆排序的过程
  1. 建立一个堆
     1. 堆顶一定是所有数里面最大的；
     2. 如果堆顶不是最大的，从最后一个父节点开始，对它自身和它的子节点，进行排序，把最大值跟当作这个父节点，然后依次从后往前，最后做到根节点；
     3. 这样就有了一个堆；
  2. 挨个出数，先出顶端最大的数（得到堆顶元素）；
  3. 把整个堆**最后一个元素**，不管是不是最大的，放上去；
  4. 进行一次**向下调整**，把这个不是堆的树，变成堆；
  5. 然后就可以再循环 b 取出顶端最大的数；

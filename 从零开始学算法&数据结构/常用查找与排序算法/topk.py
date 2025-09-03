def sift(ls, low, high):
    """
    :param ls: List
    :param low: int 表示为堆的第一个元素的下标, 堆顶，根节点;
    :param high: int 表示为堆的最后一个元素的下标;
    """
    i = low  # 堆的第一个元素的下标
    j = i * 2 + 1  # j为i节点的左子节点
    tmp = ls[low]  # 将堆顶的元素存起来
    while j <= high:  # 我的左子节点的下表，没有超过堆的最后一个元素的下标，也代表 ，这个节点有子节点
        if j + 1 <= high and ls[j + 1] < ls[j]:  # 如果右子节点大于左子节点 且 右子节点没有超过堆的最后一个元素的下标(小根堆)
            j = j + 1
        if ls[j] < tmp: # 这里是小根堆
            ls[i] = ls[j]
            i = j  # 已经往下挪了一层了，因为i指向了自己的左孩子
            j = 2 * i + 1
        else:
            ls[i] = tmp  # 把tmp放到i的位置上面去, 等于是把tmp放到了一个子堆甚至整个堆的堆顶
            break
    else:
        ls[i] = tmp  

def topk(ls, k):
    heap = ls[0:k]
    # 1.建堆
    for i in range((k-2)//2,-1,-1):
        sift(heap, i, k-1)
    # 2.遍历列表中剩余的元素
    for i in range(k, len(ls)-1):
        if ls[i] > heap[0]:
            heap[0] = ls[i]
            sift(heap, 0, k-1)        
    # 3.挨个抽数
    for i in range(k - 1, -1, -1):
        # 需要让i指向堆的最后一个元素，就得倒序range()
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)
    return heap



import random 
li = [i for i in range(100)]
random.shuffle(li)

print(li)
print(topk(li, 10))
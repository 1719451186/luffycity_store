def sift(ls, low, high):
    """
    :param ls: List
    :param low: int 表示为堆的第 一个元素的下标, 堆顶，根节点;
    :param high: int 表示为堆的最后一个元素的下标;
    """
    i = low  # 堆的最后一个元素的下标
    j = i * 2 + 1  # j为i节点的左子节点
    tmp = ls[low]  # 将堆顶的元素存起来
    while j <= high:  # 我的左子节点的下表，没有超过堆的最后一个元素的下标，也代表 ，这个节点有子节点
        if j + 1 <= high and ls[j + 1] > ls[j]:  # 如果右子节点大于左子节点 且 右子节点没有超过堆的最后一个元素的下标
            j = j + 1
        if ls[j] > tmp:
            ls[i] = ls[j]
            i = j  # 已经往下挪了一层了，因为i指向了自己的左孩子
            j = 2 * i + 1
        else:
            ls[i] = tmp  # 把tmp放到i的位置上面去, 等于是把tmp放到了一个子堆甚至整个堆的堆顶
            break
    else:
        ls[i] = tmp  #


def heap_sort(ls):
    n = len(ls)
    # 1.建堆
    # 找到最后一个节点的下标，就是n-1,它的父亲就是，((n-1)-1)//2 = n//2-1
    for i in range((n - 2) // 2, -1, -1):
        # i 代表了建堆的时候调整的部分的根的下标
        sift(ls, i, n - 1)  # high 的作用就是保证j不越界
    # 建堆完成了
    # 2.挨个出数
    for i in range(n - 1, -1, -1):
        # 需要让i指向堆的最后一个元素，就得倒序range()
        ls[0], ls[i] = ls[i], ls[0]
        sift(ls, 0, i - 1) # i-1是新的堆的最后一个元素的下标
    print(ls)


# 这里是为了验证
list_1 = [i for i in range(100)]
import random
random.shuffle(list_1)
print(list_1)
heap_sort(list_1)
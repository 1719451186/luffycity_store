
def sift(ls, low, high):
    """
    :param ls: List
    :param low: int 表示为堆的第 一个元素的下标, 堆顶，根节点;
    :param high: int 表示为堆的最后一个元素的下标;
    """
    i = low # 堆的最后一个元素的下标
    j = i*2+1 # j为i节点的左子节点
    tmp = ls[low] # 将堆顶的元素存起来
    while j <= high: # 我的左子节点的下表，没有超过堆的最后一个元素的下标，也代表 ，这个节点有子节点
        if ls[j+1]>ls[j] and j+1<=high: # 如果右子节点大于左子节点 且 右子节点没有超过堆的最后一个元素的下标
            j = j + 1
        if ls[j] > tmp:
            ls[i] = ls[j]
            i = j # 已经往下挪了一层了，因为i指向了自己的左孩子
            j = 2*i + 1
        else:
            ls[i] = tmp # 把tmp放到i的位置上面去, 等于是把tmp放到了一个子堆甚至整个堆的堆顶
            break
    else:
        ls[i] = tmp

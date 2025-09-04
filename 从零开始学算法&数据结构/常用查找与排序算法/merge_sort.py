def merge(ls, low, mid, high):
    '''
    low - mid 就是前半段有序序列
    mid - high 就是后半段有序序列
    '''
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:
        if ls[i] < li[j]:
            ltmp.append(ls[i])
            i += 1
        else:
            ltmp.append(ls[j])
            j += 1
    while i <= mid:
        ltmp.append(ls[i])
        i += 1
    while j <= high:
        ltmp.append(ls[j])
        j += 1
    li[low:high+1] = ltmp

def merge_sort(ls, low, high):
    if low < high :
        mid = (low+high)//2
        merge_sort(ls, low, mid) 
        merge_sort(ls, mid+1, high)
        merge(ls, low, mid, high)

li = [54,26,93,17,77,31,44,55,20]
merge_sort(li, 0, len(li)-1)
print(li)

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
    return left

def quick_sort(ls, left, right):
    if left < right:
        mid = partition(ls, left, right)
        quick_sort(ls, left, mid - 1)
        quick_sort(ls, mid + 1, right)


list = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
quick_sort(list,0,len(list)-1)
print(list)
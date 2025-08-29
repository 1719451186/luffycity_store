def select_sort_simple(list):
    list_result = []
    for i in range(len(list)):
        min_vla = min(list)
        list_result.append(min_vla) # 按值添加
        list.remove(min_vla) # 按值删除
    return list_result

# 不希望新建一个新的列表，浪费空间复杂度
def select_sort(list):
    for i in range(len(list)-1):
        min_loc = i # 最小值位置
        for j in range(i, len(list)):
            if list[j] < list[min_loc]:
                min_loc = j
        list[i], list[min_loc] = list[min_loc], list[i] # 交换
    return list

list1 = [64, 25, 12, 22, 11]
print(select_sort(list1))

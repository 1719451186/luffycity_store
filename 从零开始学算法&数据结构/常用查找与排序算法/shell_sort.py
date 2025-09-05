def insert_sort(ls, gap):
    for i in range(gap, len(ls)): # i 表示摸到的牌的下标
        j = i-gap # j 表示手里牌的下标
        tmp = ls[i]
        while j>= 0 and ls[j] > tmp:
            ls[j+gap] = ls[j]
            j -= gap
        ls[j+gap] = tmp

def shell_sort(ls):
    gap = len(ls) // 2
    while gap >= 1:
        insert_sort(ls, gap)
        gap = gap // 2


list_1 = [5,3,6,2,10,8,7,4,9,1]
shell_sort(list_1)
print(list_1)
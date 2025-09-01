def insert_sort(ls):
    for i in range(1, len(ls)): # i 表示摸到的牌的下标
        j = i-1 # j 表示手里牌的下标
        tmp = ls[i]
        while ls[j] > tmp and j>= 0:
            ls[j+1] = ls[j]
            j -= 1
        ls[j+1] = tmp
        print(ls)

list_1 = [5,3,6,2,10,8,7,4,9,1]
insert_sort(list_1)
print(list_1)
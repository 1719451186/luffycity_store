def list_to_dic(list):
    return {item: "test" for item in list}

def bubble_sort(ls, IF_BUB = 0):
    list_result = []
    for i in ls:
        if i%2 == 1:
            list_result.append(i)
    if IF_BUB == 1:
        for i in range(len(list_result)-1):
            for j in range(len(list_result)-1-i):
                if list_result[j] > list_result[j+1]:
                    list_result[j], list_result[j+1] = list_result[j+1], list_result[j]
        return list_result
    elif IF_BUB == 0:
        return sorted(list_result)

list_1= [5,3,2,8,1,4]

print(list_to_dic(bubble_sort(list_1, IF_BUB=0)))

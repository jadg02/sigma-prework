#queue FIFO order

def min_max(lst):
    if len(lst) == 0:
        raise Exception('Error: empty list')
    else:
        min_num = lst[0]
        max_num = lst[0]

        for el in lst:
            if el < min_num:
                min_num = el
            if el > max_num:
                max_num = el
    return [min_num,max_num]

lst = [2,4,1,0,2,-1]

min_max_lst = min_max(lst)
print(min_max_lst)

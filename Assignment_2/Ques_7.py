def swap_list(list1):
    list1[0], list1[-1] = list1[-1], list1[0]
    return list1
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(swap_list(list1))
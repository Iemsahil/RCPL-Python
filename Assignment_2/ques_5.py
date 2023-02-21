def even_odd(list1):
    even_list = []
    odd_list = []
    for x in list1:
        if x % 2 == 0:
            even_list.append(x)
        else:
            odd_list.append(x)
    return even_list, odd_list
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_list, odd_list = even_odd(list1)
print(even_list)
print(odd_list)
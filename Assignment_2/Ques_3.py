def largest(list1):
    max_num = list1[0]
    for num in list1:
        if num > max_num:
            max_num = num
    return max_num


list1 = [1, 99, 3, 4, 5]
print(largest(list1))

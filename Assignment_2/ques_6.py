def square_list(list1):
    square_list = []
    for x in list1:
        square_list.append((x, x**2))
    return square_list
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(square_list(list1))
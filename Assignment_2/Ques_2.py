def merge_sort(list1, list2):
    merged_list = list1 + list2
    merged_list.sort()
    return merged_list

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
print(merge_sort(list1, list2))



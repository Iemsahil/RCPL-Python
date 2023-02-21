def sort_by_length(list1):
    list1.sort(key=len)
    return list1
list1 = ['a', 'aaaa', 'aa', 'aaaaa', 'aaa']
print(sort_by_length(list1))

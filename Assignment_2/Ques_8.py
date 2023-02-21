def count(list1):
    count = 0
    for x in list1:
        if len(x) >= 2 and x[0] == x[-1]:
            count += 1
    return count
list1 = ['abc', 'xyz', 'aba', '1221']
print(count(list1))
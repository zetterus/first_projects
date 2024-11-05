def move_zeros(lst):
    zeros_count = lst.count(0)
    while 0 in lst:
        lst.remove(0)
    lst.extend([0]*zeros_count)
    return lst


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))

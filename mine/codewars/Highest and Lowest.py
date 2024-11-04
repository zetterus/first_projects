def high_and_low(numbers):
    num_lst = list(map(int, numbers.split(" ")))
    result = F"{max(num_lst)} {min(num_lst)}"
    # ...
    return result

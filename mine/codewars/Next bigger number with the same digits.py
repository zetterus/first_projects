def next_bigger(n):
    str_n = str(n)
    if all(str_n[i] >= str_n[i + 1] for i in range(len(str_n) - 1)):
        return -1
    else:
        for i in range(-1, -len(str_n), -1):
            if int(str_n[i]) > int(str_n[i - 1]) and str_n[i] != "0":
                num = str_n[i - 1]
                replacer = min(s for s in str_n[i:] if s > num)
                rest = "".join(sorted(list(str_n[i - 1:].replace(replacer, "", 1))))
                return int(str_n[:i - 1] + replacer + rest)


print(next_bigger(144))

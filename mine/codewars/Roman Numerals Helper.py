roman_to_value = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}

value_to_roman = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I'
}


def to_roman(val: int) -> str:
    result = ""
    for num in value_to_roman.keys():
        result += (val // num) * value_to_roman[num]
        val = val % num
        if not val:
            break
    return result


def from_roman(roman_num: str) -> int:
    result = 0
    prev_num = 0
    for s in roman_num[::-1]:
        num = roman_to_value[s]
        if num >= prev_num:
            result += num
        else:
            result -= num
        prev_num = num
    return result


print(to_roman(4))

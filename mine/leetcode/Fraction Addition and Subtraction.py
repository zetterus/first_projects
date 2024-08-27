from fractions import Fraction

s = input()

if s[0] != "-":
    s = "+" + s

result = 0
temp = ""

for c in s[::-1]:
    if c not in ("+", "-"):
        temp += c
    elif c == "+" and temp:
        print(temp[::-1])
        result += Fraction(temp[::-1])
        temp = ""
    elif c == "-" and temp:
        print(temp[::-1])
        result -= Fraction(temp[::-1])
        temp = ""

print(str(result.numerator) + "/" + str(result.denominator))
print()
print(type(result))

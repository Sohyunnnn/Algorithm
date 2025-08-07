import sys

for line in sys.stdin:
    result = [0, 0, 0, 0]
    for char in line:
        if char.islower():
            result[0] += 1
        elif char.isupper():
            result[1] += 1
        elif char.isdigit():
            result[2] += 1
        elif char == " ":
            result[3] += 1
    print(*result)

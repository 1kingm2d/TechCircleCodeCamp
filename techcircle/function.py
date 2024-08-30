def infinite_arguments(*args):
    sum = 0
    for arg in range(100000000000):
        sum += arg
    return sum

grades = [10, 20, 30]

print(len(grades))
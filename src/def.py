def power(x, n=2):
    return x ** n


# num1 = int(input("请输入第一个数："))
# num2 = int(input("请输入第二个数："))
# print(power(num1, num2))


def calc(*numbers):
    sam = 0
    for item in numbers:
        sam = sam + item
    return sam


print(calc(*[1, 2, 3, 4, 4, 5, 65, 6, 7, 87, 8, 9, 9]))

from functools import reduce

digists = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': '.'}


def str2float(s):
    return digists[s]


def fn(x, y):
    return x * 10 + y


print(reduce(fn, map(str2float, "123456")))

# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')

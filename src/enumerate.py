# 在迭代 ['Adam', 'Lisa', 'Bart', 'Paul'] 时，如果我们想打印出名次 - 名字（名次从1开始)，请考虑如何在迭代中打印出来。
#
# 提示：考虑使用zip()函数和range()函数


L = ['Adam', 'Lisa', 'Bart', 'Paul']
N = range(1, 5)
Z = zip(N, L)
for index, name in Z:
    print(index, '-', name)

C = {"a": 1, "b": 2}
for key in C:
    print(key, "-", C[key])

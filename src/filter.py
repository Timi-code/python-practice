def is_odd(n):
    return n % 2 == 1


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
c = list(filter(is_odd, l))
print(c)
print(l)


def is_palindrome(n):
    return str(n) == str(n)[::-1]


print(list(filter(is_palindrome, range(1, 1000))))

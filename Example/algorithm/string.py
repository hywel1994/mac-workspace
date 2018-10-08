from string import digits, ascii_uppercase, ascii_lowercase

Alphabet = digits + ascii_lowercase + ascii_uppercase
print(Alphabet)  # "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def ten2any(n, b=62):
    """"""
    assert b <= 62

    n, index = divmod(n, b)  # n = n // b, index = n % b
    if n > 0:
        return ten2any(n, b) + Alphabet[index]
    else:
        return Alphabet[index]

def ten2any_2(n, b=62):
    """"""
    ret = ""
    while n > 0:
        n, index = divmod(n, b)
        ret = Alphabet[index] + ret

    return ret

def any2ten(s, base=62):
    """"""
    n = 0
    for i, c in enumerate(reversed(s)):  # reversed(s)
        index = Alphabet.index(c)
        n += index * pow(base, i)

    return n

a = ten2any(99,16)
print(a)
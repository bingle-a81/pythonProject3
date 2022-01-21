# -*- coding: utf-8 -*-
dec=12340
print(bin(dec))


def count_bits(n):
    return (bin(n).count('1'))

print((count_bits(dec)))
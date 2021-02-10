#!/usr/bin/python3
import math

from decimal import *
from random import randint
from functools import reduce

getcontext().prec=10000


def is_prime(num, test_count):
    if num == 1:
        return False
    if test_count >= num:
        test_count = num - 1
    for x in range(test_count):
        val = randint(1, num - 1)
        if pow(val, num-1, num) != 1:
            return False
    return True


def generate_big_prime(n):
    found_prime = False
    while not found_prime:
        p = randint(2**(n-1), 2**n)
        if is_prime(p, 1000):
            return p


def int_to_bytes(x):
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')


def bytes_to_int(x):
    result = 0
    for b in x:
        result = result * 256 + int(b)
    return result


def chinese_remainder(n, a):
	n = list(map(Decimal, n))
	a = list(map(Decimal, a))

	s = 0
	prod = reduce(lambda a, b: a*b, n)

	for n_i, a_i in zip(n, a):
		p = prod // n_i
		s += a_i * mul_inv(p, n_i) * p
	return s % prod
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def find_invpow(x, n):
    high = 1
    while high ** n < x:
        high *= 2
    low = high // 2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid**n < x:
            low = mid
        elif high > mid and mid**n > x:
            high = mid
        else:
            return mid
    return mid + 1


if __name__ == "__main__":
	e = 3

	N1 = 77020858988154262006946450467675394086338338737520610576961898087902443926950955494784478547853018690013462612815810302372908454818869914879061201 
	N2 = 10602908577525766320675254637503821586208230527554774528812371445512482368765012162393368590739618497747139759482717983472861602801874965841650171
	N3 = 98230837226275538981855961078006434635477826107155606366689337969888359236992457066556534384455590481026337862763006126371396552769737961788144947

	c1 = 46207242172217531038472271629566951205554480830439239312334382929898065847361487683033056905946114941725749778260617316289994070831595099778385423
	c2 = 5584930408594912270629329005935666550287183486281541192686033161148110677577094781856865365303993386488811743535024687523392137796751806309574145
	c3 = 79412263195859437957130560682904074348488555097076785404191718801838128031366136686944105045110357377470310074174452352302290083661047246245542209
	 
	# let's solve it!
	flag_cubed = chinese_remainder([N1, N2, N3], [c1, c2, c3])
	flag = find_invpow(Decimal(flag_cubed), 3)
	 
	print(int_to_bytes(flag))

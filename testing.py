from math import gcd
import math
from math import sqrt
from collections import Counter
import numpy as np
import os
import re


def prime(i, primes):
    for prime in primes:
        if not (i == prime or i % prime):
            return False
    primes.append(i)
    return i


def get_primes(n):
    primes = []
    i, p = 2, 0
    while True:
        if prime(i, primes):
            p += 1
            if p == n:
                return primes
        i += 1


def prime_facs(n):
    step = 1
    i = 2
    if i > 2:
        step = 2
    factors = []
    while i * i <= n:
        if i > largest_factor_prime:
            return False
        if n % i:
            i += step
        else:
            n //= i
            factors.append(i)
    if n > 1 and (n in prime_fac_base):
        factors.append(n)
    else:
        return False
    return factors


def guess_r(a, b):
    nbr = math.floor(sqrt(a*N)) + b
    return nbr


test_N_1 = 323
test_N_2 = 307561
test_N_3 = 31741649
test_N_4 = 3205837387
test_N_5 = 392742364277
real_N = 220744554721994695419563

test_N_hc = 16637

N = 16637

F = 10
L = F + 2

string_to_input = str(L) + " " + str(F) + "\n"

prime_fac_base = get_primes(F)
largest_factor_prime = prime_fac_base[-1]


# rone = guess_r(3, 2)
# rtwo = guess_r(4, 4)
# rthree = guess_r(5, 3)
# rfour = guess_r(5, 4)
# rfive = guess_r(6, 2)
# rsix = guess_r(7, 2)
# rseven = guess_r(10, 6)
# reight = guess_r(11, 4)
# rnine = guess_r(12, 12)
# rten = guess_r(13, 4)
# releven = guess_r(13, 8)
# rtwelve = guess_r(14, 8)
# ad = guess_r(14, 8)
# r_list_test = [rone, rtwo, rthree, rfour, rfive, rsix, rseven, reight, rnine, rten, releven, rtwelve, ad]

saved_r_vals = []
binary_m = set()
sum = 2
index = 0
while len(binary_m) < L:
    for j in range(sum-1, 0, -1):
        if len(binary_m) >= L:
            break
        k = sum - j
        r = guess_r(k, j)
        r_to_save = r
        r = r**2 % N
        if r > 1:
            r_primes = prime_facs(r)
            if r_primes:
                print(r, r_primes)

                # find out count of exponents
                count = dict(Counter(r_primes))
                # print(count)

                # Do binary row:
                binary_row = [0] * len(prime_fac_base)
                for k, v in count.items():
                    if v%2 == 0:
                        binary_row[prime_fac_base.index(k)] = 0
                    else:
                        binary_row[prime_fac_base.index(k)] = 1
                binary_row = tuple(binary_row)
                len_1 = len(binary_m)
                binary_m.add(binary_row)
                len_2 = len(binary_m)
                if len_2 > len_1:
                    # The binary row was added so save (r, r_primes)
                    binary_string = ''
                    for x in binary_row:
                        if len(binary_string) == 0:
                            binary_string = binary_string + str(x)
                        else:
                            binary_string = binary_string + " " + str(x)
                    string_to_input = string_to_input + binary_string + "\n"
                    saved_r_vals.append([index, r_to_save, r_primes, binary_row])
                    index = index + 1
                print(count)
                print(binary_row)
                print(prime_fac_base)

                print(binary_m)
                print(len(binary_m))
                print(saved_r_vals)
                print(string_to_input)
                print("---------------------------------")
        sum = sum + 1

input_file = open("input.txt", "w")
input_file.write(string_to_input)
input_file.close()

path = os.getcwd()
path = path + "/a.out input.txt output.txt"
os.system(path)

with open("output.txt") as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]
lines = lines[1:]
print("lines", len(lines), lines)
for line in lines:
    indexes = []
    line = re.sub(r"\s", "", line)
    print(line)
    for i in range(len(line)):
        if line[i] == "1":
            indexes.append(i)
    print("indexes", indexes)
    # Test solution now


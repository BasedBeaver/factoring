from math import gcd
import math
from math import sqrt
from collections import Counter
from copy import deepcopy
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
    factors = []
    for prime in prime_fac_base:
        if n == 1:
            return factors
        else:
            while not(n % prime):
                n = n // prime
                factors.append(prime)
    if n > 1:
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

N = real_N
F = 1000
L = F + 10

string_to_input = str(L) + " " + str(F) + "\n"

prime_fac_base = get_primes(F)
largest_factor_prime = prime_fac_base[-1]
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
                # Find out count of exponents
                count = dict(Counter(r_primes))
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
                    saved_r_vals.append([index, r_to_save, r_primes])
                    index = index + 1
                # Prints to see progress
                print(index)
                print("---------------------------------")
        sum = sum + 1

input_file = open("input.txt", "w")
input_file.write(string_to_input)
input_file.close()

path = os.getcwd()
path = path + "/a.out input.txt output.txt"
os.system(path)

# Read in solutions
with open("output.txt") as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]
lines = lines[1:]

for line in lines:
    indexes = []
    line = re.sub(r"\s", "", line)
    for i in range(len(line)):
        if line[i] == "1":
            indexes.append(i)
    # Test each solution now
    sum_r = 1
    sum_r_2 = 1
    list_r_2 = []
    for i in indexes:
        sum_r = (sum_r * saved_r_vals[i][1]) % N
        list_r_2.extend(saved_r_vals[i][2])
    list_r_2.sort()
    count_r_2 = dict(Counter(list_r_2))
    copy = deepcopy(count_r_2)
    for k, v in copy.items():
        temp = [k, int(v/2)]
        sum_r_2 = (sum_r_2 * (temp[0]**temp[1])) % N
    fac_1 = gcd(abs(sum_r_2 - sum_r), N)
    if fac_1 != 1 and fac_1 != N:
        fac_2 = int(N/fac_1)
        print("The Factors of " + str(N) + " are " + str(fac_1) + " and " + str(fac_2))
        break
    elif fac_1 == 1:
        print("not lucky")

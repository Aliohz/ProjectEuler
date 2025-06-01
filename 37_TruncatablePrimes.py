# Truncatable Primes
# https://projecteuler.net/problem=37

import math

def is_prime(number):
    if number < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True


def is_truncatable(number):
    if number < 10:
        return False

    n_str = str(number)
    possible_numbers_str = []
    digit_str = ""

    for i in range(len(n_str)):
        possible_numbers_str.append(n_str[i:])

    for digit in n_str:
        digit_str += digit
        if digit_str not in possible_numbers_str:
            possible_numbers_str.append(digit_str)

    for digit in possible_numbers_str:
        n = int(digit)
        if is_prime(n) == False:
            return False
    return True
    

count = 0
i = 0
truncatablePrimes = []

while count < 11:
    i += 1

    if is_truncatable(i):
        truncatablePrimes.append(i)
        count += 1

print(sum(truncatablePrimes))
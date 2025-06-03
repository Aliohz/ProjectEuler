# Self powers
# https://projecteuler.net/problem=48
# 03/06/2025

result = 0

for i in range(1, 1001):
    result += i**i

result = str(result)

print(result[-10:])
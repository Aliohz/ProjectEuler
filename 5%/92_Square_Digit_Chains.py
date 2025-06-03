# Square Digit Chains
# https://projecteuler.net/problem=92
# 03/06/2025


def next_number(number):
    new_number = 0

    for i in map(int, str(number)):
        new_number += i ** 2

    return new_number

def chain(number):
    while True:
        i = next_number(number)

        if i == 89:
            return True
        elif i == 1:
            return False
        else:
            number = i
            

counter = 0
ending89 = []
max_val = 567

for i in range(1,max_val + 1):
    if chain(i):
        ending89.append(i)
        counter += 1

for i in range(max_val+1, 10000000):
    if i % 10000 == 0:
        print(i)
    if next_number(i) in ending89:
        counter += 1

print(counter)
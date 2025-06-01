### Double-base Palindromes
### http://projecteuler.net/problem=36

def is_palindrome(string):
    reverse = string[::-1]
    
    if string == reverse:
        return True
    else:
        return False


def convert_to_binary(number):
    base = 2
    exp = 0
    binary = []
    string = ""

    while number >= base**exp:
        exp += 1
    
    for i in range(exp - 1, -1, -1):
        if (number - base**i) >= 0:
            binary.append(1)
            number -= base**i
        else:
            binary.append(0)

    for position in binary:
        string += str(position)

    return string


palindromes = []

for number in range(1, 1000000):
    
    if is_palindrome(str(number)):
        binary = convert_to_binary(number)
        if is_palindrome(binary):
            palindromes.append(number)

print(sum(palindromes))
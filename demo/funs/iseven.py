def iseven(num):
    return num % 2 == 0

def isprime(num):
    for n in range(2, num//2 + 1):
        if num % n == 0:
            return False # not prime

    return True # prime


print(iseven(10), iseven(11))
print(isprime(19), isprime(21))

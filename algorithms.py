# def eratosthenes_sieve(n):
#     digits = [i for i in range(0, n + 1)]
#
#     for i in digits[2:]:
#         if i:
#             for j in digits[i + 1:]:
#                 if j:
#                     if j % i == 0:
#                         digits[j] = 0
#     digits = [i for i in digits[2:] if i]
#     return digits


# Euclidean algorithm

def euclidean(a, b):
    if not a % b:
        return b
    else:
        return euclidean(b, a % b)


print(euclidean(24, 16))


# eratosthenes_sieve

def eratosthenes_sieve(n):
    digits = [i for i in range(0, n + 1)]
    for i in digits[2:]:
        if i:
            for j in digits[i + 1:]:
                if j:
                    if not j % i:
                        digits[j] = 0
    digits = [i for i in digits[2:] if i]
    return digits


print(eratosthenes_sieve(25))

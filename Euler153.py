import time

N = round(1e8)

def main():

    t = time.time()
    count = 0

    count += integer_divisors_leq_n(N)

    # Two because the sum is twice the real part
    count += 2 * repeated_complex_leq_n(N)

    # Two because each real and imaginary appear twice
    count += 2 * other_leq_n(N)

    total_time = time.time() - t
    print('Total sum below %d is %d, took %.2f seconds' % (N, count, total_time))


def integer_divisors_leq_n(n):

    return calc_divisors(n)

def repeated_complex_leq_n(n):

    return calc_divisors(n // 2)

def other_leq_n(n):

    valid_pairs = rel_prime_pairs(n)

    square_dict = {(a, b): a ** 2 + b ** 2 for (a, b) in valid_pairs}

    divisor_dict = {s: calc_divisors(n // s) for s in square_dict.values()}

    count = 0

    return sum([(p[0] + p[1]) * divisor_dict[square_dict[p]] for p in valid_pairs])


def gcd(a, b):
    if a > b:
        return gcd(b, a)
    if a == 0:
        return b
    return gcd(b % a, a)

def is_rel_prime(a, b):

    return gcd(a, b) == 1

def rel_prime_pairs(n):

    pairs = []
    cap = round(n ** .5)

    for i in range(1, cap):
        j = i + 1

        while i**2 + j ** 2 <= n:

            if is_rel_prime(i, j):
                pairs.append((i, j))

            j += 1

    return pairs

def calc_divisors(n):

    count = 0
    for i in range(1, n+1):

        count += i*(n // i)

    return count

if __name__=='__main__':
    main()

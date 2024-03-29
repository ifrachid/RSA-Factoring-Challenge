#!/usr/bin/python3
import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollards_rho(n):
    x = 2
    y = 2
    d = 1

    f = lambda x: (x**2 + 1) % n

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)

    return d

def factorize_rsa(n):
    factors = []
    while n > 1:
        factor = pollards_rho(n)
        factors.append(factor)
        n //= factor

    return factors

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <file>".format(sys.argv[0]))
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        for line in file:
            n = int(line.strip())
            factors = factorize_rsa(n)
            print("{}={}".format(n, "*".join(map(str, factors))))

if __name__ == "__main__":
    main()

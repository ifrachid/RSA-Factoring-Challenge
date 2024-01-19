import sys

def factorize_number(n):
    # Find the factors of n
    factors = []
    for i in range(2, n//2 + 1):
        if n % i == 0:
            factors.append((i, n//i))
    return factors

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <file>".format(sys.argv[0]))
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        for line in file:
            number = int(line.strip())
            factorizations = factorize_number(number)
            for factorization in factorizations:
                print("{}={}*{}".format(number, factorization[0], factorization[1]))

if __name__ == "__main__":
    main()

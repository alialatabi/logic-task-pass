
def prime(n):
    if n > 1:
        out = list()
        sieve = [True] * (n+1)
        for p in range(2, n+1):
            if (sieve[p]):
                out.append(p)
                for i in range(p, n+1, p):
                    sieve[i] = False
        return out
    return('1 is not a prime number')


if __name__ == "__main__":
    num = int(input('Enter a Number: '))
    print(prime(num))

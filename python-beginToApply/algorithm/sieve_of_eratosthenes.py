def eratosthenes(n):
    tf_list = [1] * (n + 1)
    threshold = n ** 0.5
    prime = 2
    while prime <= threshold:
        if tf_list[prime] != 0:
            for i in range(n+1):
                if i != prime and i % prime == 0:
                    tf_list[i] = 0
        prime += 1
    primes = [index for index, ele in enumerate(tf_list) if ele == 1]
    primes.pop(0)
    return primes

def main():
    primes = eratosthenes(10000)
    print(primes)

if __name__ == "__main__":
    main()
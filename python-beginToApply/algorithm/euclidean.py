import random

def euclidean(a, b):
    remain = a % b
    while remain != 0:
        a, b = b, remain
        remain = a % b
    return b

def main():
    n = random.randint(2, 1000)
    m = random.randint(2, 1000)
    max_divisor = euclidean(n, m)
    print('what number is max divisor of {} and {}?'.format(n, m))
    print('max divisor is {}'.format(max_divisor))

if __name__ == "__main__":
    main()
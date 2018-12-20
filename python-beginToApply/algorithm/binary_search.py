import random

def binary_search(data, obj):
    head = 0
    tail = len(data)
    center = (head + tail) // 2
    while head <= tail:
        if obj == data[center]:
            print('リストの', center, '番目', sep='')
            return
        elif obj > data[center]:
            head = center + 1
            center = (head + tail) // 2
        else:
            tail = center - 1
            center = (head + tail) // 2
    print('not found')

def main():
    data = random.sample(range(10000), 5000)
    data.sort()
    obj = int(input())
    binary_search(data, obj)

if __name__ == "__main__":
    main()
import random

def selection_sort(data):
    first_index = 0
    while first_index < len(data):
        # initialize minimum value
        now_min = len(data) + 1
        # iterate unsorted part
        for num in data[first_index:]:
            if now_min > num:
                now_min = num
        # get index of minimum value
        i = data.index(now_min)
        # switch index with head of unsorted part
        data[first_index], data[i] = data[i], data[first_index]
        first_index += 1
    return data


def main():
    data = random.sample(range(0, 1000), 100)
    print(data)
    print(selection_sort(data))


if __name__ == "__main__":
    main()
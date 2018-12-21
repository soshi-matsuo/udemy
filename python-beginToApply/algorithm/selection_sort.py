import random

def selection_sort(data):
    first_index = 0
    while first_index < len(data):
        now_min = len(data) + 1
        for num in data[first_index:]:
            if now_min > num:
                now_min = num
        i = data.index(now_min)
        data[first_index], data[i] = data[i], data[first_index]
        first_index += 1
    return data


def main():
    data = random.sample(range(0, 1000), 100)
    print(data)
    print(selection_sort(data))


if __name__ == "__main__":
    main()
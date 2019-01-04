import random


def bubble_sort(data):
    tail_index = len(data) - 1
    while tail_index > 0:
        i = 0
        while i < tail_index:
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
            i += 1
        tail_index -= 1
    return data

def main():
    chaos_data = random.sample(range(1000), 100)
    print(chaos_data)
    sorted_data = bubble_sort(chaos_data)
    print(sorted_data)

if __name__ == "__main__":
    main()

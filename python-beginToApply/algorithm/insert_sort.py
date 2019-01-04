import random


def insert_sort(data):
    unsorted_index = 1
    while unsorted_index < len(data):
        insert_index = unsorted_index
        x = data.pop(unsorted_index)
        # search list backward for location to insert x
        while insert_index > 0 and data[insert_index-1] > x:
            insert_index -= 1
        # when the number that is smaller than x is found, x is inserted behind it
        data.insert(insert_index, x)
        unsorted_index += 1
    return data

def main():
    chaos_data = random.sample(range(1000), 100)
    print(chaos_data)
    sorted_data = insert_sort(chaos_data)
    print(sorted_data)

if __name__ == "__main__":
    main()
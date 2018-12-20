def linear_search(data, obj):
    for i, num in enumerate(data):
        if num == obj:
            print('リストの{}番目'.format(i))
            return
    print('入力値はありません')

def main():
    data = range(0, 10000, 3)
    obj = int(input())
    linear_search(data, obj)

if __name__ == '__main__':
    main()
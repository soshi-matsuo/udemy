import random

def store(data, leng=150):
    box = [0] * leng
    for num in data:
        hashed = num % leng
        while box[hashed] != 0:
            hashed = (hashed + 1) % leng
        if box[hashed] == 0:
            box[hashed] = num
    return box

def search(stored_box, num, leng=150):
    hashed = num % leng
    if stored_box[hashed] != 0:
        while stored_box[hashed] != num:
            hashed = (hashed + 1) % leng
            if stored_box[hashed] == 0:
                return '配列の中に目的の数字はありません'
        if stored_box[hashed] == num:
            return '配列の{}個目の要素'.format(hashed)
    else:
        return '配列の中に目的の数字はありません'

def main():
    numbers = 100
    data = random.sample(range(1, 200), numbers)
    box = store(data)
    print(box)
    obj = int(input('探す数字を入力：'))
    result = search(box, obj)
    print(result)

if __name__ == "__main__":
    main()
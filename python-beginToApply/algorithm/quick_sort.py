import random
import sys
import statistics

# def quick_sort(data, head, tail):
#     l_scanner = head
#     r_scanner = tail
#     pivot = statistics.median(data[head:tail+1])
#     while l_scanner < r_scanner:
#         # iterate to find index of number more than head
#         while data[l_scanner] < pivot and l_scanner < tail:
#             l_scanner += 1
#         # iterate to find index of number less than head
#         while data[r_scanner] >= pivot and r_scanner >= head:
#             r_scanner -= 1
#         # switch location of them
#         if l_scanner < r_scanner:
#             data[l_scanner], data[r_scanner] = data[r_scanner], data[l_scanner]

#     if head < r_scanner - 1:
#         data = quick_sort(data, head, r_scanner)
#     if r_scanner + 1 < tail:
#         data = quick_sort(data, r_scanner+1, tail)

#     return data

def quick_sort(arr):
    left = []
    right = []
    # 再帰の過程でarr <= 1になるのは、leftまたはrightの要素数が1以下の時
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)
    piv_count = 0
    # 配列内からピボットより小さいものをleft, 大きいものをright, 同値の回数をpivot_countに入れる
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            piv_count += 1
    # left, rightに分けたそれぞれに対して、再帰的にクイックソートする
    left = quick_sort(left)
    right = quick_sort(right)
    return left + [pivot] * piv_count + right


def main():
    sys.setrecursionlimit(10000)
    # print(sys.getrecursionlimit())
    chaos = [random.randint(0, 20) for i in range(10)]
    sorted_data = quick_sort(chaos)
    print(sorted_data)

if __name__ == "__main__":
    main()
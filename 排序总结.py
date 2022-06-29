import random

li = list(range(20))
random.shuffle(li)
print(li)


def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right:
            if li[right] >= tmp:
                right -= 1
        li[left] = li[right]
        while left < right:
            if li[left] <= tmp:
                left += 1
        li[right] = li[left]
    li[left] = tmp
    return left
    pass


def bubble_sort(li):
    n = len(li)
    exchange = False
    for i in range(n - 1):
        for j in range(n - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        if not exchange:
            return li


def select_sort(li):
    n = len(li)
    for i in range(n - 1):
        min_loc = i
        for j in range(i + 1, n):
            if li[min_loc] > li[j]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]
    pass


def insert_sort(li):
    n = len(li)
    for i in range(1, n):
        tmp = li[i]
        for j in range(i - 1, -1, -1):
            if li[j] > tmp:
                li[j + 1], li[j] = li[j], li[j + 1]
    pass


def quick_sort(li, left, right):
    mid = partition(li, left, right)
    quick_sort(li, left, mid - 1)
    quick_sort(li, mid + 1, right)
    pass


bubble_sort(li)
print('bubble sort result')
print(li)

random.shuffle(li)
select_sort(li)
print('select sort result')
print(li)

random.shuffle(li)
insert_sort(li)
print('insert sort result')
print(li)

random.shuffle(li)
quick_sort(li, 0, len(li) - 1)
print('quick sort result')
print(li)
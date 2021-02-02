arr = [3,6,7,1,2,4]
n = len(arr)

for i in range(1<<n):       # a << n = a * (2의 n승)    # arr 의 부분집합 개수
    # print(i)
    for j in range(n):
        if i & (1<<j):
            print(arr[j], end=' ')
    print()




def search1(a, key):
    n = len(a)
    i = 0
    while i < n and a[i] != key:
        i += 1

    if i < n:
        return i
    else:
        return None

a_li = [2,4,7,9,11,14]
print(search1(a_li,11))
print(search1(a_li,10))

def search2(a, key):
    n = len(a)
    b = sorted(a)
    i = 0
    while b[i] < key:
        i += 1
        if i < n:
            if b[i] == key:
                return i
            elif b[i] > key:
                return None
        else:
            print("Out of range")

a_li2 = [4,6,2,7,9,11]

print(search2(a_li2,9))
print(search2(a_li2,10))

def binary_search(li, key):
    n = len(li)
    low, high = li[0], li[n - 1]
    pivot = (low + high) // 2
    while key != pivot:
        if key < pivot:
            pivot = (low + pivot) // 2
        else:
            pivot = (pivot + high) // 2
    if key == pivot:
        return True


Li = [1, 2, 3, 4, 5, 6, 7]
print(binary_search(Li, 6))

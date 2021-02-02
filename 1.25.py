def quicksort(li):
    if len(li) <= 1:
        return li
    pivot = li[len(li)//2]
    first_li, equal_li, last_li = [], [], []
    for i in li:
        if i < pivot:
            first_li.append(i)
        elif i > pivot:
            last_li.append(i)
        else:
            equal_li.append(i)
    return quicksort(first_li) + equal_li + quicksort(last_li)

x = [6,11,29,3,15,9,32,23,6,29]
print(quicksort(x))


Data = list(map(int, input("입력하세요:").split()))
cnt_list = [0] * 12

for i in range(len(Data)):
    cnt_list[Data[i]] += 1
print(cnt_list)


def bubblesort():
    a = [7,42,12,76,54]
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

print(bubblesort())

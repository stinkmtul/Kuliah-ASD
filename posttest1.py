from random import randint
import os, time

def clear():
    os.system('cls')
    time.sleep(1)

def mergeSort(a):
    if len(a) <= 1:
        return a
    else :
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]

        left = mergeSort(left)
        right = mergeSort(right)

        return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else :
            result.append(right[j])
            j += 1
    
    result += left[i:]
    result += right[j:]
    return result

a = []
for i in range(20):
    listacak = randint(0, 30)
    a.append(listacak)

clear()
result = mergeSort(a)
print("MERGE SORT")
print(f"List acak tidak terurut : {a}")
print(f"List sudah terurut : {result}")
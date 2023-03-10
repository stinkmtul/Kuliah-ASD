from prettytable import PrettyTable

import os
os.system('cls')

table = PrettyTable()
table.field_names = ["No", "Nama Aslab"]

def tampil():
    table.clear_rows()

    no = 1
    for y in range(len(arr2)):
        table.add_row([no, arr2[y]])
        no += 1
    print(table)

def fib(n): 
    if n < 1 :
        return 0
    elif n == 1 :
        return 1
    else:
        return fib(n-1) + fib(n-2)

def Fibonaccisearch(arr,x): 
    n = 0 
    while fib(n) < len(arr):
        n = n + 1 
    offset = -1
    while (fib(n) > 1):
        i = min(offset + fib(n-2), len(arr) - 1)
        if (x > arr[i]):
            n = n -1 
            offset = i
        elif (x < arr[i]):
            n = n - 2
        else :
            return i 
    if(fib(n-1) and arr[offset + 1] == x):
        return offset + 1
    return -1

def searchnested(x):
    for i in range(len(arr)):
        c = arr[i]
        if type(c) == list:
            searchrow = Fibonaccisearch(c, x)
            if searchrow != -1:
                print(f"\n{x} berada diindex {i} kolom {searchrow}\n")
            else :
                if c == x:
                    print(f"\n{x} berada diindex {i}\n")
        else :
            if c == x:
                print(f"\n{x} berada diindex {i}\n")

arr = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"], "Aslab"]
arr2 = []

for z in arr:
    if (isinstance(z,list)):
        for b in z:
            arr2.append(b)
    else:
        arr2.append(z)

tampil()
x = input("\nMasukan nama aslab yang ingin dicari : ").capitalize()
if x in arr2 :
    searchnested(x)
else :
    print("\nNama tidak terdaftar\n")

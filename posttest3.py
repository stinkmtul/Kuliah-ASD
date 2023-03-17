import os, time
from prettytable import PrettyTable
from datetime import datetime as dt

daftarapk = ["Whatsapp", "Gojek", "Instagram", "Tiktok", "Telegram", "Google", "Youtube"]

datamasuk = []

datakeluar = {
    "nama" : [],
    "masuk" : [],
    "keluar" : []
}

tablee = PrettyTable()
tablee.field_names = ["No", "Nama Aplikasi", "Waktu (data masuk)", "Waktu (selesai update)"]

table = PrettyTable()
table.field_names = ["No", "Update Tersedia"]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Aplikasi():
    def __init__(self):
        self.head = None
    
    def tampilapk(self):
        if self.head is None:
            print("")
        else:
            x = self.head
            while x is not None:
                print(x.data)
                x = x.next

    def tambahakhir(self, data):
        nodebaru = Node(data)
        if self.head is None:
            self.head = nodebaru
        else:
            x = self.head
            while x.next is not None:
                x = x.next
            x.next = nodebaru

    def hapusawal(self):
        if self.head is None:
            print("Daftar kosong")
        else:
            self.head = self.head.next

linkedlist = Aplikasi()
linkedlist.tampilapk()

def clear():
    os.system("cls")

j = []
l = len(j)
def waktu():
    clear()
    dn = 5
    while dn :
        detik = dn
        print("\t sedang mengupdate aplikasi... {", detik, "detik }", end="\r")
        time.sleep(1)
        dn -= 1
        j.append(0)

def update():
    time.sleep(2)
    if len(j) <= len(datamasuk):
        if datamasuk not in datakeluar['nama']:
            for i in range(len(datamasuk)):
                datakeluar["nama"].append(datamasuk[i])
                wkt = str(dt.now())[11:19]
                datakeluar["keluar"].append(wkt)
                waktu()
                linkedlist.hapusawal()
                clear()
                linkedlist.tampilapk()
                tampill()
        else :
            clear()
            print("Kesalahan sistem")
    else:
        clear()
        print("Kesalahan sistem")

def tampill():
    tablee.clear_rows()
    no = 1
    for i in range(len(datakeluar["nama"])):
        tablee.add_row([no, datakeluar.get("nama")[i], datakeluar.get("masuk")[i], datakeluar.get("keluar")[i]])
        no += 1
    print(len(datamasuk), "aplikasi berhasil di update\n")
    print("Daftar Riwayat Update")
    print(tablee)

def tampil():
    table.clear_rows()
    no = 1
    for y in range(len(daftarapk)):
        table.add_row([no, daftarapk[y]])
        no += 1
    print(table)

def menu():
    clear()
    w =[]
    o = len(daftarapk)
    while len(w) < o:
        tampil()
        inputuser = input("Masukan nama aplikasi yang ingin anda update : ").capitalize()
        
        if inputuser in daftarapk:
            if inputuser not in datamasuk:
                linkedlist.tambahakhir(inputuser)
                clear()
                time.sleep(1)
                print("satu aplikasi ditambahkan ke antrian list\n")
                print("-- Riwayat data masuk --")
                linkedlist.tampilapk()
                w.append(1)
                wktt = str(dt.now())[11:19]
                datamasuk.append(inputuser)
                datakeluar["masuk"].append(wktt)
                
                if len(w) < o:
                    time.sleep(1)
                    a2 = input("\nApakah ingin menambah daftar list update aplikasi (y/t) : ")

                    if a2 == "y":
                        clear()
                    elif a2 == "t":
                        clear()
                        time.sleep(1)
                        print(len(datamasuk), "aplikasi akan diupdate")
                        print("\nMemuat...")
                        update()
                        break
                    else :
                        clear()
                        time.sleep(1)
                        print("Mohon masukan inputan benar!\n")

                else :
                    clear()
                    print("\nAplikasi dalam daftar telah dipilih semua")
                    time.sleep(1)
                    print("\nMemuat...")
                    update()
                    break

            else :
                clear()
                time.sleep(1)
                print(f"{inputuser} telah ditambahkan didalam daftar list\n")
                time.sleep(1)
                print("-- Riwayat data masuk --")
                linkedlist.tampilapk()
                print("\n")
        
        else :
            time.sleep(1)
            clear()
            print("Aplikasi tidak ada didaftar Update tersedia!\n")
menu()
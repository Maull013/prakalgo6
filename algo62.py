# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 20:57:23 2023

@Maull: TUF GAMING
"""

def input_bulan():
    while True:
        month = int(input("masukkan bulan (1-12): "))
        if month in range(1, 13):
            return month
        else:
            print("* salah memasukkan nilai bulan: ", month, "* ")
            
def menentukan_hari_dlm_bulan(month):
    if month == 0:
        return "Terima kasih sudah menggunakkan program saya. samapi jumpa lagi. "
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return "ada 31 hari dalam bulan"
    elif month in [4, 6, 9, 11]:
        return "ada 30 hari dalam bulan"
    elif month == 2:
        year = int(input("memasukkan tahun (misalnya, 2023): "))
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return "ada 29 hari dalam bulan"
        else:
            return "ada 28 hari dalam bulan"
        
        
bosan = False
print("program ini akan menentukan jumlah hari dalam bulan tertentu")
while not bosan:
    print("Masukkan 0 untuk menghentikan program")
    month = input_bulan()
    result = menentukan_hari_dlm_bulan(month)
    print(result)
    if month == 0:
        bosan = True
        
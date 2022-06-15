#Bagian ilham : main.py
#Bagian Farid : Bank.py, customer.py
import sys
from customer import Customer
from Bank import Bank

s = Bank()
atm = Customer(id)
while True:

    id = int(input("Masukan Pin Anda :"))
    trial = 0

    while (id != int(atm.checkPin()) and trial < 3):
        id = int(input("Pin anda salah. Silahkan Masukan Lagi : "))
        trial += 1

        if trial == 3:
            print("Error. Silahkan ambil kartu dan coba lagi..")
            exit()
    while True:
        
        try:
            print("""
            ********************
            Menu:
            1. cek saldo
            2. Deposit
            3. Penarikan
            4. Keluar
            ********************
            """) 
            option = int(input("Enter 1, 2, 3, 4: "))
        except:

            print("Error: Enter 1, 2, 3, 4 only!\n")
            continue
        else:
            if option == 1:
                s.cekSaldo()
                input("Ketik enter untuk kembali ke menu : ")
            elif option == 2:
                s.deposit()
                input("Ketik enter untuk kembali ke menu : ")
            elif option == 3:
                s.withdraw()
                input("Ketik enter untuk kembali ke menu : ")
            elif option == 4:
                print("Terima kasih telah menggunakan layanan kami")
                sys.exit()
            else:
                print("Keyword yang anda masukkan tidak ada di menu")
                input("Ketik enter untuk kembali ke menu : ")





        

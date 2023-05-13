from colorama import Fore, Style

print(Fore.RED + Style.BRIGHT + "Konversi Jam ke Menit dengan Python" + Style.RESET_ALL)

x = int(input("Masukkan Angka: "))

y = x * 60 #1 Jam = 60 Menit

print("Hasil nya:",y, "Menit")

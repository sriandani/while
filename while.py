number = int(input("Masukkan sebuah bilangan (masukkan -1 untuk keluar): "))

while number != -1:
    if number % 2 == 0:
        print(f"{number} adalah bilangan genap.")
    else:
        print(f"{number} adalah bilangan ganjil.")
    
    number = int(input("Masukkan sebuah bilangan (masukkan -1 untuk keluar): "))

print("Selesai.")

print("="*10, "Kalukulator Sederhana", "="*10)

while True:
    try:
        num_1 = float(input("Masukkan angka pertama: "))
        num_2 = float(input("Masukkan angka kedua: "))
        operasi = input("Masukkan operasi matematika (+,-,*,/), atau q untuk keluar: ")

        if operasi == "+":
            print(f"Hasil: {num_1} + {num_2} = {num_1 + num_2}")
        elif operasi == "-":
            print(f"Hasil: {num_1} - {num_2} = {num_1 - num_2}")
        elif operasi == "*":
            print(f"Hasil: {num_1} * {num_2} = {num_1 * num_2}")
        elif operasi == "/":
            if num_2 != 0:
                print(f"Hasil: {num_1} / {num_2} = {num_1 / num_2}")
            else:
                print("⚠️ Tidak bisa dibagi dengan nol.")
        elif operasi.lower() == "q":
            print("Terima kasih telah menggunakan kalkulator 🙌")
            break
        else:
            print("⚠️ Operasi tidak valid, gunakan +, -, *, atau /")
    except ValueError:
        print("⚠️ Input harus berupa angka!")

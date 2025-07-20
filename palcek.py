print(f'''
    ▜     ▌ 
▛▌▀▌▐ ▛▘█▌▙▘
▙▌█▌▐▖▙▖▙▖▛▖
▌ palindrom checker with python language.           
''')

wordInput = input("Masukan kata: ") # USER MEMASUKAN INPUT UNTUK VAR wordInput

def palchecker(word): # fungsi palchecker dibuat dengan parameter WORD
    word = word.lower() # memastikan bahwa inputan low semua atau kecil semua karakternya
    return word == word[::-1] # kembalikan nilai true apabila karakter sebelumnya sama dengan karakter yang sudah di cek, misal: K A T A K, dari belakang atau -1: K A T A K 

if palchecker(wordInput): # jika 
    print(f"{wordInput} adalah palindrom")
else:
    print(f"{wordInput} bukan palindrom")


# Penjelasannya:

#     palchecker adalah fungsi yang menerima satu parameter yaitu word (kata yang akan dicek).

#     word.lower() mengubah semua huruf menjadi huruf kecil, agar pengecekan tidak peduli huruf besar/kecil.

#     word[::-1] membalik urutan huruf.
#     Misalnya: "katak" → dibalik jadi "katak", tetap sama.
#     Tapi "Buku" → dibalik "ukuB", beda.

#     Fungsi akan mengembalikan nilai True jika kata tersebut sama dengan versi terbaliknya → artinya itu palindrom.
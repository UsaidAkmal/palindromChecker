print(f'''
    ▜     ▌ 
▛▌▀▌▐ ▛▘█▌▙▘
▙▌█▌▐▖▙▖▙▖▛▖
▌ palindrom checker with python language.           
''')

def palchecker(word):
    word = kata.lower()
    return word == word[::-1] 

userWordInput = input("Masukan kata: ")

if palchecker(userWordInput):
    print(f"{userWordInput} adalah palindrom")
else:
    print(f"{userWordInput} bukan palindrom")
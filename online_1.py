# s = " 1,2,3,4,5,6,7,8,10,9"
# first_number = s.startswith(" 1")
# print(first_number)
# s = s.strip()
# print(s)
# s = s[0:3]
# print(s)


# vstup  = "C++ je [kolkokrat] KRÁT lepší! "
# vstup_bez_medzier = vstup.strip()
# print(vstup_bez_medzier)
# vstup_malymi = vstup.lower()
# print(vstup_malymi)
# nahrada = vstup.replace("C++","Python")
# print(nahrada)
# print(nahrada.startswith("Python"))
# pocet = len(vstup)
# vstup = nahrada.replace ("[kolkokrat]", str((pocet * 3)))
# print(vstup)


# a = int(input("zadaj prve cislo"))
# b = int(input("zadaj druhe cislo"))
# if a == b:
#     print("su rovne")
# elif a > b:
#     print("prve je vacsie")
# else:
#     print("druhe je vacsie")



# print("Malá násobilka pomocou dvoch cyklov:")
# for j in range(1, 11):
#     for i in range(1, 11):
#         print(f"{i * j}\t", end="")
#     print()
#
# for repeat in range(3):
#     print("halo")
# print()
#
# for numbers in range(1,11):
#     print(numbers)
#
# for numbers in range(10,0,-1):
#     print(numbers)
#
# for mriezka in range(10):
#     for medzera in range(10):
#         print("#" + " ", end="")
#     print()

# s = "1,2,3,4,5,6,7,8,9,10"
# a = [int(s) for s in s.split(",")]
# print(a)
# tyzden = ["pondelok", "utorok", "streda", "stvrtok", "piatok", "sobota", "nedela"]
# den = int(input("zadaj cislo dna v tyzdni "))
# print(tyzden[den-1])
# print()
#
# text = "karol"
# text_zoznam = [str(s) for s in text]
# text_zoznam.reverse()
# for znak in text_zoznam:
#     print(znak, end="")
# print()
#
# text = "30. nar 1.1.2020"
# for i in text:

# text_zoznam = [str(s) for s in text]
# print(text_zoznam)
# zoznam_cisla = []
# zoznam_znaky = []
# for znak in text_zoznam:
#     if znak.isnumeric():
#         zoznam_cisla.append(int(znak))
#     else:
#         zoznam_znaky.append(znak)
# print(sum(zoznam_cisla))


# Sčitanie dvoch čísel
a = 5
b = 3
sucet = a + b
print("Súčet:", sucet)  # Výstup: Súčet: 8

# Odčítanie dvoch čísel
rozdiel = a - b
print("Rozdiel:", rozdiel)  # Výstup: Rozdiel: 2

# Násobenie dvoch čísel
sucin = a * b
print("Súčin:", sucin)  # Výstup: Súčin: 15

# Delenie dvoch čísel
podiel = a / b
print("Podiel:", podiel)  # Výstup: Podiel: 1.6666666666666667

# Celé delenie dvoch čísel
celociselne_delenie = a // b
print("Celé delenie:", celociselne_delenie)  # Výstup: Celé delenie: 1

# Zvyšok po delení dvoch čísel
zvysok = a % b
print("Zvyšok:", zvysok)  # Výstup: Zvyšok: 2

# Mocnenie čísla
mocnina = a ** b
print("Mocnina:", mocnina)  # Výstup: Mocnina: 125

# Zápis do súboru
with open("aritmeticke_operatory.txt", "w", encoding="utf-8") as file:
    file.write(f"Súčet: {sucet}\n")
    file.write(f"Rozdiel: {rozdiel}\n")
    file.write(f"Súčin: {sucin}\n")
    file.write(f"Podiel: {podiel}\n")
    file.write(f"Celé delenie: {celociselne_delenie}\n")
    file.write(f"Zvyšok: {zvysok}\n")
    file.write(f"Mocnina: {mocnina}\n")
# Kód bol úspešne spustený a výsledky boli uložené do súboru aritmeticke_operatory.txt
print("Výsledky boli uložené do súboru aritmeticke_operatory.txt")






# # Rodičovská třída
# class Zvire:
#     def __init__(self, jmeno):
#         self.jmeno = jmeno
#
#     def zvuk(self):
#         return "Neznámý zvuk"
#
# # Podtřída Pes, která dědí ze Zvire
# class Pes(Zvire):
#     def zvuk(self):
#         return "Haf haf!"
#
# # Podtřída Kocka, která dědí ze Zvire
# class Kocka(Zvire):
#     def zvuk(self):
#         return "Mňau!"
#
# # Použití
# zvire1 = Pes("Rex")
# zvire2 = Kocka("Micka")
#
# print(f"{zvire1.jmeno} říká: {zvire1.zvuk()}")
# print(f"{zvire2.jmeno} říká: {zvire2.zvuk()}")
#
# jmeno = input("Zadej své jméno: ")
# if len(jmeno) == 0:
#     print("nezadal si ziadny znak")
#     exit()
# else:
#     if 3 <= len(jmeno) <= 10:
#         print("Normální jméno")
#     else:
#         print("Máš moc krátké nebo moc dlouhé jméno!")

from decimal import Decimal
def sucet (a:float, b:float):
    result_sucet = a + b
    print("Vysledok je ", result_sucet)
def rozdiel (a:float, b:float):
    result_rozdiel = a - b
    print("Vysledok je ", result_rozdiel)
def sucin (a:float, b:float):
    result_sucin = a * b
    print("Vysledok je ", result_sucin)
def podiel (a:float, b:float):
    result_podiel = float(a / b)
    print("Vysledok je", result_podiel)

print("VITAJTE V KALKULACKE")
print("zadaj prve cislo")
a = float(input())
print("zadaj druhe cislo")
b = float(input())
print("Zvol operaciu" + "+" + "-" + "*" + "/")
q = input()
if q == "+":
    (sucet(a, b))
elif q == "-":
    rozdiel(a, b)
elif q == "*":
    sucin(a, b)
elif q == "/":
    rozdiel(a, b)


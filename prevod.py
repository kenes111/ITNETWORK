def prevod(cislo, sustava):
    """Prevod čísla zo sústavy desiatkovej do ľubovoľnej sústavy (2-36)."""
    if sustava < 2 or sustava > 36:
        raise ValueError("Sústava musí byť medzi 2 a 36")

    znaky = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    vysledok = ""

    # špeciálny prípad pre 0
    if cislo == 0:
        return "0"

    while cislo > 0:
        zvysok = cislo % sustava
        vysledok = znaky[zvysok] + vysledok
        cislo //= sustava

    return vysledok


# --- Hlavná časť programu ---
dec_cislo = int(input("Zadaj číslo v desiatkovej sústave: "))
zaklad = int(input("Zadaj základ cieľovej sústavy (2-36): "))

print(f"Číslo {dec_cislo} v sústave {zaklad} je: {prevod(dec_cislo, zaklad)}")










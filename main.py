import random

MAX_CHYB = 6
SLOVA = [
    "programovani", "kompilator", "pocitac", "klavesnice", "monitor",
    "debugovani", "internet", "protokol", "server", "sit", "autobus", "mikrovlnka"
]

def vyber_nahodne_slovo():
    return random.choice(SLOVA)

def zobraz_stav(tajne_slovo, uhodnuta_pismena):
    stav = ""
    for pismeno in tajne_slovo:
        if pismeno in uhodnuta_pismena:
            stav += pismeno + " "
        else:
            stav += "_ "
    print("Slovo:", stav.strip())

def kontrola_vyhry(tajne_slovo, uhodnuta_pismena):
    return all(p in uhodnuta_pismena for p in tajne_slovo)

def zpracuj_vstup(pismeno, tajne_slovo, uhodnuta_pismena):
    if pismeno in tajne_slovo:
        uhodnuta_pismena.add(pismeno)
        return True
    return False

def hraj_hru():
    tajne_slovo = vyber_nahodne_slovo()
    uhodnuta_pismena = set()
    chybne_pokusy = 0

    print("=== Vítej ve hře Hádání slova ===")
    print(f"Hádej slovo! Máš {MAX_CHYB} pokusů.\n")

    while chybne_pokusy < MAX_CHYB:
        zobraz_stav(tajne_slovo, uhodnuta_pismena)
        pismeno = input("Zadej písmeno: ").lower()

        if len(pismeno) != 1 or not pismeno.isalpha():
            print("Zadej prosím jedno písmeno.\n")
            continue

        if pismeno in uhodnuta_pismena:
            print("Toto písmeno už jsi zkusil(a).\n")
            continue

        if zpracuj_vstup(pismeno, tajne_slovo, uhodnuta_pismena):
            print("Správně!\n")
        else:
            chybne_pokusy += 1
            print("Špatně! Počet chyb:", chybne_pokusy, "\n")

        if kontrola_vyhry(tajne_slovo, uhodnuta_pismena):
            print(f"Gratulace! Uhodl(a) jsi slovo: {tajne_slovo}\n")
            break
    else:
        print(f"Prohrál(a) jsi! Tajné slovo bylo: {tajne_slovo}\n")

def main():
    while True:
        hraj_hru()
        znovu = input("Chceš hrát znovu? (a/n): ").lower()
        if znovu != 'a':
            print("Díky za hru! 👋")
            break

if __name__ == "__main__":
    main()

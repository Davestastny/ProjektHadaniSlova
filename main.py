import random  # Načtení knihovny pro generování náhodných hodnot

# Maximální počet chyb, než hráč prohraje
MAX_CHYB = 6

# Seznam slov, ze kterých se vybírá náhodné slovo pro hru
SLOVA = [
    "programovani", "kompilator", "pocitac", "klavesnice", "monitor",
    "debugovani", "internet", "protokol", "server", "sit", "autobus", "mikrovlnka"
]

# Vybere náhodné slovo ze seznamu SLOVA
def vyber_nahodne_slovo():
    return random.choice(SLOVA)

# Zobrazí aktuální stav slova – písmena, která hráč uhodl, a ostatní jako "_"
def zobraz_stav(tajne_slovo, uhodnuta_pismena):
    stav = ""
    for pismeno in tajne_slovo:
        if pismeno in uhodnuta_pismena:
            stav += pismeno + " "
        else:
            stav += "_ "
    print("Slovo:", stav.strip())

# Zkontroluje, jestli hráč uhodl všechna písmena slova
def kontrola_vyhry(tajne_slovo, uhodnuta_pismena):
    return all(p in uhodnuta_pismena for p in tajne_slovo)

# Zpracuje zadané písmeno – pokud je ve slově, přidá ho mezi uhodnutá
def zpracuj_vstup(pismeno, tajne_slovo, uhodnuta_pismena):
    if pismeno in tajne_slovo:
        uhodnuta_pismena.add(pismeno)
        return True
    return False

# Hlavní herní smyčka jedné hry
def hraj_hru():
    tajne_slovo = vyber_nahodne_slovo()  # Náhodné slovo k uhádnutí
    uhodnuta_pismena = set()             # Množina již správně uhodnutých písmen
    chybne_pokusy = 0                    # Počet chybných pokusů

    print("=== Vítej ve hře Hádání slova ===")
    print(f"Hádej slovo! Máš {MAX_CHYB} pokusů.\n")

    # Smyčka běží, dokud hráč neprohraje nebo nevyhraje
    while chybne_pokusy < MAX_CHYB:
        zobraz_stav(tajne_slovo, uhodnuta_pismena)
        pismeno = input("Zadej písmeno: ").lower()

        # Kontrola platnosti vstupu
        if len(pismeno) != 1 or not pismeno.isalpha():
            print("Zadej prosím jedno písmeno.\n")
            continue

        # Kontrola, jestli už nebylo písmeno zadáno dříve
        if pismeno in uhodnuta_pismena:
            print("Toto písmeno už jsi zkusil(a).\n")
            continue

        # Zpracování vstupu – správné nebo špatné písmeno
        if zpracuj_vstup(pismeno, tajne_slovo, uhodnuta_pismena):
            print("Správně!\n")
        else:
            chybne_pokusy += 1
            print("Špatně! Počet chyb:", chybne_pokusy, "\n")

        # Kontrola výhry
        if kontrola_vyhry(tajne_slovo, uhodnuta_pismena):
            print(f"Gratulace! Uhodl(a) jsi slovo: {tajne_slovo}\n")
            break
    else:
        # Pokud hráč překročí limit chyb, prohrává
        print(f"Prohrál(a) jsi! Tajné slovo bylo: {tajne_slovo}\n")

# Spuštění hry – ptá se hráče, jestli chce hrát znovu
def main():
    while True:
        hraj_hru()
        znovu = input("Chceš hrát znovu? (a/n): ").lower()
        if znovu != 'a':
            print("Díky za hru! 👋")
            break

# Pokud se soubor spouští přímo, spustí se main()
if __name__ == "__main__":
    main()

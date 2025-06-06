# 🕵️‍♂️ ProjektHadaniSlova

Jednoduchá hra v příkazovém řádku, kde hráč hádá tajné slovo.

## 🎯 Cíl hry
Cílem hry je uhodnout náhodně zvolené slovo z předem připraveného seznamu. Hráč hádá jednotlivá písmena a snaží se slovo uhodnout dříve, než udělá příliš mnoho chyb.

## 🛠 Funkcionalita
- Výběr náhodného slova ze seznamu
- Zadávání písmen uživatelem
- Zobrazení stavu hádaného slova
- Počet chyb hráče
- Kontrola výhry/prohry
- Možnost rozšíření o úrovně obtížnosti nebo opakovanou hru

## 📂 Struktura kódu
Program je rozdělen do několika funkcí:
- `vyber_nahodne_slovo()` – náhodně vybere slovo
- `zobraz_stav()` – zobrazí aktuální stav slova
- `zpracuj_vstup()` – zpracuje vstup od hráče
- `kontrola_vyhry()` – zkontroluje, zda hráč vyhrál

## 🚀 Spuštění hry
```bash
python hadani.py
# ProjektHadaniSlova

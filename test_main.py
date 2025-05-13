import pytest
from main import (
    vyber_nahodne_slovo,
    zpracuj_vstup,
    kontrola_vyhry,
    SLOVA
)

def test_vyber_nahodne_slovo():
    for _ in range(10):
        slovo = vyber_nahodne_slovo()
        assert slovo in SLOVA

def test_zpracuj_vstup_spravne():
    tajne_slovo = "monitor"
    uhodnuta = set()
    vysledek = zpracuj_vstup("m", tajne_slovo, uhodnuta)
    assert vysledek is True
    assert "m" in uhodnuta

def test_zpracuj_vstup_spatne():
    tajne_slovo = "monitor"
    uhodnuta = set()
    vysledek = zpracuj_vstup("z", tajne_slovo, uhodnuta)
    assert vysledek is False
    assert "z" not in uhodnuta

def test_kontrola_vyhry_true():
    tajne_slovo = "sit"
    uhodnuta = {"s", "i", "t"}
    assert kontrola_vyhry(tajne_slovo, uhodnuta) is True

def test_kontrola_vyhry_false():
    tajne_slovo = "sit"
    uhodnuta = {"s", "i"}
    assert kontrola_vyhry(tajne_slovo, uhodnuta) is False

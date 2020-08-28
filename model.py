# tukaj bom ustvaril model za mojo stran
from typing import List
import secrets
import json


# preverja datum
def je_prestopno(leto):
    if isinstance(leto, int):
        return leto % 4 == 0 and leto % 100 != 0 or leto % 400 == 0
    else:
        raise Exception("a")


def stevilo_dni(mesec, leto):
    if not isinstance(mesec, int) or not isinstance(leto, int):
        raise Exception("b")
    if mesec == 2 and je_prestopno(leto):
        return 29
    elif mesec == 2:
        return 28
    elif mesec == 4 or mesec == 6 or mesec == 9 or mesec == 11:
        return 30
    else:
        return 31


def je_veljaven_datum(dan, mesec, leto):
    if not isinstance(dan, int):
        raise Exception("c")
    return 1 <= mesec <= 12 and 1 <= dan <= stevilo_dni(mesec, leto)


def razbije_datum(niz):
    return niz.split("/")

# preveri uro


def je_veljavna_ura(ura):
    u = ura.split(":")
    return 0 <= int(u[0]) <= 24 and 0 <= int(u[1]) <= 60


# preveri geslo
def veljavno_geslo(geslo):
    return len(geslo.strip()) >= 5


class Uporabnik:
    class TIP:
        TUTOR = 'tutor'
        UCENEC = 'ucenec'

    @staticmethod
    def ustvari(json: dict):
        u = Uporabnik()
        u.__dict__ = json
        return u

    def __init__(self,  uporabnisko_ime: str = None, geslo: str = None, tip: str = None):
        self.uporabnisko_ime: str = uporabnisko_ime
        self.geslo: str = geslo
        self.tip: str = tip


class Dogodek:
    @staticmethod
    def ustvari(json: dict):
        dogodek = Dogodek()
        dogodek.__dict__ = json
        return dogodek

    def __init__(self, datum: str = None, ura: str = None, ime: str = None, letnik: int = None, smer: str = None, ucilnica: int = None, predmet: str = None, tutor=None):  # dodaj tutorja dogodka
        self.datum: str = datum
        self.ura: str = ura
        self.ime: str = ime
        self.letnik: int = letnik
        self.smer: str = smer
        self.ucilnica: int = ucilnica
        self.predmet: str = predmet
        self.id = self.ustvari_id()
        self.tutor = tutor
        self.ucenec = None

    def nastavi_ucenca(self, ucenec):  # to je ob prijavi
        self.ucenec = ucenec

    def odstrani_ucenca(self, ucenec):  # ob odjavi od dogodka
        self.ucenec = None

    def ustvari_id(self):
        return secrets.token_urlsafe(7)

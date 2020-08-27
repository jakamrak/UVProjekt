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
    if mesec == 1 or mesec == 3 or mesec == 5 or mesec == 7 or mesec == 8 or mesec == 10 or mesec == 12:
        return 31
    elif mesec == 4 or mesec == 6 or mesec == 9 or mesec == 11:
        return 30
    elif mesec == 2 and je_prestopno(leto):
        return 29
    else:
        return 28


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


class Tutor:
    def __init__(self,  uporabnisko_ime: str, geslo: str):
        self.uporabnisko_ime: str = uporabnisko_ime
        self.geslo: str = geslo


    #def dodaj_dogodek(self, letnik: int, smer: str, ucilnica: int, predmet: str, ura: str):
    #    nov = Dogodek(datum, ura, ime, letnik, smer,ucilnica, predmet, self.uporabnisko_ime)
    #    return nov


    # def izbrisi_dogodek(self, id_dogodka):


class Ucenec:
    def __init__(self,  uporabnisko_ime: str, geslo: str):
        self.uporabnisko_ime: str = uporabnisko_ime
        self.geslo: str = geslo



    #def prijava_v_dogodek(self, id_dogodka):
    #    for dogodek in self.dogodki:
    #        if id_dogodka == dogodek.id:
    #            self.dogodki.append(dogodek)
    #            break

    #def odjava_od_dogodka(self, id_dogodka):
    #    for i, dogodek in enumerate(self.dogodki):
    #        if id_dogodka == dogodek.id:
    #            self.dogodki.pop(i)
    #            break




class Dogodek:
    def __init__(self, datum: str, ura: str, ime: str, letnik: int, smer: str, ucilnica: int, predmet: str, tutor):  # dodaj tutorja dogodka
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

    def nastavi_ucenca(self, ucenec):  #to je ob prijavi
        self.ucenec = ucenec


    def odstrani_ucenca(self, ucenec): #ob odjavi od dogodka
        self.ucenec = None


    def ustvari_id(self):
        return secrets.token_urlsafe(7)


    def shrani_stanje(self, ime_datoteke):
        slovar_dogodkov = {
            self.id: {
            'datum': self.datum,
            'ime': self.ime,
            'letnik': self.letnik,
            'smer': self.smer,
            'ucilnica': self.ucilnica,
            'predmet': self.predmet,
            'ura': self.ura,
            'tutor': self.tutor,
            'ucenec': self.ucenec
        }
        }
        with open(ime_datoteke, 'w') as datoteka:
            json.dump(slovar_dogodkov, datoteka, ensure_ascii=False, indent=4)


    @classmethod
    def nalozi_stanje(cls, ime_datoteke):
        with open(ime_datoteke) as datoteka:
            slovar_stanja = json.load(datoteka)
      

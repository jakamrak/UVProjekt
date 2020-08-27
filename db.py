#database
from typing import List
from model import *
import sys
import os.path



DATOTEKA_DB = 'db.json'

this = sys.modules[__name__]
this.uporabniki = []
this.dogodki = [] #probaj sortirat dogodke po uri in datumu


#preveri ali je kdo s tem uporabniskim imenom ze registriran
def je_registriran(uporabnisko_ime):
    for uporabnik in this.uporabniki:
        if uporabnik.uporabnisko_ime == uporabnisko_ime:
            return True
    return False
    

#preveri ali ta profil obstaja
def uporabnik_obstaja(uporabnisko_ime='', geslo=''):
    for uporabnik in this.uporabniki:
        if uporabnik.uporabnisko_ime == uporabnisko_ime and uporabnik.geslo == geslo:
            return True
    return False



def dogodek_obstaja(datum, ura, ucilnica):
    for dogodek in this.dogodki:
        if dogodek.datum == datum and dogodek.ucilnica == ucilnica and dogodek.ura == ura:
            return True
    return False


def uporabnik_najdi(uporabnisko_ime):
    for uporabnik in this.uporabniki:
        if uporabnik.uporabnisko_ime == uporabnisko_ime:
            return uporabnik
    

def shrani_stanje():
        db_json = {
            'uporabniki': [u.__dict__ for u in this.uporabniki],
            'dogodki': [d.__dict__ for d in this.dogodki]
        }

        
        with open(DATOTEKA_DB, 'w') as datoteka:
            json.dump(db_json, datoteka, ensure_ascii=False, indent=4)


def nalozi_stanje():
    if os.path.isfile(DATOTEKA_DB):
        with open(DATOTEKA_DB) as datoteka:
            db_json = json.load(datoteka)
            this.uporabniki = [ Uporabnik.ustvari(u) for u in db_json['uporabniki']]
            this.dogodki = [ Dogodek.ustvari(d) for d in db_json['dogodki']]

    




#REFERENCE

#.this
#https://stackoverflow.com/questions/1977362/how-to-create-module-wide-variables-in-python









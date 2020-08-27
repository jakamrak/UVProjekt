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

    




#slovar_dogodkov =  {87654: Dogodek(...),...}
#slovar_stanja = {87654:1, 73645:2 }  #1 pomeni prosto 2 pa zasedeno
#dogodki_ucenec = []
#for id in slovar_stanja:
#    if slovar_stanja[id] == 1:
#        dogodki_ucenec.append(slovar_dogodkov[id])
#    return dogodki_ucenec
    






#testni
#t1 = Uporabnik("tutor1", "geslo1", Uporabnik.TIP.TUTOR)
#t2 = Uporabnik("tutor2", "geslo2", Uporabnik.TIP.TUTOR)
#
#u1 = Uporabnik("ucenec1", "geslo1", Uporabnik.TIP.UCENEC)
#u2 = Uporabnik("ucenec2", "geslo2", Uporabnik.TIP.UCENEC)
#
#d1 = Dogodek('28/12/2020', '14:30', 'dogodek1', 1, 'financna mat', 201, 'Analiza1', 't1')
#d2 = Dogodek('22/9/2020', '17:30', 'dogodek2', 3, 'financna mat', 205, 'Analiza2', 't2')
#d1.ucenec = 'ucenec1'


#t1.dogodki = [d1]
#t2.dogodki = [d2]
#u1.dogodki = [d2]
#u2.dogodki = [d1]


#uporabniki += [t1, t2, u1, u2]
#
#dogodki[d1.id] = d1
#dogodki[d2.id] = d2







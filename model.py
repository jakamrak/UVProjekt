#tukaj bom ustvaril model za mojo stran
from typing import List
import secrets


#preverja datum
def je_prestopno(leto):
    if isinstance(leto, int):
        return  leto % 4 == 0 and leto % 100 != 0 or leto % 400 == 0
    else:
        raise Exception("a")


def stevilo_dni(mesec, leto): 
    if not isinstance(mesec, int) or not isinstance(leto, int):
        raise Exception("b")
    if mesec == 1 or mesec == 3 or mesec == 5 or mesec == 7 or mesec == 8 or mesec == 10 or mesec == 12:
       return 31
    elif mesec == 4 or mesec == 6 or mesec == 9 or mesec == 11 :
        return 30
    elif mesec == 2 and je_prestopno(leto):
        return 29
    else: 
        return 28  


def je_veljaven_datum(dan, mesec, leto):
    if not isinstance(dan, int):
        raise Exception("c")
    return   1 <= mesec <= 12 and 1 <= dan <= stevilo_dni(mesec, leto)

def razbije_datum(niz):
    return niz.split("/")

#preveri uro
def je_veljavna_ura(ura):
    u = ura.split(":")
    return 0 <= int(u[0]) <= 24 and  0 <= int(u[1]) <= 60








class Tutor:
    def __init__(self,  uporabnisko_ime: str, geslo: str):
        self.uporabnisko_ime: str = uporabnisko_ime
        self.geslo: str = geslo 
        

    def dodaj_dogodek(self, letnik: int, smer: str, ucilnica: int, predmet: str, ura: str): #doda dogodek in ga vrne
        #doda ga v dogodke tutorja ter ga returna in to uporabi za dodat v dbju
        nov = Dogodek(datum, ura, ime, letnik, smer, ucilnica, predmet, self.uporabnisko_ime)
        return nov

        #tlele morem se id_dogodka nekako nastimat?


    

    #def izbrisi_dogodek(self, id_dogodka):
    
    
class Ucenec:
    def __init__(self,  uporabnisko_ime: str, geslo: str):
        self.uporabnisko_ime: str = uporabnisko_ime
        self.geslo: str = geslo
        #self.dogodki: List(Dogodek) = []  
    
    

    def prijava_v_dogodek(self, id_dogodka):
        for dogodek in self.dogodki:
            if id_dogodka == dogodek.id:
                self.dogodki.append(dogodek)
                break

        
    
    def odjava_od_dogodka(self, id_dogodka):
        for i, dogodek in enumerate(self.dogodki):
            if id_dogodka == dogodek.id: 
                self.dogodki.pop(i)
                break
        


class Dogodek:
    def __init__(self, datum: str, ura: str, ime: str, letnik: int, smer: str, ucilnica: int, predmet: str, tutor): #dodaj tutorja dogodka
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

    
    def nastavi_ucenca(self, ucenec):
        self.ucenec = ucenec


    def ustvari_id(self): 
        return secrets.token_urlsafe(7)


    



        


#tukaj bom ustvaril model za mojo stran
from typing import List
import secrets



class Tutor:
    def __init__(self,  uporabnisko_ime: str, geslo: str):
        self.uporabnisko_ime: str = uporabnisko_ime
        self.geslo: str = geslo
        self.dogodki: List(Dogodek) = []

    #def ustvari_dogodek(self, letnik: int, smer: str, ucilnica: int, predmet: str, ura: str): #doda dogodek in ga vrne
        #doda ga v dogodke tutorja ter ga returna in to uporabi za dodat v dbju
    

    #def izbrisi_dogodek(self, id_dogodka):
    

    #def posodobi_dogodek(self, id_dogodka, letnik=None, smer=None, ucilnica=None, predmet=None, ura=None):
    
class Ucenec:
    def __init__(self,  uporabnisko_ime: str, geslo: str):
        self.uporabnisko_ime: str = uporabnisko_ime
        self.geslo: str = geslo
        self.dogodki: List(Dogodek) = []
    
    #def prijava_v_dogodek(self, dogodek: Dogodek):
    
    
    def odjava_od_dogodka(self, id_dogodka):
        for i, dogodek in enumerate(self.dogodki):
            if id_dogodka == dogodek.id: #tle se mora se id funkcija ustvarit smz oz uprasi
                self.dogodki.pop(i)
                break


class Dogodek:

    def __init__(self, datum: str, ura: str, ime: str, letnik: int, smer: str, ucilnica: int, predmet: str):
        self.datum: str = datum
        self.ura: str = ura
        self.ime: str = ime
        self.letnik: int = letnik
        self.smer: str = smer
        self.ucilnica: int = ucilnica
        self.predmet: str = predmet
        self.id = self.ustvari_id()

    def ustvari_id(self): 
        return secrets.token_urlsafe(5)


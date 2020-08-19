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
    #    pass

    #def izbrisi_dogodek(self, id_dogodka):
    #    pass

    #def posodobi_dogodek(self, id_dogodka, letnik: int=None, smer: str, ucilnica: int, predmet: str, ura: str):
    #    pass
class Ucenec:
    def __init__(self,  uporabnisko_ime: str, geslo: str):
        self.uporabnisko_ime: str = uporabnisko_ime
        self.geslo: str = geslo
        self.dogodki: List(Dogodek) = []
    
    #def prijava_v_dogodek(self, dogodek: Dogodek):
    # pass
    
    def odjava_od_dogodka(self, id_dogodka):
        for i, dogodek in enumerate(self.dogodki):
            if id_dogodka == dogodek.id: #tle se mora se id funkcija ustvarit smz oz uprasi
                self.dogodki.pop(i)
                break


class Dogodek:

    def __init__(self, letnik: int, smer: str, ucilnica: int, predmet: str, ura: str):
        self.letnik: int = letnik
        self.smer: str = smer
        self.ucilnica: int = ucilnica
        self.predmet: str = predmet
        self.ura: str = ura
        self.id = self.ustvari_id()

    def ustvari_id(self): 
        return secrets.token_urlsafe(5)


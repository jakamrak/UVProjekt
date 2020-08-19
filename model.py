#tukaj bom ustvaril model za mojo stran
from typing import List





class Tutor:
    def __init__(self,  uporabnisko_ime: str, geslo: str):
        self.uporabnisko_ime: str = uporabnisko_ime
        self.geslo: str = geslo
        self.dogodki: List(Dogodek) = []

class Ucenec:
    def __init__(self,  uporabnisko_ime: str, geslo: str):
        self.uporabnisko_ime: str = uporabnisko_ime
        self.geslo: str = geslo
        self.dogodki: List(Dogodek) = []


class Dogodek:
    def __init__(self, letnik: int, smer: str, ucilnica: int, predmet: str, ura: str):
        self.letnik: int = letnik
        self.smer: str = smer
        self.ucilnica: int = ucilnica
        self.predmet: str = predmet
        self.ura: str = ura



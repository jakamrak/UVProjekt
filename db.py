from typing import List
from model import *

tutorji: List[Tutor] = []
ucenci: List[Ucenec] = []
dogodki: List[Dogodek] = []

def je_registriran(uporabnisko_ime):
    for tutor in tutorji:
        if tutor.uporabnisko_ime == uporabnisko_ime:
            return True
    for ucenec in ucenci:
        if ucenec.uporabnisko_ime == uporabnisko_ime:
            return True
    return False
    

def obstaja(uporabnisko_ime, geslo):
    for tutor in tutorji:
        if tutor.uporabnisko_ime == uporabnisko_ime and tutor.geslo == geslo:
            return True
    for ucenec in ucenci:
        if ucenec.uporabnisko_ime == uporabnisko_ime and ucenec.geslo == geslo:
            return True
    return False




#testni
t1 = Tutor("tutor1", "geslo1")
t2 = Tutor("tutor2", "geslo2")

u1 = Ucenec("ucenec1", "geslo1")
u2 = Ucenec("ucenec2", "geslo2")

d1 = Dogodek(1, 'financna mat', 201, 'Analiza1', '14:30')
d2 = Dogodek(2, 'financna mat', 205, 'Analiza2', '17:30')

t1.dogodki = [d1]
t2.dogodki = [d2]
u1.dogodki = [d1, d2]
u2.dogodki = [d1, d2]

tutorji += [t1, t2]
ucenci += [u1, u2]
dogodki += [d1, d2]



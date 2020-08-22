#database
from typing import List
from model import *

tutorji: List[Tutor] = []
ucenci: List[Ucenec] = []
dogodki: List[Dogodek] = [] #probaj sortirat dogodke po uri in datumu
dogodki_ucenec = [] #dogodki, vidni ucencem oz tisti, ki so se prosti
dogodki_tutor = []  #zasedeni dogodki


#preveri ali je kdo s tem uporabniskim imenom ze registriran
def je_registriran(uporabnisko_ime):
    for tutor in tutorji:
        if tutor.uporabnisko_ime == uporabnisko_ime:
            return True
    for ucenec in ucenci:
        if ucenec.uporabnisko_ime == uporabnisko_ime:
            return True
    return False
    

#preveri ali ta profil obstaja
def obstaja(uporabnisko_ime, geslo):
    for tutor in tutorji:
        if tutor.uporabnisko_ime == uporabnisko_ime and tutor.geslo == geslo:
            return True
    for ucenec in ucenci:
        if ucenec.uporabnisko_ime == uporabnisko_ime and ucenec.geslo == geslo:
            return True
    return False



#določi tip osebe
#def kateri_tip(uporabnisko_ime):
    






#testni
t1 = Tutor("tutor1", "geslo1")
t2 = Tutor("tutor2", "geslo2")

u1 = Ucenec("ucenec1", "geslo1")
u2 = Ucenec("ucenec2", "geslo2")

d1 = Dogodek('28/12/2020', '14:30', 'dogodek1', 1, 'financna mat', 201, 'Analiza1', 'tutor1@gmail.com' )
d2 = Dogodek('22/9/2020', '17:30', 'dogodek2', 3, 'financna mat', 205, 'Analiza2', 'tutor2@gmail.com')

t1.dogodki = [d1]
t2.dogodki = [d2]
u1.dogodki = [d1, d2]
u2.dogodki = [d1, d2]


tutorji += [t1, t2]
ucenci += [u1, u2]
dogodki += [d1, d2]
dogodki_ucenec += [d1] 
dogodki_tutor += [d2]



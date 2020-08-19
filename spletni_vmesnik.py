import bottle
from model import * 
import db

#slovar oseb
#tutor = 1
#ucenec = 2

tip_osebe = {
    1: 'Tutor', 
    2: 'Ucenec'
}

@bottle.get('/')
def zacetna_stran():
    bottle.redirect('/prijava/')

@bottle.get('/prijava/')
def prijava_get():
    return bottle.template('prijava.html')

@bottle.get('/registracija/')
def registracija_get():
    return bottle.template('registracija.html')

@bottle.post('/prijava/')
def prijava_post():
    uporabnisko_ime = bottle.request.forms.getunicode('uporabnisko_ime')
    geslo = bottle.request.forms.getunicode('geslo')

    print(uporabnisko_ime, geslo)
    


@bottle.post('/registracija/')
def registracija_post():
    uporabnisko_ime = bottle.request.forms.getunicode('uporabnisko_ime')
    geslo = bottle.request.forms.getunicode('geslo')
    tip = tip_osebe[int(bottle.request.forms.getunicode('tip_osebe'))]

    

    if tip == 'Ucenec':
        ucenec = Ucenec(uporabnisko_ime, geslo)
        db.ucenci.append(ucenec)
    elif tip == 'Tutor':
        tutor = Tutor(uporabnisko_ime, geslo)
        db.tutorji.append(tutor)

    bottle.redirect('/')
    






bottle.run(debug=True, reloader=True)
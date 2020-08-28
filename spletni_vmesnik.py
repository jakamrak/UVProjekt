import bottle
from model import *
import db
from datetime import date


tip_osebe = {
    1: Uporabnik.TIP.TUTOR,
    2: Uporabnik.TIP.UCENEC
}


@bottle.get('/')
def zacetna_stran():
    bottle.redirect('/prijava/')


@bottle.get('/prijava/')
def prijava_get():
    # da se ne rabi prijavit ce se je pred minuto prijavu
    uporabnisko_ime = bottle.request.get_cookie('uporabnik')
    if uporabnisko_ime is not None:
        uporabnik = db.uporabnik_najdi(uporabnisko_ime)
        if uporabnik is not None:
            if uporabnik.tip == Uporabnik.TIP.TUTOR:
                bottle.redirect('/dogodki/')
            else:
                bottle.redirect('/dogodki-ucenec/')
    else:
        return bottle.template('prijava.html', error='')


@bottle.get('/registracija/')
def registracija_get():
    return bottle.template('registracija.html', error='')


# dogodki ki jih vidis ce si registriran kot tutor
@bottle.get('/dogodki/')
def dogodki_get():
    # da ne mores prek urlja kr do dogodkov mimo prijave
    uporabnisko_ime = bottle.request.get_cookie('uporabnik')
    datum = date.today()
    if uporabnisko_ime is None:
        bottle.redirect('/prijava/')
    else:
        dogodki = []
        for d in db.dogodki:
            dogodki.append(d.__dict__)

        moji_dogodki = []
        for d in db.dogodki:
            if d.tutor == uporabnisko_ime:
                moji_dogodki.append(d.__dict__)
        return bottle.template('dogodki.html', dogodki=dogodki, moji_dogodki=moji_dogodki, uporabnik=uporabnisko_ime, datum=datum)


# dogodki ki jih vidis ce si registriran kot ucenec
@ bottle.get('/dogodki-ucenec/')
def dogodki_ucenec_get():
    uporabnisko_ime = bottle.request.get_cookie('uporabnik')
    datum = date.today()
    if uporabnisko_ime is None:
        bottle.redirect('/prijava/')
    else:
        dogodki = []
        for d in db.dogodki:
            if d.ucenec is None:
                dogodki.append(d.__dict__)

        moji_dogodki = []
        for d in db.dogodki:
            if d.ucenec == uporabnisko_ime:
                moji_dogodki.append(d.__dict__)

        return bottle.template('dogodki_ucenec.html', dogodki=dogodki, moji_dogodki=moji_dogodki, uporabnik=uporabnisko_ime, datum=datum)


@ bottle.get('/odjava/')
def odjava_get():
    bottle.response.delete_cookie('uporabnik', path='/')
    bottle.redirect('/prijava/')


@ bottle.get('/dodaj-dogodek/')  # form za ustvarjanje dogodka
def dodaj_dogodek_get():
    return bottle.template('dodaj_dogodek.html', error='')


@ bottle.post('/prijava/')
def prijava_post():
    uporabnisko_ime = bottle.request.forms.getunicode('uporabnisko_ime')
    geslo = bottle.request.forms.getunicode('geslo')
    if db.uporabnik_obstaja(uporabnisko_ime, geslo):
        bottle.response.set_cookie('uporabnik', uporabnisko_ime, path='/')
        uporabnik = db.uporabnik_najdi(uporabnisko_ime)
        if uporabnik.tip == Uporabnik.TIP.TUTOR:
            bottle.redirect('/dogodki/')
        else:
            bottle.redirect('/dogodki-ucenec/')
    else:
        return bottle.template('prijava.html', error='Prijava ni uspela.')


@ bottle.post('/registracija/')
def registracija_post():
    uporabnisko_ime = bottle.request.forms.getunicode('uporabnisko_ime')
    geslo = bottle.request.forms.getunicode('geslo')
    tip = tip_osebe[int(bottle.request.forms.getunicode('tip_osebe'))]

    if not veljavno_geslo(geslo):
        return bottle.template('registracija.html', error=f'Geslo mora vsebovati vsaj 5 znakov.')

    if db.je_registriran(uporabnisko_ime):
        return bottle.template('registracija.html', error=f'Uporabniško ime "{uporabnisko_ime}" že obstaja.')

    uporabnik = Uporabnik(uporabnisko_ime, geslo, tip)
    db.uporabniki.append(uporabnik)
    db.shrani_stanje()

    bottle.redirect('/')


@ bottle.post('/dodaj-dogodek/')
def dodaj_dogodek_post():
    tutor = bottle.request.get_cookie('uporabnik')
    datum = bottle.request.forms.getunicode('datum')
    ura = bottle.request.forms.getunicode('ura')
    ime = bottle.request.forms.getunicode('imeinpriimek')
    letnik = bottle.request.forms.getunicode('letnik')
    smer = bottle.request.forms.getunicode('smer')
    ucilnica = bottle.request.forms.getunicode('ucilnica')
    predmet = bottle.request.forms.getunicode('predmet')
    dan = int(razbije_datum(datum)[0])
    mesec = int(razbije_datum(datum)[1])
    leto = int(razbije_datum(datum)[2])

    if je_veljaven_datum(dan, mesec, leto) and je_veljavna_ura(ura):
        if db.dogodek_obstaja(datum, ura, ucilnica):
            return bottle.template('dodaj_dogodek.html', error=f'Dogodek {datum} ob {ura} v učilnici {ucilnica} že obstaja.')
        else:
            nov = Dogodek(datum, ura, ime, letnik, smer,
                          ucilnica, predmet, tutor)
            db.dogodki.append(nov)
            db.shrani_stanje()
            bottle.redirect('/')
    elif je_veljaven_datum(dan, mesec, leto) and not je_veljavna_ura(ura):
        return bottle.template('dodaj_dogodek.html', error=f'Ura {ura} ni veljavna.')
    elif not je_veljaven_datum(dan, mesec, leto) and not je_veljavna_ura(ura):
        return bottle.template('dodaj_dogodek.html', error=f'Datum {datum} in ura {ura} nista veljavna.')
    else:
        return bottle.template('dodaj_dogodek.html', error=f'Datum {datum} ni veljaven.')


@bottle.get('/dogodki/odstrani/<id>')  # za izbris dogodka
def dogodek_odstrani(id):
    for i, d in enumerate(db.dogodki):
        if d.id == id:
            db.dogodki.remove(d)
            db.shrani_stanje()
    bottle.redirect('/')


@bottle.get('/dogodki-ucenec/prijava/<id>')
def dogodek_prijava(id):
    ucenec = bottle.request.get_cookie('uporabnik')
    if db.uporabnik_najdi(ucenec) is not None:
        for d in db.dogodki:
            if d.id == id:
                d.nastavi_ucenca(ucenec)
                db.shrani_stanje()
    bottle.redirect('/')


@bottle.get('/dogodki-ucenec/odjava/<id>')
def dogodek_odjava(id):
    ucenec = bottle.request.get_cookie('uporabnik')
    if db.uporabnik_najdi(ucenec) is not None:
        for d in db.dogodki:
            if d.id == id:
                d.odstrani_ucenca(ucenec)
                db.shrani_stanje()
    bottle.redirect('/')


db.nalozi_stanje()
bottle.run(debug=True, reloader=True)

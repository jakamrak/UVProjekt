import bottle
from model import *
import db

# slovar oseb
#tutor = 1
#ucenec = 2

tip_osebe = {
    1: 'Tutor',
    2: 'Ucenec'
}

# def dodaj_uporabnike():
#    dogodki = []
#    for d in db.dogodki:
#        dogodki.append({
#            'ime': d.ime,
#            'letnik': str(d.letnik),
#            'smer': d.smer,
#            'ucilnica': d.ucilnica,
#            'predmet': d.predmet,
#            'ura': d.ura
#        })
#    return dogodki


@bottle.get('/')
def zacetna_stran():
    bottle.redirect('/prijava/')


@bottle.get('/prijava/')
def prijava_get():
    # da se ne rabi prijavit ce se je pred minuto prijavu
    uporabnik = bottle.request.get_cookie('uporabnik')
    if uporabnik is not None:
        bottle.redirect('/dogodki/')
    else:
        return bottle.template('prijava.html')


@bottle.get('/registracija/')
def registracija_get():
    return bottle.template('registracija.html', error='')


@bottle.get('/dogodki/')
def dogodki_get():
    # da ne mores prek urlja kr do dogodkov mimo prijave
    uporabnisko_ime = bottle.request.get_cookie('uporabnik')
    if uporabnisko_ime is None:
        bottle.redirect('/prijava/')
    else:
        dogodki = []
        for d in db.dogodki:
            dogodki.append({
                'datum': d.datum,
                'ime': d.ime,
                'letnik': str(d.letnik),
                'smer': d.smer,
                'ucilnica': d.ucilnica,
                'predmet': d.predmet,
                'ura': d.ura
            })
        return bottle.template('dogodki.html', dogodki=dogodki, uporabnik=uporabnisko_ime)


@bottle.get('/odjava/')
def odjava_get():
    bottle.response.delete_cookie('uporabnik', path='/')
    bottle.redirect('/prijava/')


@bottle.post('/prijava/')
def prijava_post():
    uporabnisko_ime = bottle.request.forms.getunicode('uporabnisko_ime')
    geslo = bottle.request.forms.getunicode('geslo')
    # tip = ? moras nekako dobit tip iz cookija vrjetno
    if db.obstaja(uporabnisko_ime, geslo):
        bottle.response.set_cookie('uporabnik', uporabnisko_ime, path='/')
        # if tip == 'Tutor':
        #    pass
        # else:
        #    pass
        bottle.redirect('/dogodki/')
    else:
        return bottle.template('prijava.html', error='Prijava ni uspela.')


@bottle.post('/registracija/')
def registracija_post():
    uporabnisko_ime = bottle.request.forms.getunicode('uporabnisko_ime')
    geslo = bottle.request.forms.getunicode('geslo')
    tip = tip_osebe[int(bottle.request.forms.getunicode('tip_osebe'))]

    if db.je_registriran(uporabnisko_ime):
        return bottle.template('registracija.html', error=f'Uporabniško ime "{uporabnisko_ime}" že obstaja.')
    if tip == 'Ucenec':
        ucenec = Ucenec(uporabnisko_ime, geslo)
        db.ucenci.append(ucenec)
    elif tip == 'Tutor':
        tutor = Tutor(uporabnisko_ime, geslo)
        db.tutorji.append(tutor)

    bottle.redirect('/')


@bottle.get('/ustvari-dogodek/')  # form za ustvarjanje dogodka
def ustvari_dogodek_get():
    # pazit mores da ne ustvarita dve osebi dogodka ob isti uri v isti ucilnici
    return bottle.template('ustvari_dogodek.html', error='')


# @bottle.post('/ustvari-dogodek/') #tutor posreduje info o ustvarjenem dogodku
# def ustvari_dogodek_post():


# @bottle.get('/dogodek/odstrani/') #za izbris dogodka


bottle.run(debug=True, reloader=True)

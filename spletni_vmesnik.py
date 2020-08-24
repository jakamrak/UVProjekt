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


#moras glede na tip povedat kam ga preusmeri ce ze ima cookie!!!!
@bottle.get('/prijava/')
def prijava_get():
    # da se ne rabi prijavit ce se je pred minuto prijavu
    uporabnik = bottle.request.get_cookie('uporabnik')
    #tip = db.slovar_tipov[uporabnik]   
    if uporabnik is not None:
        #if tip == 'Tutor':
        bottle.redirect('/dogodki/')
        #else:
            #bottle.redirect('/dogodki-ucenec/')
    else:
        return bottle.template('prijava.html', error='')



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



@bottle.get('/dogodki-ucenec/') #dogodki ki jih vidis ce si registriran kot ucenec
def dogodki_ucenec_get():
    uporabnisko_ime = bottle.request.get_cookie('uporabnik')
    if uporabnisko_ime is None:
        bottle.redirect('/prijava/')
    else:
        dogodki = []
        for d in db.dogodki_ucenec:
            dogodki.append({
                'datum': d.datum,
                'ime': d.ime,
                'letnik': str(d.letnik),
                'smer': d.smer,
                'ucilnica': d.ucilnica,
                'predmet': d.predmet,
                'ura': d.ura
            })
        return bottle.template('dogodki_ucenec.html', dogodki=dogodki, uporabnik=uporabnisko_ime)



@bottle.get('/odjava/')
def odjava_get():
    bottle.response.delete_cookie('uporabnik', path='/')
    bottle.redirect('/prijava/')



@bottle.get('/dodaj-dogodek/')  # form za ustvarjanje dogodka
def dodaj_dogodek_get():
    return bottle.template('dodaj_dogodek.html', error='')



@bottle.post('/prijava/')
def prijava_post():
    uporabnisko_ime = bottle.request.forms.getunicode('uporabnisko_ime')
    geslo = bottle.request.forms.getunicode('geslo')
     #moras nekako dobit tip iz cookija vrjetno
    if db.obstaja(uporabnisko_ime, geslo):
        bottle.response.set_cookie('uporabnik', uporabnisko_ime, path='/')
        tip = db.slovar_tipov[uporabnisko_ime]
        if tip == 'Tutor':
            bottle.redirect('/dogodki/')
        else:
            bottle.redirect('/dogodki-ucenec/')
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
    
    db.slovar_tipov[uporabnisko_ime] = tip
    bottle.redirect('/')



@bottle.post('/dodaj-dogodek/') #tutor posreduje info o ustvarjenem dogodku
def dodaj_dogodek_post():
    datum = bottle.request.forms.getunicode('datum')
    ura = bottle.request.forms.getunicode('ura')
    ime = bottle.request.forms.getunicode('imeinpriimek')
    letnik = bottle.request.forms.getunicode('letnik')
    smer = bottle.request.forms.getunicode('smer')
    ucilnica = bottle.request.forms.getunicode('ucilnica')
    predmet = bottle.request.forms.getunicode('predmet')
    dan, mesec, leto = int(razbije_datum(datum)[0]), int(razbije_datum(datum)[1]), int(razbije_datum(datum)[2])
    
    if je_veljaven_datum(dan, mesec, leto) and je_veljavna_ura(ura):
        if db.dogodek_obstaja(datum, ura, ucilnica):
            return bottle.template('dodaj_dogodek.html', error=f'Dogodek {datum} ob {ura} v učilnici {ucilnica} že obstaja.')
        else:
            nov = Dogodek(datum, ura, ime, letnik, smer, ucilnica, predmet)
            db.dogodki.append(nov)
            bottle.redirect('/')
    elif je_veljaven_datum(dan, mesec, leto) and not je_veljavna_ura(ura):
        return bottle.template('dodaj_dogodek.html', error=f'Ura {ura} ni veljavna.')
    elif not je_veljaven_datum(dan, mesec, leto) and not je_veljavna_ura(ura):
        return bottle.template('dodaj_dogodek.html', error=f'Datum {datum} in ura {ura} nista veljavna.')
    else:
        return bottle.template('dodaj_dogodek.html', error=f'Datum {datum} ni veljaven.')
    
   






# @bottle.get('/odstrani-dogodek/') #za izbris dogodka


























bottle.run(debug=True, reloader=True)

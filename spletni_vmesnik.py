import bottle

@bottle.get('/')
def zacetna_stran():
    bottle.redirect('/prijava/')

@bottle.get('/prijava/')
def prijava():
    return bottle.template('prijava.html')

@bottle.get('/registracija/')
def registracija():
    return bottle.template('registracija.html')

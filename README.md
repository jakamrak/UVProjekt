# Tutournik
Za končni projekt pri predmetu Uvod v programiranje v letu 2019/2020 sem se odločil ustvariti preprost <b>urnik tutorstva</b>, ki tutorju nudi vpogled v svoje dogodke (tutorske ure), "učencem" pa omogoča prijavo na tutorsko uro. S tem se izognemo nejevolji, ko na tutorja zaman čakamo, saj nas je nekdo že prehitel in zasedel mesto. 

Spletni vmesnik je narejen s pomočjo knjižnice <a href='https://bottlepy.org/docs/dev/'>bottle</a>.

Uporaba je zelo preprosta. Vsak se mora ob prvem obisku registrirati, pri čemer tudi izbere eno od možnosti tutor/učenec. Za registracijo je možna prijava, kjer ima tutor vpogled v svoje dogodke in v vse dogodke (tudi drugih tutorjev). Pravtako ima učenec možnost vpogleda v svoje in v vse razpisane dogodke, med katerimi nato izbere svj termin. Tutor lahko dogodke dodaja, odstrani ali samo posodobi obstoječi dogodek. Učenec pa se prijavi oz. odjavi od dogodka ter s tem sprosti termin za nekoga drugega. 


Strežnik poženite z:

    $ python spletni_vmesnik.py runserver

Spletni vmesnik je lociran na tem <a href='http://127.0.0.1:8080/'>naslovu</a>.





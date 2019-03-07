# -*- coding: utf-8 -*-
# quiz-orm/views.py

from flask import Flask
from flask import render_template, request, redirect, url_for, abort, flash
from playhouse.flask_utils import get_object_or_404
from modele import *
from forms import *

app = Flask(__name__)

plec = [(0, 'męzczyzna'), (1, 'kobieta')]

@app.route('/')
def index():
    """Strona główna"""
    return render_template('index.html')
    
@app.route("/lista_klas")
def lista_klas():
    klasy = Klasa.select().order_by(Klasa.rok_naboru, Klasa.nazwa)
    return render_template('lista_klas.html', klasy=klasy)

@app.route("/dodaj_klase", methods=['GET', 'POST'])
def dodaj_klase():
    form = KlasaForm()

    if form.validate_on_submit():
        Klasa(nazwa=form.nazwa.data, rok_naboru=form.rok_naboru.data,
              rok_matury=form.rok_matury.data).save()
        flash("Klasa dodana", 'alert alert-success')
        return redirect(url_for('lista_klas'))
    elif request.method == 'POST':
        flash("Nie uzupełniono wymaganych pól", 'alert alert-danger')

    return render_template('dodaj_klase.html', form=form)
    
@app.route('/lista_uczniow')
def lista_uczniow():
    uczniowie = Uczen.select().order_by(Uczen.klasa, Uczen.nazwisko, Uczen.imie)
    return render_template('lista_uczniow.html', uczniowie=uczniowie)
    
@app.route("/dodaj_ucznia", methods=['GET', 'POST'])
def dodaj_ucznia():
    form = UczenForm()
    form.plec.choices = plec
    form.klasa.choices = [(klasa.id, klasa.nazwa) for klasa in Klasa.select()]

    if form.validate_on_submit():
        klasa = get_object_or_404(Klasa, Klasa.id == form.klasa.data)
        Uczen(imie=form.imie.data, nazwisko=form.nazwisko.data,
              plec=form.plec.data, klasa=klasa.id).save()
        flash("Uczeń dodany", 'alert alert-success')
        return redirect(url_for('lista_uczniow'))
    elif request.method == 'POST':
        flash("Nie uzupełniono wymaganych pól", 'alert alert-danger')

    return render_template('dodaj_ucznia.html', form=form)
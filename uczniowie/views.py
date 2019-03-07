# -*- coding: utf-8 -*-
# quiz-orm/views.py

from flask import Flask
from flask import render_template, request, redirect, url_for, abort, flash
from modele import *
from forms import *

app = Flask(__name__)

@app.route('/')
def index():
    """Strona główna"""
    return render_template('index.html')

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

@app.route("/lista_klas")
def lista_klas():
    klasy = Klasa.select().order_by(Klasa.rok_naboru, Klasa.nazwa)
return render_template('lista_klas.html', klasy=klasy)

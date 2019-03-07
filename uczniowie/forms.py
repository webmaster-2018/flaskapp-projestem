# -*- coding: utf-8 -*-
# quiz-orm/forms.py

from flask_wtf import FlaskForm
from wtforms import BooleanField, SelectField
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired

blad1 = 'To pole jest wymagane'


class KlasaForm(FlaskForm):
  id = HiddenField()
  nazwa = StringField('Nazwa klasy:', validators=[DataRequired(message=blad1)])
  rok_naboru = StringField('Rok naboru:', validators=[DataRequired(message=blad1)])
  rok_matury = StringField('Rok matury:', validators=[DataRequired(message=blad1)])


class UczenForm(FlaskForm):
  id = HiddenField()
  imie = StringField('Imię ucznia:', validators=[DataRequired(message=blad1)])
  nazwisko = StringField('Nazwisko ucznia:', validators=[DataRequired(message=blad1)])
  plec = SelectField('Płeć ucznia:', validators=[DataRequired(message=blad1)])
  klasa = SelectField('Klasa', coerce=int)

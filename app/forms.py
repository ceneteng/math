# app/forms.py

from flask_wtf import Form
from wtforms import StringField, SelectField, IntegerField, HiddenField
from wtforms.validators import DataRequired

class nameform(Form):
    name = StringField('Name', validators=[DataRequired()])

class gameform(Form):
    problems = StringField('problems', validators=[DataRequired()])
    prbtype = SelectField(u'Problem Type', choices=[('addition','addition'),('subtraction','subtraction'),('mixed','mixed')])
    ceiling = StringField('cieling', validators=[DataRequired()])

class countform(Form):
    counter = IntegerField('counter')

class playform(Form):
    answer = IntegerField('answer')
    total = HiddenField()

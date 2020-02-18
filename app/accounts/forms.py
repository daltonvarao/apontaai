from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, EqualTo, Length


password_validators = [
    DataRequired(), 
    EqualTo('confirm', message='As senhas não conferem'),
    Length(min=8, max=32, message='Senha deve ter entre 8 e 32 caracteres.')
]


class UserForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Senha', validators=password_validators)
    confirm = PasswordField('Confirme a senha', validators=password_validators)
    submit_button = SubmitField('Salvar')

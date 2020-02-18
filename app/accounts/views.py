from flask import Blueprint, render_template, request, flash, redirect, url_for
from .forms import UserForm
from flask.views import MethodView
from .models import Usuario, db
from ..app.utils import flash_form_errors, logged_out_only


accounts = Blueprint('accounts', __name__)

class NewAccountsView(MethodView):
    decorators = [
        logged_out_only
    ]

    def get(self):
        form = UserForm()
        return render_template('accounts/new.html', form=form)


    def post(self):
        form = UserForm(request.form)
        
        if form.validate_on_submit():
            email_exists = Usuario.get_by_email(email=form.email.data)
            
            if not email_exists:
                usuario = Usuario(
                    name = form.name.data,
                    email = form.email.data,
                )
                usuario.encrypt_password(form.password.data)
                usuario.save()
                flash(f'Bem vindo, {usuario.name}. Faça login para continuar.', 'success')
                return redirect(url_for('auth.login'))
            else:
                flash('Email já existe, tente outro.', 'danger')
                return render_template('accounts/new.html', form=form)
        else:
            flash_form_errors(form)
        return render_template('accounts/new.html', form=form)

accounts.add_url_rule('/register', view_func=NewAccountsView.as_view('new'))

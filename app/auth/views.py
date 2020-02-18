from flask import Blueprint, render_template, request, redirect, url_for, g, session, flash
from .forms import LoginForm
from flask.views import MethodView
from ..accounts.models import Usuario
from ..app.utils import flash_form_errors, login_required, login, logged_out_only


auth = Blueprint('auth', __name__)


class LoginView(MethodView):
    decorators = [
        logged_out_only
    ]


    def get(self):
        form = LoginForm()
        return render_template('auth/new.html', form=form)


    def post(self):
        form = LoginForm(request.form)
        
        if form.validate():
            usuario = Usuario.get_by_email(email=form.email.data)
            if usuario:
                if usuario.authenticate(form.password.data):
                    login(usuario)
                    flash(f'Seja bem vindo {usuario.name.split()[0]}.', 'success')
                    return redirect(url_for('home.index'))
                else:
                    flash('Senha incorrenta, tente novamente.', 'danger')
                    return render_template('auth/new.html', form=form)
            else:
                flash('Email de usuário não econtrado, tente outro.', 'danger')
                return render_template('auth/new.html', form=form)
        else:
            flash_form_errors(form)
        return render_template('auth/new.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    session.clear()
    return redirect(url_for('auth.login'))


@auth.before_app_request
def load_logged_user():
    user_id = session.get('user_id')
    if user_id:
        user = Usuario.get(user_id)
        user.is_authenticated = True
        g.user = user
    else:
        g.user = Usuario()

auth.add_url_rule('/login', view_func=LoginView.as_view('login'))

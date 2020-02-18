from flask import g, session, flash, redirect, url_for
import functools


def flash_form_errors(form):
    for _, error in form.errors.items():
        flash(error[0], 'danger')


def login(user):
    session['user_id'] = user.id


def logged_out_only(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):        
        if session.get('user_id'):
            return redirect(url_for('home.index'))
        return view(**kwargs)
    return wrapped_view


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):        
        if not session.get('user_id'):
            flash('Faça login para continuar.', 'danger')
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view


def admin_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):        
        if session.get('user_id') and (not g.user.is_admin):
            flash('Permissão negada.', 'danger')
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view

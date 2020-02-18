import click
import os
import sys

from flask import Flask

CURRENT_DIR = os.path.dirname(__file__).split('/')[-1]
PACKAGE_DIR = os.path.dirname(os.path.dirname(__file__))

files = ['models', 'views', '__init__']


def set_app_generator_command(app):
    
    @app.cli.command('app', help='Gerador de apps flask.')
    @click.argument('app_name')
    def app_generator(app_name):
        full_path = f"{PACKAGE_DIR}/{app_name}"
        
        if os.path.exists(full_path):
            print('Erro: App ja existe.')
            sys.exit()
        else:
            os.system(f'mkdir {full_path}')
            
            for file in files:
                os.system(f'touch {full_path}/{file}.py')
            print('Criado novo app %s.' % app_name)
            with open(f'{PACKAGE_DIR}/{CURRENT_DIR}/__init__.py', 'a') as file:
                file.write(f"import_module('app.{app_name}.models')\n")


def set_deploy_command(app):
    
    @app.cli.command('deploy', help='Comando de pos-deploy do heroku.')
    def app_generator():
        os.system('flask db migrate')
        os.system('flask db upgrade')


def register_commands(app):
    set_app_generator_command(app)
    set_deploy_command(app)

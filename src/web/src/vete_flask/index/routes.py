import inject

from flask import render_template, flash, redirect,request, Markup, url_for, send_from_directory, jsonify

from vete_flask.config import Config
from . import bp

@bp.route('/')
@inject.autoparams()
def index(config: Config):
    return render_template('index.html', version=config.version)

@bp.route('/error')
def error():
    return render_template('error.html', error='', version='')

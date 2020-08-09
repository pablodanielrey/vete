import inject
from flask import render_template, flash, redirect,request, Markup, url_for, send_from_directory, jsonify

from . import bp

@inject.autoparams('config')
@bp.route('/')
def index(config):
    return render_template('index.html', version=config.version)

@inject.autoparams('config')
@bp.route('/error')
def error(config):
    return render_template('error.html', error='', version=config.version)

from flask import render_template, flash, redirect,request, Markup, url_for, send_from_directory, jsonify

from . import bp

@bp.route('/')
def index():
    return render_template('index.html', version='')

@bp.route('/error')
def error():
    return render_template('error.html', error='', version='')

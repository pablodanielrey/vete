import logging
import inject
from flask import render_template, flash, redirect,request, Markup, url_for, send_from_directory, jsonify

from vete.config import Config
from vete.models.ClinicModel import ClinicModel
from . import bp


@bp.route('/')
@inject.autoparams()
def index(config:Config):
    return render_template('index.html', version=config.version)

@bp.route('/error')
@inject.autoparams()
def error(config: Config):
    return render_template('error.html', error='', version=config.version)

@bp.route('/patients', methods=['GET'])
@inject.autoparams()
def patients(config: Config, model: ClinicModel):
    try:
        patients = model.patients()
        return render_template('patients.html', patients=patients, version=config.version)
    except Exception as e:
        logging.exception(e)
        return render_template('error.html', error='', version=config.version)

@bp.route('/patient', methods=['GET'])
@inject.autoparams()
def patient(config: Config):
    return render_template('patient.html', version=config.version)

@bp.route('/patient', methods=['POST'])
@inject.autoparams()
def patients_create(config: Config):
    return render_template('patient.html', version=config.version)

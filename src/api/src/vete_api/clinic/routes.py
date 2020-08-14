import logging
import inject
from flask import render_template, flash, redirect,request, Markup, url_for, send_from_directory, jsonify

from vete_flask.config import Config
from vete_models.clinic.ClinicModel import ClinicModel

from . import bp

@bp.route('breeds/<species_id>', methods=['GET'])
@inject.autoparams('model')
def get_breeds_by_species(species_id: str, model: ClinicModel):
    breeds = model.breeds_by_species(species_id)
    r = {
        'data': breeds
    }
    return jsonify(r)

@bp.route('species', methods=['GET'])
@inject.autoparams()
def get_species(model: ClinicModel):
    breeds = model.species()
    r = {
        'data': breeds
    }
    return jsonify(r)

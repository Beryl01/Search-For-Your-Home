from flask import render_template, url_for, redirect, request
from . import main
from ..models import User_Owner, User_tenant, Property
from flask_login import login_required
from .. import db

# your views go here i.e for home,about
@main.route("/")
@main.route("/index")
def index():
    return render_template('index.html')
   
@main.route("/categories")
def categories():
    all_properties = Property.query.all()
    nairobi_properties = Property.query.filter_by(location = 'nairobi').all() 
    nakuru_properties = Property.query.filter_by(location = 'nakuru').all()
    mombasa_properties = Property.query.filter_by(location = 'mombasa').all()
    kisumu_properties = Property.query.filter_by(location = 'kisumu').all()
    eldoret_properties = Property.query.filter_by(location = 'eldoret').all()
    _0_to_20 = Property.query.filter_by(rent_category = '_0_to_20').all()
    _20_to_40 = Property.query.filter_by(rent_category = '_20_to_40').all()
    _40_to_60 = Property.query.filter_by(rent_category = '_40_to_60').all()
    above_60 = Property.query.filter_by(rent_category = 'above_60').all()
   
    return render_template('categories.html',all_properties = all_properties, nairobi_properties = nairobi_properties, mombasa_properties = mombasa_properties, nakuru_properties = nakuru_properties, kisumu_properties = kisumu_properties, eldoret_properties = eldoret_properties, _0_to_20 = _0_to_20, _20_to_40 = _20_to_40, _40_to_60 = _40_to_60, above_60 = above_60 )

@main.route('/property/<int:id>')
def _property(id):

    _property = Property.query.get(id)
    
    return render_template('property.html',property = property)

from flask import render_template,request,redirect,url_for,abort
from . import owner
from .forms import PropertyForm
from ..models import User_Owner, Property
from flask_login import login_required, current_user
from .. import db,photos


@owner.route('/create_property', methods = ['POST','GET'])
@login_required
def create_property():
    form = PropertyForm()
    if form.validate_on_submit():
        _0_to_20 = None
        _20_to_40 = None
        _40_to_60 = None
        above_60 = None
        description = form.description.data
        rent = form.rent.data
        if rent < 20001:
            rent_category = _0_to_20
        elif rent < 40001:
            rent_category = _20_to_40
        elif rent < 60001:
            rent_category = _40_to_60
        else:
            rent_category = above_60

        location = form.location.data 
        image_file = form.image.data
        owner_id = current_user._get_current_object().id 
        new_property = Property(description=description, rent=rent, rent_category=rent_category, location=location, image_file=image_file, owner_id=owner_id)
        new_property.save()
        return redirect(url_for('owner.create_property'))
        
    return render_template('create_propert.html', form = form)


 
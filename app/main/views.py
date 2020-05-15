from flask import render_template, url_for, flash, redirect, request, abort
from . import main
from PIL import Image
from ..models import User, Property
from flask_login import login_user, current_user, logout_user, login_required
from .. import db
from .forms import RegistrationForm, LoginForm, PropertyForm

# your views go here i.e for home,about
@main.route("/")
@main.route("/index")
def index():
    return render_template('index.html')
   
@main.route("/categories")
def categories():
    all_properties = Property.query.all()
    return render_template('categories.html',all_properties = all_properties)

@main.route('/property/<int:id>',methods= ['POST'])
@login_required
def property_pic(id):
    property = Property.query.filter_by(owner_id = id).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'images/{filename}'
        property.image_file = path
        db.session.commit()
    return redirect(url_for('categories'))

@main.route("/property/new", methods=['GET', 'POST'])
@login_required
def new_property():
    form = PropertyForm()
    if form.validate_on_submit():
        property = Property(location=form.location.data, rent= form.rent.data, content=form.content.data, picture=form.picture.data, contact=form.contact.data)
        db.session.add(property)
        db.session.commit()
        flash('Your property has been posted!', 'success')
        return redirect(url_for('categories'))
    return render_template('create_property.html', title='New Property', form=form, legend='New Property')     

@main.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
    
@main.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)   

@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))

 

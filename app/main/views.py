from flask import render_template, url_for, flash, redirect, request, abort
from . import main
from PIL import Image
from ..models import User, Property
from flask_login import login_user, current_user, logout_user, login_required
from .. import db

# your views go here i.e for home,about
@main.route("/")
@main.route("/index")
def index():
    return render_template('index.html')
   
@main.route("/categories")
def categories():
    all_properties = Property.query.all()
    return render_template('categories.html',all_properties = all_properties)

@main.route('/property/<int:property_id>')
@login_required
def _property(property_id):
    _property = Property.query.get(id)
    return render_template('property.html',_property = _property)

@main.route("/property/new", methods=['GET', 'POST'])
@login_required
def new_property():
    form = PropertyForm()
    if form.validate_on_submit():
        _property = Property(location=form.location.data, rent= form.rent.data, content=form.content.data, picture=form.picture.data, contact=form.contact.data)
        db.session.add(_property)
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

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/images', picture_fn)

    output_size = (1364, 900)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn   

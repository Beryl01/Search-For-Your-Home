from . import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

class User_tenant(db.Model, UserMixin):

    __tablename__ = 'tenant_users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(20), unique=True, nullable=False)
    last_name = db.Column(db.String(20), unique=True, nullable=False)
    secure_password = db.Column(db.String(20),nullable = False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    property_id = db.Column(db.Integer, db.ForeignKey('properties.id'))
    _property = db.relationship('Property',backref = 'tenant_user',lazy="dynamic")

    @property
    def set_password(self):
        raise AttributeError('You cannot read the password attribute')

    @set_password.setter
    def password(self, password):
            self.secure_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.secure_password,password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class User_Owner(db.Model, UserMixin):

    __tablename__ = 'owner_users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(20), unique=True, nullable=False)
    last_name = db.Column(db.String(20), unique=True, nullable=False)
    secure_password = db.Column(db.String(255),nullable = False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    property_id = db.Column(db.Integer, db.ForeignKey('properties.id'))
    verified = db.Column(db.Boolean, default=False, nullable=False)
    _property = db.relationship('Property',backref = 'owner_user',lazy="dynamic")

    @property
    def set_password(self):
        raise AttributeError('You cannot read the password attribute')

    @set_password.setter
    def password(self, password):
            self.secure_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.secure_password,password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Property(db.Model):

    __tablename__ = 'properties'
    
    id = db.Column(db.Integer, primary_key=True)
    rent = db.Column(db.Integer,nullable=False)
    rent_category = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner_users.id'), nullable=False)
    tenant_id =db.Column(db.Integer, db.ForeignKey('tenant_users.id'))
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
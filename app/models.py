from . import db

class Landlord(db.Model):
    __tablename__ = 'landlord'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f'Landlord {self.username}'

class Tenant(db.Model):
    __tablename__ = 'tenant'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f'Tenant {self.username}'

class Property(db.Model):
    __tablename__ = 'property'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(20))

    def __repr__(self):
        return f'Property {self.title}'        
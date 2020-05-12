from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    """
    creates an instances of the application 
    and passes the config name, i.e development
    or production, the will then pick the environments
    from the configuration classes in config
    """

    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # set the configurations
    app.config.from_object(config_options[config_name])

    # initialiaze bootstrap
    bootstrap.init_app(app)

    # initialiaze the database
    db.init_app(app)   

    # register your blueprints here
    from app.main import main
    from app.auth import auth
    from app.owner import owner
    from app.properties import properties
    from app.tenant import tenant
    
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(owner)
    app.register_blueprint(properties)
    app.register_blueprint(tenant)

    return app 

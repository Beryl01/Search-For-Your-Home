from flask import render_template,request,redirect,url_for,abort
from . import owner
from .forms import PropertyForm
from ..models import User_Owner, Property
from flask_login import login_required, current_user
from .. import db,photos
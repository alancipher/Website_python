from flask import  Blueprint, render_template

#blueprint nous avons des routes ici 

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")
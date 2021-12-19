from flask import  Blueprint

#blueprint nous avons des routes ici 

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return "<h1> Test </h1>"
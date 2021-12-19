#authentification purpose 

from flask import  Blueprint

#blueprint nous avons des routes ici 

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p> Login </p>"


@auth.route('/logout')
def logout():
    return "<p> Loout </p>"



@auth.route('/sig-up')
def sign_up():
    return "<p> Sign Up </p>"
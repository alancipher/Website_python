#authentification purpose 

from flask import  Blueprint,render_template

#blueprint nous avons des routes ici 

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return  render_template("login.html", text="Texting", user = "Tim")


@auth.route('/logout')
def logout():
    return "<p> Loout </p>"



@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")
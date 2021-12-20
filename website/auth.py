#authentification purpose 

from flask import  Blueprint,render_template, request, flash, url_for, redirect
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
#blueprint nous avons des routes ici 
from . import db 
auth = Blueprint('auth', __name__)

@auth.route('/login', methods= ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password') 

        user =User.query.filter_by(email=email).first()
        if user :
            if check_password_hash(user.password, password):
                flash('logged in successfully!', category='success')
            else:
                flash('not correct input, try it again!', category='error')

        else:
            flash('User does not exists!', category='error')
          
          

    return  render_template("login.html", text="Texting", user = "Tim")


@auth.route('/logout')
def logout():
    return "<p> Loout </p>"



@auth.route('/sign-up', methods= ['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firsname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user =User.query.filter_by(email=email).first()
        if user :
            flash('the user already exist', category='error')


        if len(email)< 4 :
            
            flash('email must be greater than 4 chararter ', category='error')
        elif len(firsname)< 2 :
            flash('firstname  must be greater than 2 chararter ', category='error')
           
        elif password1 != password2:
            flash('password 1 must be equal to password 2  ', category='error')
            
        elif len(password1) < 7 :
            flash('password must have more than 7 characters', category='error')
        else :
            #add user to the db
            user = User(email = email, firstname =firsname, password= password1 )
            flash('account created with succes ', category='success')
            return redirect(url_for('views.home'))
    return render_template("sign_up.html")
#authentification purpose 

from flask import  Blueprint,render_template, request, flash

#blueprint nous avons des routes ici 

auth = Blueprint('auth', __name__)

@auth.route('/login', methods= ['GET', 'POST'])
def login():
    data = request.form
    print(data)
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
            flash('account created with succes ', category='success')
    return render_template("sign_up.html")
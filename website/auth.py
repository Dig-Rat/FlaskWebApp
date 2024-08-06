from . import db
from .models import User
from flask import Blueprint
from flask import render_template
from flask import flash
from flask import redirect
from flask import url_for
from flask import request
from flask_login import login_user
from flask_login import login_required
from flask_login import logout_user
from flask_login import current_user
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

# Blueprint for authentication functions.
auth = Blueprint('auth', __name__)

# Page for handling user login.
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Print out the posted data to help debug.
        #data = request.form
        #print(data)
        # Query user data based on form input.
        email = request.form.get('email')
        password = request.form.get('password')
        #db1 = get_db()
        user = User.query.filter_by(email=email).first()
        # If a result for the user query exist.
        if user:
            # Check if password is correct by checking the password hash.
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                flash('Logged in.', category='success')
                # Redrirect user to homepage.
                return redirect(url_for('views.home'))
            else:
                flash('Password incorrect.', category='error')
        else: 
            flash('Email does not exist.', category='error')
    return render_template('login.html', user=current_user)

# Page for logging the user out.
@auth.route('/logout')
@login_required
def logout():
    # Log out the user and redirect to login page.
    logout_user()    
    return redirect(url_for('auth.login'))

# Page for handling user Sign-Up.
@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get posted form values.
        email=request.form.get('email')
        firstName=request.form.get('firstName')
        password1=request.form.get('password1')
        password2=request.form.get('password2')
        # Query for the user data by the given email. first result only.
        user = User.query.filter_by(email=email).first()
        # Check form values.
        if user:
            flash('Email already exist.', category='error')
        elif len(email) < 4:
            flash('Email too small.', category='error')
        elif len(firstName) < 2:
            flash('Name too small.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match!.', category='error')
        elif len(password1) < 7:            
            flash('Password too small.', category='error')
        else:
            # Create a new user, use a hash for the password. Then add user to database.
            new_user = User(email=email, firstName=firstName, password=generate_password_hash(password1, method='pbkdf2:sha256'))            
            db.session.add(new_user)
            db.session.commit()
            # Log the user in, remember the user session.
            login_user(new_user, remember=True)
            flash('Account Created', category='success')
            # Redirect user to the home page.
            return redirect(url_for('views.home'))
        
    return render_template('sign_up.html', user=current_user)



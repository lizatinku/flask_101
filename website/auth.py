from flask import Blueprint

auth = Blueprint('auth', '__name___')

# Route 1
@auth.route('/login')
def login():
    return "<p>Login</p>"

# Route 2
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

# Route 3
@auth.route('/sign-up')
def sign_up():
        return "<p>Sign Up</p>"


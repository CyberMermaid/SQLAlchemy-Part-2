from flask import Flask, request, render_template, redirect, flash, session
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'AwesomeSauce'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cyber_ace'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


@app.route('/', methods=['GET'])
def base_page():
    """Redirect to list of users"""
    return redirect('/users') 
# Flask tools unit


@app.route('/users', methods=['GET'])
def list_users():
    "Show links of all users and another link to the add-user form"
    users = User.query.all()
    return render_template("list.html", users=users)
# **GET */users :*** Show all users. Make these links to view the detail page for the user. Have a link here to the add-user form.

@app.route('users/new', methods=['GET'])
def add_form():
    """Show an add form for users"""
    return render_template("form.html")

@app.route('users/new', methods=['POST'])
def add_user():
    """Process the add form and adds new user before going back to ***/users***"""
    first_name = request.args["first_name"]
    last_name = request.args["last_name"]
    image_URL = request.args["image_URL"]

     # Validate data
    if not first_name or not last_name or not image_URL:
        return "All fields are required",  400

    # Create a new user object
    new_user = User(first_name=first_name, last_name=last_name, image_URL=image_URL)

    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect('/users') 


@app.route('/users/<int:user_id>', methods=['GET'])
def show_user(user_id):
    """Show information about the given user.
    Have a button to get to their edit page, and to delete the user."""
    user = User.query.get_or_404(user_id)
    return render_template("detail.html", user=user)


# TODO
@app.route('/users/<int:user_id>/edit', methods=['GET'])
def edit_form(user_id):
    """Show the edit page for a user.
    Have a cancel button that returns to the detail page for a user,
    and a save button that updates the user."""
    user = User.query.get(user_id)
    return render_template("editUser.html", user=user)


# TODO
@app.route('/users/<int:user_id>/edit', methods=['POST'])
def update_user(user_id):
    """Process the edit form, returning the user to the /users page."""
    return redirect('/users')

# **POST */users/[user-id]/delete :*** Delete the user.
@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    """Delete the user."""
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    # flash('User deleted successfully.')
    return redirect('/users')

if __name__ == '__main__':
    app.run(debug=True)
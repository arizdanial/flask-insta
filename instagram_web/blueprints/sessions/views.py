from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.user import User
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user

sessions_blueprint = Blueprint('sessions',
                               __name__,
                               template_folder='templates')


@sessions_blueprint.route("/new")
def new():
    return render_template("sessions/new.html")


@sessions_blueprint.route("/", methods=["POST"])
def create():
    username = request.form["username"]
    password = request.form["password"]
    user = User.get_or_none(User.username == username)
    if user and check_password_hash(user.password_hash, password):
        flash("Login successful!")
        login_user(user)
        return redirect(url_for('home'))
    else:
        print("Bad login")
        return redirect(url_for('sessions.new'))


@sessions_blueprint.route("/delete", methods=["POST"])
def destroy():
    logout_user()
    return redirect(url_for('sessions.new'))


## testing new line  new2 
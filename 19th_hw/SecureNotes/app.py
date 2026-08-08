import os

from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user,
)

from db import db
from models import User, Note
from forms import RegisterForm, LoginForm, NoteForm

basedir = os.path.abspath(os.path.dirname(__file__))
instance_path = os.path.join(basedir, "instance")
os.makedirs(instance_path, exist_ok=True)

app = Flask(__name__)
app.config["SECRET_KEY"] = "შეცვალეთ-ეს-გასაღები-production-ში"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    instance_path, "notes.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.login_message = "გთხოვთ გაიაროთ ავტორიზაცია, რომ ნახოთ ეს გვერდი."
login_manager.login_message_category = "warning"


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


@app.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for("notes"))
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("notes"))

    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("რეგისტრაცია წარმატებით დასრულდა! ახლა შეგიძლიათ შეხვიდეთ სისტემაში.", "success")
        return redirect(url_for("login"))

    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("notes"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get("next")
            flash("წარმატებით შეხვედით სისტემაში!", "success")
            return redirect(next_page or url_for("notes"))
        else:
            flash("არასწორი მომხმარებლის სახელი ან პაროლი.", "danger")

    return render_template("login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("წარმატებით გახვედით სისტემიდან.", "info")
    return redirect(url_for("login"))


@app.route("/notes")
@login_required
def notes():
    user_notes = (
        Note.query.filter_by(user_id=current_user.id)
        .order_by(Note.created_at.desc())
        .all()
    )
    return render_template("notes.html", notes=user_notes)


@app.route("/notes/add", methods=["GET", "POST"])
@login_required
def add_note():
    form = NoteForm()
    if form.validate_on_submit():
        note = Note(
            title=form.title.data,
            content=form.content.data,
            user_id=current_user.id,
        )
        db.session.add(note)
        db.session.commit()
        flash("ჩანაწერი წარმატებით დაემატა!", "success")
        return redirect(url_for("notes"))

    return render_template("add_note.html", form=form)


@app.route("/notes/delete/<int:note_id>", methods=["POST"])
@login_required
def delete_note(note_id):
    note = db.session.get(Note, note_id)
    if note is None or note.user_id != current_user.id:
        flash("ჩანაწერი ვერ მოიძებნა ან წვდომა აკრძალულია.", "danger")
        return redirect(url_for("notes"))

    db.session.delete(note)
    db.session.commit()
    flash("ჩანაწერი წაიშალა.", "info")
    return redirect(url_for("notes"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
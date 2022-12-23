from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import current_user, login_required
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    from .models import User
    users = User.query.all()

    if request.method=='POST':
        note = request.form.get('note')

        if len(note)<1:
            flash('Description is too short! Add something please', category="error")
        elif len(note)>500:
            flash('Description is too long! use a smaller tag...', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Updated Successfully', category='success')
    return render_template("home.html", user=current_user, users=users)
    

@views.route('/delete-note', methods=["POST"])
def delete_note():
    note = json.loads(request.data)
    noteId= note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    
    return jsonify({})


@views.route('/about')
def about():
    return render_template("about.html", user=current_user)


@views.route('/profile', methods=["GET","POST"])
def profile():
    if(request.method=="POST"):
        bio = request.form.get('bio')
        current_user.bio = bio
        db.session.commit()
        flash("Updated Successfully", category="success")
    return render_template("profile.html", user=current_user)

@views.route('/portfolio<id>')
def portfolio(id):
    from .models import User
    portuser = User.query.get(id)
    print(portuser)
    return render_template("portfolio.html", user=current_user, displayeduser = portuser)
from . import db
from .models import Note
import json
from flask import Blueprint
from flask import render_template
from flask import flash
from flask import jsonify
from flask import request
from flask_login import login_required
from flask_login import current_user

from .downloader import download_content

# View functionality:
# Provide responses for requests to the application.

# Blueprint for views defined.
views = Blueprint('views',__name__)

# root/home
@views.route('/', methods=['GET','POST'])
def home():
    flash('Hello!', category='success')
    if request.method == 'POST':
        txt = request.form.get('TextBox')
        testURL = 'https://www.youtube.com/watch?v=He_fzO0L01I'
        #optionAudio = 'bestaudio[ext=m4a]'
        optionVideo = 'bestvideo+bestaudio'
        #download_content(testURL,optionAudio)
        download_content(testURL,optionVideo)
        
    return render_template('home.html', user=current_user)

# Page handles requests for note deletion.
@views.route('/delete-note', methods=['POST'])
@login_required
def delete_note():
    # Expects JSON data from a POST request.
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    # If a note exist with a matching note id.
    if note:
        # if note belongs to current user, delete it.
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    # Returns JSON response none/default. - Improve response.
    return jsonify({})

# Page for user to enter notes for database.
@views.route('/notes', methods=['GET','POST'])
@login_required
def NotesPage():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short', category='error')
        else:
            # Schema for note.
            new_note = Note(data=note, user_id=current_user.id)
            # Add note to database
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template(template_name_or_list='notes.html', user=current_user)

    
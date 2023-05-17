from flask import Blueprint, render_template, request, redirect, url_for
from database import ImageDB
import os

views = Blueprint('views', __name__)
db = ImageDB()

@views.route('/')
def home():
    images = db.get_images()
    return render_template('home.html', images=images)

@views.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filename = file.filename
            path = os.path.join('uploads', filename)
            file.save(path)
            db.add_image(filename, path)
            return redirect(url_for('views.home'))
    return render_template('upload.html')

@views.route("/account")
def account():
    return('yooopie')
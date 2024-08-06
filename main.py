#!/usr/bin/env/ python
from website import create_app
app = create_app()
if __name__ == '__main__':
    # App Deployment
    # https://flask.palletsprojects.com/en/3.0.x/deploying/
    app.run(debug=True)
    print('Running')

# View App on local
# http://127.0.0.1:5000

# Pre-Reqs
# pip install flask
# pip install flask-login
# pip install flask-sqlalchemy
# python3 -m pip install -U yt-dlp

# VSC Flask tutorial
# https://code.visualstudio.com/docs/python/tutorial-flask

# Flask Docs
# https://flask.palletsprojects.com/en/3.0.x/
# https://flask.palletsprojects.com/en/3.0.x/installation/
# https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application

# Jinja Docs
# https://jinja.palletsprojects.com/en/3.1.x/
# https://jinja.palletsprojects.com/en/3.1.x/templates/

# Flask SQL Alchemy
# https://flask.palletsprojects.com/en/3.0.x/patterns/sqlalchemy/
# https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/

# Bootstrap
# https://getbootstrap.com/
# https://getbootstrap.com/docs/5.3/getting-started/contents/

# Password hashing.
# https://werkzeug.palletsprojects.com/en/3.0.x/utils/#werkzeug.security.generate_password_hash

# yt-dlp
# https://github.com/yt-dlp/yt-dlp

# FFmpeg
# https://ffmpeg.org/

# TO DO
    # HTTP Requests
    # https://requests.readthedocs.io/en/latest/user/quickstart.html



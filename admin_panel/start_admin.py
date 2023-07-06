#!/usr/bin/python3
""" Starts a Flash Web Application """
import uuid
from os import environ
import subprocess
from flask import Flask, render_template
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True

@app.route('/admin', strict_slashes=False)
def admin():
    """ admin panel going live """
    return render_template('login.html')
   # php_script = 'index.php'
   # result = subprocess.check_output(['php', php_script])
   # return result

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5005)

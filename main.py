# Flask-fileserver - see VERSION_ID below  
# for gunicorn / Flask
# uses html templates in /templates
# requires read/write privileges to UPLOAD_FOLDER defined in app.config

import datetime
import os
from flask import Flask, render_template, request, send_from_directory, url_for
from werkzeug.exceptions import BadRequest
from werkzeug.utils import secure_filename

VERSION_ID = "version 1.0"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/var/www/uploads'

def _check_extension(filename):
  file, ext = os.path.splitext(filename)
  if (ext.replace('.', '') not in ALLOWED_EXTENSIONS):
    raise BadRequest('{0} has an invalid name or extension'.format(filename))

def _safe_filename(filename):
# ``filename.ext`` is transformed into ``filename-YYYY-MM-DD-HHMMSS-UUUUUU.ext``
  filename = secure_filename(filename)
  date = datetime.datetime.utcnow().strftime("%Y-%m-%d-%H%M%S-%f")
  basename, extension = filename.rsplit('.', 1)
  return "{0}-{1}.{2}".format(basename, date, extension)

@app.route('/')
def index():
    return 'Flask-fileserver %s' % VERSION_ID

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/list', methods=['GET'])
def list_files():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('list.html', files=files)

@app.route('/upload/<filename>', methods=['GET', 'POST'])
def upload_file(filename=None):
    if request.method == 'POST':
      f = request.files['image']
      _check_extension(filename)
      filename = _safe_filename(filename)
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template('upload.html')

@app.route('/download/<filename>')
def download_file(filename):
    if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
      return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    raise BadRequest('{0} does not exist'.format(filename))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

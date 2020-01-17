from datetime import datetime
from pathlib import Path
import os

import flask as f

# create the application object
app = f.Flask(__name__)

def _enabled(round):
    return os.path.exists(round)

def _enable(round):
    Path(round).touch()

def _disable(round):
    os.remove(round)

@app.route('/')
def welcome():
    return f.render_template('home.html')  # render a template

@app.route('/round1')
def round1():
    if (_enabled('round1')):
        return f.render_template('slothpops.html')
        
    return f.render_template('cheating.html')

@app.route('/round2')
def round2():
    if (_enabled('round2')):
        return f.render_template('hedgehog.html')
        
    return f.render_template('cheating.html')

@app.route('/admin')
def admin():
    status = {
        'round1': _enabled('round1'),
        'round2': _enabled('round2')
    }
    return f.render_template('admin.html', status=status)

@app.route('/toggle/<round>')
def toggle(round):
    if _enabled(round):
        _disable(round)
    else:
        _enable(round)
    
    return f.redirect(f.url_for('admin'))

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
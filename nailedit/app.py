from flask import Flask, render_template
from datetime import datetime

# create the application object
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('home.html')  # render a template

@app.route('/round1')
def round1():
    return render_template('slothpops.html')

@app.route('/round2')
def round2():
    return render_template('hedgehog.html')

@app.route('/round3')
def round3():
    return render_template('cheating.html')

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
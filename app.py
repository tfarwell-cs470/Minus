import os
from flask import render_template, redirect, url_for
app = Flask(__name__)

# Home page. Index link for all assignments
@app.route('/')
def index():
    return redirect(url_for('static', filename='index.html'))

# @app.route('/assignment<num>')
# def site(num):
#     return render_template('assignment{assignment{0}.html'.format(num))

if __name__ == '__main__':
   

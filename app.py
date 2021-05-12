from flask import Flask, render_template, request, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
import string
import random

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()

class Urls(db.Model):
    id = db.Column("id_", db.Integer, primary_key=True)
    long = db.Column("long", db.String())
    short = db.Column("short", db.String(5))

    def __init__(self, long, short):
        self.long = long
        self.short = short

    def __str__(self):
        return f'Long URL:{self.long}, short URL:{self.short}'

def shorten_url():
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_letters = random.choices(letters, k=5)
        rand_letters = "".join(rand_letters)
        short_url = Urls.query.filter_by(short=rand_letters).first()
        if not short_url:
            return rand_letters

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
      # first check if url is in db
        url_received = request.form["url"]
        found_url = Urls.query.filter_by(long=url_received).first()
        # return short url if found
        if found_url:
            return redirect(url_for("display_short_url", url=found_url.short))
        # if not found then create one
        else:
            short_url = shorten_url()
            print(short_url)
            new_url = Urls(url_received, short_url)
            db.session.add(new_url)
            db.session.commit()
            return redirect(url_for("display_short_url", url=short_url))
    else:
        return render_template('home.html')

@app.route('/<short_url>')
def redirection(short_url):
    long_url = Urls.query.filter_by(short=short_url).first()
    if long_url:
        return redirect(long_url.long)
    else:
        abort(404)

@app.route('/display/<url>')
def display_short_url(url):
    return render_template('shorturl.html', short_url_display=url)

@app.errorhandler(404)
def handle_404(self):
    return render_template('errors/404.html'), 404

@app.errorhandler(405)
def handle_400(self):
    return render_template('errors/405.html'), 405

@app.errorhandler(500)
def handle_500(self):
    return render_template('errors/500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
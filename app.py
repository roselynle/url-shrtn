from flask import Flask, render_template, request, redirect, url_for
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
        else:
            short_url = shorten_url()
            print(short_url)
            new_url = Urls(url_received, short_url)
            db.session.add(new_url)
            db.session.commit()
            return redirect(url_for("display_short_url", url=short_url))
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
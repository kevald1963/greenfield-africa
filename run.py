import os
from flask import Flask, render_template

SECRET_KEY = os.environ['SECRET_KEY']

app = Flask(__name__)
app.secret_key = SECRET_KEY

app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.config.from_object(__name__)


@app.route('/')
def index():
    return render_template("index.html", title="Home")


@app.route('/ourteam')
def ourteam():
    return render_template("index.html", title="Our Team")


@app.route('/ourpartners')
def ourpartners():
    return render_template("index.html", title="Our Partners")


@app.route('/ghana')
def ghana():
    return render_template("ghana.html", title="Ghana")


@app.route('/kenya')
def kenya():
    return render_template("kenya.html", title="Kenya")


@app.route('/malawi')
def malawi():
    return render_template("malawi.html", title="Malawi")


@app.route('/airpollution')
def airpollution():
    return render_template("airpollution.html", title="Air Pollution")


@app.route('/buildrefurb')
def buildrefurb():
    return render_template("buildrefurb.html", title="Building & Refurbishment")


@app.route('/medicalhealthcare')
def medicalhealthcare():
    return render_template("medicalhealthcare.html", title="Medical & Healthcare")


@app.route('/teachingorphanage')
def teachingorphanage():
    return render_template("teachingorphanage.html", title="Teaching & Orphanage Childcare")


@app.route('/sportscoaching')
def sportscoaching():
    return render_template("sportscoaching.html", title="Sports Coaching & Development")


@app.route('/musicdance')
def musicdance():
    return render_template("musicdance.html", title="Music, Dance & Art")


@app.route('/donate')
def donate():
    return render_template("donate.html", title="Donate")


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    host = "0.0.0.0"
    app.run(host=host, port=port, debug=True)

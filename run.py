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
    return render_template("ourteam.html", title="Our Team")


@app.route('/ourorganisation')
def ourorganisation():
    return render_template("ourorganisation.html", title="Our Organisation")


@app.route('/ghana')
def ghana():
    return render_template("ghana.html", title="Ghana")


@app.route('/kenya')
def kenya():
    return render_template("kenya.html", title="Kenya")


@app.route('/malawi')
def malawi():
    return render_template("malawi.html", title="Malawi")


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


@app.route('/feescosts')
def feescosts():
    return render_template("feescosts.html", title="Fees & Costs")


@app.route('/applytovolunteer')
def applytovolunteer():
    return render_template("applytovolunteer.html", title="Apply to Volunteer")


@app.route('/termsandconditions')
def termsandconditions():
    return render_template("termsandconditions.html", title="Terms and Conditions")


@app.route('/all_development')
def all_development():
    return render_template("development_funding/all_development.html", title="Development Funding")


@app.route('/dev_iddrisu_school')
def dev_iddrisu_school():
    return render_template("development_funding/ghana_development/dev_iddrisu_school.html", title="Iddrisu-Krom School Development")


@app.route('/dev_peki_tsame_school')
def dev_peki_tsame_school():
    return render_template("development_funding/ghana_development/dev_peki_tsame_school.html", title="Peki-Tsame School Development")


@app.route('/dev_refurbishment_after_flood')
def dev_refurbishment_after_flood():
    return render_template("development_funding/kenya_development/dev_refurbishment_after_flood.html", title="Greencard School Refurbishment")


@app.route('/donate')
def donate():
    return render_template("donate.html", title="Donate")


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    host = "0.0.0.0"
    app.run(host=host, port=port, debug=True)

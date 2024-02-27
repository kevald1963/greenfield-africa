import os
from flask import Flask, render_template

# import psycopg2
# import psycopg2.extras
# from datetime import datetime

# DB_NAME = os.environ['DB_NAME']
# DB_USER = os.environ['DB_USER']
# DB_PASS = os.environ['DB_PASS']
# DB_HOST = os.environ['DB_HOST']
SECRET_KEY = os.environ['SECRET_KEY']

app = Flask(__name__)
app.secret_key = SECRET_KEY

app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.config.from_object(__name__)


"""
def query(month, year):
    import calendar
    int_request_month = int(month)
    int_request_year = int(year)

    # Get the start and end days.
    start_day = "01"
    end_day = calendar.monthrange(int_request_year, int_request_month)[1]
    end_day = str(end_day)

    # Add a leading zero to month value if a single digit.
    if len(str(month)) == 1:
        this_month = "0" + str(month)
    else:
        this_month = str(month)

    this_year = year

    print("this_year = " + str(this_year))
    print("this_month = " + str(this_month))
    print("end_day = " + str(end_day))
    print("start_day = " + str(start_day))

    start_date = this_year + "-" + this_month + "-" + start_day
    end_date = this_year + "-" + this_month + "-" + end_day

    print("start_date = " + start_date)
    print("end_date = " + end_date)

    # conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    # print("PostgreSQL connection has been opened.")

    # curs = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    try:
        curs.execute(
            "SELECT title, "
            "       description, "
            "       to_char(event_date, 'DD/MM/YYYY') event_date, "
            "       to_char(event_time, 'HH24:MI') event_time, "
            "       EXTRACT(DAY FROM event_date) day_of_month "
            "FROM event "
            "WHERE event_date "
            "BETWEEN '" + start_date + "' "
            "AND '" + end_date + "' "
            "ORDER BY event_date"
        )

        result = curs.fetchall()
        dict_result = []

        for row in result:
            dict_result.append(dict(row))

        print("Requested events data successfully selected from database.")

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL: ", error)
    else:
        print("REQUESTED DATA PASSED TO TEMPLATE: " + str(dict_result))
        return dict_result

    finally:
        # Closing database connection.
        if conn:
            curs.close()
            conn.close()
            print("PostgreSQL connection has been closed.")


@app.route('/get-next-month/', endpoint='get-next-month', methods=['GET', 'POST'])
def getnextmonth():

    # Check if a request for next, or previous, month and year parameters.
    request_month = request.args.get("next-month")
    request_year = request.args.get("next-year")
    print("request_month = " + str(request_month))
    print("request_year = " + str(request_year))

    result = query(request_month, request_year)

    return jsonify(result)


@app.route('/calendar', defaults={'request_month': None, 'request_year': None})
@app.route('/calendar/<request_month>/<request_year>')
def calendar(request_month, request_year):
    import calendar
    start_day = "01"

    if request_month is None:

        # This is a default calendar request, so set the start and end dates for the current month.
        this_year = datetime.now().year
        this_month = datetime.now().month
        end_day = str(calendar.monthrange(this_year, this_month)[1])

        this_year = str(this_year)
        this_month = str(this_month)

        # Add a leading zero to month value if a single digit.
        if len(this_month) == 1:
            this_month = "0" + this_month
    else:
        # If a valid request has been made, use the input parameters to set the start and end date
        # parameters prior to running the query on the Events table.

        print("GOT HERE")
        int_request_year = int(request_year)
        int_request_month = int(request_month)

        end_day = calendar.monthrange(int_request_year, int_request_month)[1]
        end_day = str(end_day)

        # Add a leading zero to month value if a single digit.
        if len(str(request_month)) == 1:
            this_month = "0" + str(request_month)
        else:
            this_month = str(request_month)

        this_year = request_year

    print("this_year = " + str(this_year))
    print("this_month = " + str(this_month))
    print("end_day = " + str(end_day))
    print("start_day = " + str(start_day))

    start_date = this_year + "-" + this_month + "-" + start_day
    end_date = this_year + "-" + this_month + "-" + end_day

    print("start_date = " + start_date)
    print("end_date = " + end_date)

    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    print("PostgreSQL connection has been opened.")

    curs = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    try:
        curs.execute(
            "SELECT title, "
            "       description, "
            "       to_char(event_date, 'DD/MM/YYYY') event_date, "
            "       to_char(event_time, 'HH24:MI') event_time, "
            "       EXTRACT(DAY FROM event_date) day_of_month " 
            "FROM event "
            "WHERE event_date "
            "BETWEEN '" + start_date + "' "
            "AND '" + end_date + "' "
            "ORDER BY event_date"
        )

        result = curs.fetchall()
        dict_result = []

        for row in result:
            dict_result.append(dict(row))

        print("Events data successfully selected from database.")

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL: ", error)
    else:
        print("END DAY PASSED TO TEMPLATE: " + str(end_day))
        print("DATA PASSED TO TEMPLATE: " + str(dict_result))
    finally:
        # Closing database connection.
        if conn:
            curs.close()
            conn.close()
            print("PostgreSQL connection has been closed.")
"""


@app.route('/')
def index():
    return render_template("index.html", title="Home")


@app.route('/ourteam')
def ourteam():
    return render_template("index.html", title="Our Team")


@app.route('/ourpartners')
def ourpartners():
    return render_template("index.html", title="Our Partners")


@app.route('/newcastle')
def newcastle():
    return render_template("newcastle.html", title="Newcastle")


@app.route('/gateshead')
def gateshead():
    return render_template("gateshead.html", title="Gateshead")


@app.route('/northtyneside')
def northtyneside():
    return render_template("northtyneside.html", title="North Tyneside")


@app.route('/southtyneside')
def southtyneside():
    return render_template("southtyneside.html", title="South Tyneside")


@app.route('/sunderland')
def sunderland():
    return render_template("sunderland.html", title="Sunderland")


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
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)

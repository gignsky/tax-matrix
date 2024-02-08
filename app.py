from flask import Flask, render_template
import src

counties = src.county_data.counties.get_counties()
Subject = src.subject.Subject()

app = Flask(__name__)


@app.route("/")
def introduction():
    return render_template(
        "introduction.html",
        version=src.config.current_version(),
        update_date=src.config.date_revised(),
    )

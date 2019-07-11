import os
from bottle import route, run, view
from datetime import datetime as dt
from random import random
from horoscope import generate_prophecies

@route("/")
@view("predicions")

def index():
	now = dt.now()
	x = random()
	predicions = generate_prophecies()

	return {
			"date": f"{now.year} - {now.month} - {now.day}",
			"predicions" : predicions,
			"spetial_date": x>0.5,
			"x":x 
			}
@route("/api")
def api_test():
	return {
			"something":"Привет!"
	}

if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(
	host="localhost",
	port=8080,
	autoreload=True

)


import flask
from flask import request
import config
import json
import logging
import lat_lon_parser
###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY
leaflet_key = CONFIG.ACCESS_TOKEN
locations = CONFIG.LOCATIONS
###
# Pages
###


@app.route("/")
@app.route("/index")
def index():
    return flask.render_template('index.html', api = leaflet_key )
    #send leaflet key to index

@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('404.html'), 404


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_interest_points")
def _display_locations():
    """
    a descriptiob here
    """
    app.logger.debug("Got a JSON request")
    #change to load from config
    app.logger.debug("Processing the location")
    location_data = lat_lon_parser.process(locations)
    return json.dumps(location_data)


#############

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")

import flask
import requests
import muambator_urls
from bs4 import BeautifulSoup

from flask_cors import CORS


app = flask.Flask(__name__)
CORS(app=app)

@app.get("/")
def welcome_msg():
    return flask.jsonify({"message": "Hi curious."})

@app.route("/api/v1/search-tracking-code", methods=["GET"])
def search_tracking_code():
    s = requests.Session()
    tracking_code = "NL525245714BR"
    s.get(muambator_urls.home)
    pacote_page = s.get(muambator_urls.pacote_info.replace("[tracking_code]", tracking_code))
    print(pacote_page.text)
    return pacote_page.text

app.run("localhost", port=1337)
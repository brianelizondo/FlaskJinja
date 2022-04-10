from crypt import methods
from distutils.log import debug
from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "abcd1234"
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    """Return homepage with story form"""
    return render_template("home.html")

@app.route('/story', methods=["POST"])
def show_story():
    """Receive data from the form, generate the story object and send the story text result to the template story.html"""
    place = request.form["place"]
    noun = request.form["noun"]
    verb = request.form["verb"]
    adjective = request.form["adjective"]
    plural_noun = request.form["plural_noun"]

    story_text = story.generate({"place": place, "noun": noun, "verb": verb, "adjective": adjective, "plural_noun": plural_noun})
    return render_template("story.html", story=story_text)
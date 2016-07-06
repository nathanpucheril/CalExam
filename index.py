from flask import Flask
from flask import render_template
from flask import request
from Core.DB import search_class
from Core.DB import update_db
import json
import ast
from bson.json_util import loads
import os
from threading import Timer

app = Flask(__name__)
APP_TITLE = "Cal Exam Archive"
PORT = int(os.environ.get('PORT', 5000))# For Heroku


@app.route("/")
def index():
    query = request.args.get("search")
    if query:
        query = query.lower()
    results = search_class(query)
    # results = ""

    title = "{main}{bar}{query}".format(main=APP_TITLE,
                                        query=query if query else "",
                                        bar=" | " if query else "")

    print("Render Index")
    return render_template("index.html",
                           title=title,
                           suggestion1="CS 61A",
                           suggestion2="Math 53",
                           suggestion3="Physics 7A",
                           suggestion4="EE 20",
                           results_json=results
                           )


@app.route("/attribution")
def attribution():
    return render_template("attribution.html",
                           title="{main} | Attribution".format(main=APP_TITLE))




if __name__ == '__main__':
    # app.run(debug=True, port=PORT)
    app.run(host='0.0.0.0', port=PORT)

# def interval():
#     update_db()
#     Timer(600, interval).start()
# interval()

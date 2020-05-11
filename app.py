from flask import Flask,render_template,request,redirect, url_for, jsonify, g
from datetime import datetime
from covid import covid
import os

app = Flask(__name__) 



def file_loader():
    if 'lines' not in g:
        with open('indian_states.txt') as f:
          g.lines = f.read().splitlines()
    return g.lines

@app.route("/")
def covidHome():
    list_states = file_loader()
    get_state = request.args.get('state', default='Tamil Nadu')
    covid19 =  covid(get_state,None)
    data = covid19.getStateData()["districtData"]
    return render_template("covidtable.html", Statedata = data, State = get_state, Statelist = list_states)

@app.route("/covid")
def covidstat():
    State = "Tamil Nadu"
    District = "Chennai"
    covid19 =  covid(State,District)
    data = covid19.getChennaiData()
    return render_template("covid19.html", data = data, District=District, State =State)

@app.route("/covid/<string:state>/<string:district>")
def covidstats(state,district):
    State = state.title()
    District = district.title()
    covid19 =  covid(State,District)
    data = covid19.getChennaiData()
    return render_template("covid19.html", data = data, District=District, State =State)

# New functions
@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(threaded=True,host='0.0.0.0')

from flask import Flask,render_template,request,redirect, url_for, jsonify
from datetime import datetime
from covid import covid

app = Flask(__name__) 

@app.route("/")
@app.route("/<State>")
def covidHome(State="Tamil Nadu",District="Chennai"):
    covid19 =  covid(State,None)
    data = covid19.getStateData()["districtData"]
    return render_template("covidtable.html", Statedata = data, State =State)

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

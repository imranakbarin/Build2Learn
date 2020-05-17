from flask import Flask,render_template,request,redirect, url_for, jsonify, g, send_from_directory
from datetime import datetime
from covid import covid
import os

app = Flask(__name__) 

#Load states from a text file once the app gets loaded
lines = ''
teamdetails= ''
with app.app_context():
    with open('indian_states.txt') as f,open("team_members.txt") as f2:
          lines = f.read().splitlines()
          teamdetails = f2.read().splitlines()
                
#Method whenever there is a error in page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error-404.html')

#A tiny page with Stayhome message
@app.route("/stayhome")
def stayhome():
    return render_template('stayhome.html') 

#Main route for loading the First page, it loads default state first
@app.route("/")
def covidHome():
    list_states = lines
    totaldictionary = {}
    get_state = request.args.get('state', default='Tamil Nadu')
    covid19 =  covid(get_state,None)
    data = covid19.getStateData()["districtData"]
    totaldictionary = covid19.totalstats(data)
    return render_template("covidtable.html", Statedata = data, State = get_state, totalstats = totaldictionary, Statelist = list_states)

#Route for chennai related Stats
@app.route("/covid")
def covidstat():
    State = "Tamil Nadu"
    District = "Chennai"
    covid19 =  covid(State,District)
    data = covid19.getChennaiData()
    return render_template("covid19.html", data = data, District=District, State =State)

#Route for State and District related stats passed in URL
@app.route("/covid/<string:state>/<string:district>")
def covidstats(state,district):
    State = state.title()
    District = district.title()
    covid19 =  covid(State,District)
    data = covid19.getChennaiData()
    return render_template("covid19.html", data = data, District=District, State =State)

# About Page
@app.route("/about/")
def about():
    #sort the teamdetails
    return render_template("about.html", teamlist=teamdetails)

#Contact Page
@app.route("/contact/")
def contact():
    return render_template("contact.html")

#Sitemap
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

#A tiny page with Stayhome message
@app.route("/test")
def test():
    return render_template('hello_there.html') 


if __name__ == "__main__":
    app.run(threaded=True,host='0.0.0.0')
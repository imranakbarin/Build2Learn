from flask import Flask,render_template,request,redirect, url_for, jsonify, g, send_from_directory, flash
from datetime import datetime
from covid import covid
from forms import LoginForm, RegistrationForm
from newsapi import NewsApiClient
import os

app = Flask(__name__) 

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

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


#Formatting Filter
@app.template_filter()
def comafy(value):
    value = int(value)
    return "{:,}".format(value)


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

#testing some features in this route
@app.route("/test")
def test():
    list_states = lines
    totaldictionary = {}
    get_state = request.args.get('state', default='Tamil Nadu')
    covid19 =  covid(get_state,None)
    data = covid19.getStateData()["districtData"]
    totaldictionary = covid19.totalstats(data)
    return render_template("hello_there.html", Statedata = data, State = get_state, totalstats = totaldictionary, Statelist = list_states)


@app.route("/")
def statewisereport():
    covid19 = covid(None,None)
    statewisedata = covid19.getstatewiseresults()
    return render_template('statewisereport.html',statedatalist = statewisedata)
    

#Main route for loading the First page, it loads default state first
@app.route("/district")
def covidHome():
    list_states = lines
    totaldictionary = {}
    get_state = request.args.get('state', default='Tamil Nadu')
    covid19 =  covid(get_state,None)
    data = covid19.getStateData()["districtData"]
    totaldictionary = covid19.totalstats(data)
    return render_template("covidtable.html", Statedata = data, State = get_state, totalstats = totaldictionary, Statelist = list_states)

#Hiral Global Covid Stats Changes
@app.route("/global")
def countrywisereport():
    covid19 = covid(None, None)
    data = covid19.covidGlobal()
    globalDataList = data["Global"]
    countrywisedata = data["Countries"]
    return render_template('countrywisereport.html', globalData = globalDataList, countrydatalist=countrywisedata)


#End of Global stats changes



#News API

@app.route("/news")
def newspage():
    try:
        api = NewsApiClient(api_key=NEWS_API_KEY)
        top_headlines = api.get_top_headlines(country='in',
                                            language='en')
        return render_template('news.html', headlines = top_headlines)
    except:
        return "<H2> Issue Fetching News - We will Look into it soon </H2>"

@app.route("/Login", methods=['GET','POST'])
def Login():
    form = LoginForm()  
    if form.validate_on_submit():
        if form.UserName.data == 'Alagappan' and form.Password.data == '123456':
            flash('You have been logged in!', 'success')
            return redirect(url_for('covidHome'))            
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template("Login.html", title='Login', form=form)

@app.route("/Register",methods=['GET','POST'])
def Register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('Login'))
    return render_template("Register.html", title='Register', form=form)

if __name__ == "__main__":
    app.run(threaded=True,host='0.0.0.0')

from flask import Flask,render_template,request,redirect, url_for, jsonify, send_from_directory, flash, json
from datetime import datetime
from covid import covid
# from forms import LoginForm, RegistrationForm
from newsapi import NewsApiClient
from collections import OrderedDict 
from operator import getitem 
import os
import codecs
from itertools import groupby

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

#Below Method does formating of numbers to Indian Numbering format
def format_as_indian(input):
    input_list = list(str(input))
    if len(input_list) <= 1:
        formatted_input = input
    else:
        first_number = input_list.pop(0)
        last_number = input_list.pop()
        formatted_input = first_number + (
            (''.join(l + ',' * (n % 2 == 1) for n, l in enumerate(reversed(input_list)))[::-1] + last_number)
        )

        if len(input_list) % 2 == 0:
            formatted_input.lstrip(',')

    return formatted_input

#Formatting Filter
@app.template_filter()
def comafy(value):
    try:
        value = int(value)
        return format_as_indian(value)
    except:
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
    # return render_template("chennaizonewise.html")

#Route for Chennai Page
@app.route("/chennai")
def chennaizonalreport():
    covid19 = covid(None,None)
    try:
        response = covid19.getChennaizones()
        #Fetching the Date from first key
        FormattedDate = datetime.strptime(response[0]['date'].strip(), "%Y-%m-%d").strftime("%A, %d %b %Y")
        zones_chennai = response[:16]
        zones_chennaiOneday = response[16:32]
        Last_twentydays = response[:16*30]
        #Chennai Data Charts
        Chennai_dict = {}
        chennai_date = []
        chennai_confirmed = []
        chennai_recovered = []
        chennai_hospitalized = []
        chennai_deceased =[]
        for k,v in groupby(Last_twentydays,key=lambda x:x['date'].strip()):
                tot1 =tot2 = tot3 = tot4 = 0
            #  Chennai_dict[k] = sorted(list(v),key=lambda x: datetime.strptime(x['date'].strip(), '%Y-%m-%d'))
                for item in v:
                    tot1 += item['confirmedCases']
                    tot2 += item['recovered']
                    tot3 += item['hospitalized']
                    tot4 += item['deceased']
                chennai_confirmed.append(tot1)
                chennai_recovered.append(tot2)
                chennai_hospitalized.append(tot3)
                chennai_deceased.append(tot4)
                chennai_date.append(datetime.strptime(k.strip(), "%Y-%m-%d").strftime("%b %d")) 
                
        #To Reverse  
        Chennai_dict['date'] = chennai_date[::-1]
        Chennai_dict['confirmedCases'] = chennai_confirmed[::-1]
        Chennai_dict['recovered'] = chennai_recovered[::-1]
        Chennai_dict['hospitalized'] = chennai_hospitalized[::-1]
        Chennai_dict['deceased'] = chennai_deceased[::-1]
       #Area Wise Charts data 
        dict_list = {}        
        Last_twentydays.sort(key=lambda x:x['zoneName'])
    
        for k,v in groupby(Last_twentydays,key=lambda x:x['zoneName']):
             dict_list[k] = sorted(list(v),key=lambda x: datetime.strptime(x['date'].strip(), '%Y-%m-%d'))

        #  zones_list = list(zones_chennai['zoneName'].values())
        zones_list = [zones_list['zoneName'].capitalize() for zones_list in zones_chennai]
        active_list = [active_list['hospitalized'] for active_list in zones_chennai]
        recovered_list = [recovered_list['recovered'] for recovered_list in zones_chennai]
        deceased_list =  [deceased_list['deceased'] for deceased_list in zones_chennai]
        
        # active_list1, recovered_list1, deceased_list1 = [] 
        active_list1 = [active_list1['hospitalized'] for active_list1 in zones_chennaiOneday]
        recovered_list1 = [recovered_list1['recovered'] for recovered_list1 in zones_chennaiOneday]
        deceased_list1 =  [deceased_list1['deceased'] for deceased_list1 in zones_chennaiOneday]
        
        return render_template('chennaizonewise.html', onlychennai_data = Chennai_dict,chennaidata = zones_chennai, formatteddate = FormattedDate,
                               zones_list=zones_list,active_list=active_list,recovered_list=recovered_list,
                               deceased_list=deceased_list,fivedaysstat = dict_list, active_list1 = active_list1, 
                           recovered_list1 = recovered_list1, deceased_list1 = deceased_list1   )
    except Exception as e:
		# return 404 page if error occurs
        print("error in chennai route " + e)         
        return render_template("error-404.html")

@app.route("/")
def statewisereport():
    covid19 = covid(None,None)
    # Sorting state wise data according to the active cases
    statewisedata = (sorted(covid19.getstatewiseresults(), key = lambda i: int(i['active']),reverse=True))
    return render_template('statewisereport.html',statedatalist = statewisedata)
    

#StateWise Page Route
@app.route("/district")
def covidHome():
    list_states = lines
    totaldictionary = {}
    try:
        get_state = request.args.get('state', default='Tamil Nadu')
        covid19 =  covid(get_state,None)
        data = covid19.getStateData()["districtData"]
        # Data Sorting as per the number of active cases
        sorted_data = OrderedDict(sorted(data.items(), 
        key = lambda x: getitem(x[1], 'active'), reverse=True)) 
        totaldictionary = covid19.totalstats(data)
        return render_template("covidtable.html", Statedata = sorted_data, State = get_state, totalstats = totaldictionary, Statelist = list_states)
    except Exception as e:
        print(e)
        return render_template("error-404.html")

#Hiral Global Covid Stats Changes
@app.route("/global")
def countrywisereport():
    covid19 = covid(None, None)
    try:
        data = covid19.covidGlobal()
        globalDataList = data["Global"]
        countrywisedata = data["Countries"]
        for countries in countrywisedata:
            countries['TotalActive']=(countries['TotalConfirmed'] - countries['TotalDeaths'] - countries['TotalRecovered'])
        return render_template('countrywisereport.html', globalData = globalDataList, countrydatalist=countrywisedata)
    except Exception as e:
		# return 404 page if error occurs 
	    return render_template("error-404.html")

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
        return render_template("error-404.html")
    
  
#Chennai Street wise
@app.route("/chennaicovidlist")
def chennaistreetwise():
     StreetChennaiCovid = covid(None, None) 
     try:
        # with codecs.open('static/json/chennai_data_11.json','r', 'utf-8-sig') as f:
        #     chennaidata = json.load(f)
        Chennai_Data = StreetChennaiCovid.getChennaiStreet()
        chennaiStreetData = Chennai_Data['chennaidata'];
       # print(chennaiStreetData)
        Datetitle = Chennai_Data['title'];
        return render_template('chennaicovidlist.html', chennailist = chennaiStreetData, datetitle = Datetitle)      
     except Exception as e:
        print(e)
        return render_template("error-404.html")
    
    
#Chennai API Section

@app.route('/api/chennaizones/cases', methods = ['GET']) 
def ChennaiZoneCases(): 
     covid19 = covid(None,None)
     try:
        response = covid19.getChennaizones()
        return jsonify({"success": True, "cases":response})
     except Exception as e:
        print(e)
        return jsonify({"success": False})

@app.route('/api/chennaiStreet/daily', methods = ['GET']) 
def ChennaiStreetwiseCases(): 
     covid19 = covid(None,None)
     try:
        response = covid19.getChennaiStreet()
        
     
        return jsonify({"success": True, "title": response['title'], "chennaidata":response['chennaidata']})
     except Exception as e:
        print(e)
        return jsonify({"success": False})



if __name__ == "__main__":
    app.run(threaded=True,host='0.0.0.0')

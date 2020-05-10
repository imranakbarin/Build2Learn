import requests
import json

tndata = None
def callApi(url,params):
    res = requests.get(url, params)
    data = res.json()
    return data

def covidStats():
    url = "https://api.covid19india.org/state_district_wise.json"
    data = callApi(url,params=None)
    tndata = data["Tamil Nadu"]['districtData']
    for data in tndata:
      StatewiseData = tndata[data]
      print(f"District {data} Active {StatewiseData['active']} Confirmed {StatewiseData['confirmed']} Deceased {StatewiseData['deceased']} recovered {StatewiseData['recovered']}")
     



covidStats()
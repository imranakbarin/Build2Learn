import requests
import json

tndata = None
def callApi(url,params):
    res = requests.get(url, params)
    data = res.json()
    return data

StatewiseData = None
def covidStats():
    url = "https://api.covid19india.org/state_district_wise.json"
    data = callApi(url,params=None)
    print(data)
    tndata = data["Tamil Nadu"]['districtData']
    for data in tndata:
      StatewiseData = tndata[data]
      print(f"District {data} Active {StatewiseData['active']} Confirmed {StatewiseData['confirmed']} Deceased {StatewiseData['deceased']} recovered {StatewiseData['recovered']}")
     


def covidStateWise():
    url = "https://api.covid19india.org/state_district_wise.json"
    data = callApi(url,params=None)
    print(data)
    #tndata = data["Tamil Nadu"]['districtData']
    with open("indian_states.txt", "a") as f:
        for datastate in data:
             print(datastate, file=f)
      

covidStateWise()
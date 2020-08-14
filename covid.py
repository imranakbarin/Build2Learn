import requests
import requests_cache
from datetime import datetime

requests_cache.install_cache(expire_after=60)

class covid():
    tndata = None
    totalsum = None
    def __init__(self, state, district):
        self.tndata = None
        self.state = state
        self.district = district
        self.totalsum ={'active':0,'confirmed':0,'deceased':0,
                        'recovered':0,'deltaconfirmed':0,
                        'deltadeceased':0, 'deltarecovered':0 }

    def callApi(self, url, params):
        res = requests.get(url, params)
        data = res.json()
        return data

    def covidStats(self, Notsure):
        url = "https://api.covid19india.org/state_district_wise.json"
        data = self.callApi(url, params=None)
        return data
        # print(res.json())

    def covidGlobal(self):
        url = "https://api.covid19api.com/summary"
        data = self.callApi(url, params=None)
        return data
        
    def totalstats(self,statedata):
         for data in statedata:
            StatewiseData = statedata[data]
            self.totalsum['active'] += StatewiseData['active']
            self.totalsum['confirmed'] += StatewiseData['confirmed']
            self.totalsum['deceased'] += StatewiseData['deceased']
            self.totalsum['recovered'] += StatewiseData['recovered']
            self.totalsum['deltaconfirmed'] += StatewiseData['delta']['confirmed']
            self.totalsum['deltadeceased'] += StatewiseData['delta']['deceased']
            self.totalsum['deltarecovered'] += StatewiseData['delta']['recovered']
         return self.totalsum
     
    def getStateData(self):
        jsonData = self.covidStats(None)
        self.tndata = jsonData[self.state]
 #       if self.tndata:
 #           self.totalstats(self.tndata["districtData"])
        return self.tndata
    
    def stateWiseData(self):
        url = "https://api.covid19india.org/v2/state_district_wise.json"
        response = self.callApi(url, params=None)
        return response


    def getChennaiData(self):
        Chennaidata = self.getStateData()
        return Chennaidata["districtData"][self.district]
    
    
    def getstatewiseresults(self):
        url ="https://api.covid19india.org/data.json"
        data = self.callApi(url,None)
        return data['statewise']
    
    
#Chennai Zonal Wise Data

    def getChennaizones(self):
        url = "https://v2-api.sheety.co/9b810596b61530e455e40ea4e0b5a1a1/chennaiCovid19/cases"
        data = self.callApi(url,None)
        #Sorting data using date
        sorted_data = sorted(data['cases'], key=lambda x: datetime.strptime(x['date'].strip(), '%Y-%m-%d'), reverse = True)
        return sorted_data
    
    def getChennaiStreet(self):
        url = "https://v2-api.sheety.co/9b810596b61530e455e40ea4e0b5a1a1/chennaiCovid19/chennaidata"
        data = self.callApi(url,None)
        #Sorting data using date 
        return data['chennaidata']

#really dont want the title to be stored in separate Json, Need to find a way
    def getDatetitle(self):
        url = "https://v2-api.sheety.co/9b810596b61530e455e40ea4e0b5a1a1/chennaiCovid19/title"
        data = self.callApi(url,None)
        #Sorting data using date
        return data['title']
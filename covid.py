import requests
import requests_cache

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


    def getChennaiData(self):
        Chennaidata = self.getStateData()
        return Chennaidata["districtData"][self.district]

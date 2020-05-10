import requests
import requests_cache

requests_cache.install_cache(expire_after=60)

class covid():
    tndata = None
    def __init__(self, state,district):
        self.tndata = None
        self.state = state
        self.district = district
     
    def callApi(self,url,params):
         res = requests.get(url, params)
         data = res.json()
         return data

    def covidStats(self, Notsure):
        url = "https://api.covid19india.org/state_district_wise.json"
        data = self.callApi(url,params=None)
        return data
        #print(res.json())

    def getStateData(self):
        jsonData = self.covidStats(None)
        self.tndata = jsonData[self.state]
        return self.tndata
#        print(self.tndata)

    def getChennaiData(self):
         Chennaidata = self.getStateData()
         return Chennaidata["districtData"][self.district]
        


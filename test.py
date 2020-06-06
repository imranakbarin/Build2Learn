import requests
import json
import collections, functools, operator 
from datetime import datetime
from statecodes import ConstCodes

tndata = None
arcgisDistrictUrl = 'https://services9.arcgis.com/HwXIp55hAoiv6DE9/ArcGIS/rest/services/District_Wise_Covid_19_Status_view/FeatureServer/0/query';

filterarcgis = '?where=1%3D1&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=standard&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=Name%2C+Positive_Cases%2C+Active_Cases%2C+Recovered%2C+Death%2C+Last_Updated_Date&returnGeometry=true&returnCentroid=false&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=json&token='
def callApi(url,params):
    res = requests.get(url, params)
    data = res.json()
    return data

StatewiseData = None
def covidStats():
    url = "https://api.covid19india.org/state_district_wise.json"
    data = callApi(url,params=None)
    #print(data)
    tndata = data["Tamil Nadu"]['districtData']
    print(type(tndata))
    #print(tndata)
   
 
    #sumValue1 = sum(d['active'] for d in tndata.values() if d) 

   # sumValue2 = sum(d['confirmed'] for d in tndata.values() if d)

    #print(sumValue1) 
   # print(sumValue2) 

    #for data in tndata.values():
      # print("Data ", data['active'])
 

   # totalsum = dict()
    #for k,v in tndata.items():
        #totalsum[k]= v + totalsum.get(k,0)
   #     totalsum[k] += v 
   #     print("Key ",k)
   #     print("Value ",v)
 
#  $env:NEWS_API_KEY='b96f7eb8844a4cb08d8f31ab2dc40f3a'
 
    #print(totalsum)
    totalsum ={'active':0,'confirmed':0,'deceased':0,'recovered':0,'deltaconfirmed':0,
              'deltadeceased':0, 'deltarecovered':0 }
   
    for data in tndata:
      StatewiseData = tndata[data]
      totalsum['active'] += StatewiseData['active']
      totalsum['confirmed'] += StatewiseData['confirmed']
      totalsum['deceased'] += StatewiseData['deceased']
      totalsum['recovered'] += StatewiseData['recovered']
      print(f"District {data} Active {StatewiseData['active']} Confirmed {StatewiseData['confirmed']} Deceased {StatewiseData['deceased']} recovered {StatewiseData['recovered']}")
      print(f" {StatewiseData['delta']} ")
    print(f"total  Confirmed {totalsum['deltaconfirmed']} Deceased {totalsum['deltadeceased']} recovered {totalsum['deltadeceased']}")
    



def covidStateWise():
    url = "https://api.covid19india.org/state_district_wise.json"
    data = callApi(url,params=None)
    print(data)
    #tndata = data["Tamil Nadu"]['districtData']
    with open("indian_states.txt", "a") as f:
        for datastate in data:
             print(datastate, file=f)
      
token =''
#print(callApi(arcgisDistrictUrl + filterarcgis + token,None ))

#covidStateWise()

def callingGlobal():
    url = "https://covid19.mathdro.id/api/countries/india"
    data = callApi(url,None)
    print(f"Confirmed {data['confirmed']['value']} Recovered {data['recovered']['value']}  Deaths {data['deaths']['value']}")
   # print(datetime.strptime(data['lastUpdate'], "%Y-%m-%dT%H:%M:%S.%fZ"))
    timestamp = datetime.fromtimestamp(1590058974)
    print(timestamp.strftime('%Y-%m-%d %H:%M:%S'))
    print(data)
    
    
def getstatewiseresults():
    url ="https://api.covid19india.org/data.json"
    data = callApi(url,None)
    #print(f"{data['statewise']}")
    for everystate in data['statewise']:
        print(f"\r {everystate['state']}")
    
    
    
    
    
getstatewiseresults()
#print(ConstCodes.getstatecodes())
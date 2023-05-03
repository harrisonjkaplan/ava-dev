import requests, json
from custom_exception import CustomException
from helpers import coordsSmasher,coordsString,countString, getString

#takes calculated coordinates are runs elevation api 
#number of coordinates per call is limited so have to run it in batches
class ElevationGetter:
    def __init__(self,yS,xS):
        self.xS = xS
        self.yS = yS 


    def getElevation(self):
        elevations = [] 
        s2Array = coordsString(self.yS, self.xS)
        x = int(countString(s2Array))

        for i in range(x):
            s = getString(s2Array[i])
            r = requests.get('https://maps.googleapis.com/maps/api/elevation/json?locations=' + s + '&key=AIzaSyBgGmmlQPovPRX4mwC1itn0oih8I15d3IE')
            data = r.json()
            if r.status_code == 400:
                if 'error_message' in data:
                    raise CustomException(data['error_message'])
                else:
                    raise CustomException(json.dumps(data))
            elevation_dict = json.loads(r.text)
            for j in range(len(s2Array[i])):
                elevation = data["results"][j]["elevation"]
                elevations.append(int(elevation))
    
        return elevations
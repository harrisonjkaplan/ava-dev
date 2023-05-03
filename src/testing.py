import requests
from coord_field import CoordField
from haversine import haversine, Unit


# url = "https://ava-iimm3tykgq-uc.a.run.app/coordinate?h=1&r=1&s=.1&longitudeCoord=37&latitudeCoord=82"
# url_test = "http://127.0.0.1:5000/testAPI?h=1&r=1&s=.1&longitudeCoord=37&latitudeCoord=82"

# payload={}
# headers = {
#   'x-api-key': 'Av@Ap1K3y'
# }

# response = requests.request("GET", url_test, headers=headers, data=payload)
# print(len(response.text))
# print(response.text)
cf = CoordField(0,89,1,.1)
cf.fillField()
# print(cf.xList)
# print(cf.yList)

print(len(cf.xList))
print(haversine((cf.xList[0],cf.yList[0]),(cf.xList[1],cf.yList[1])))
print(haversine((cf.xList[1],cf.yList[1]),(cf.xList[2],cf.yList[2])))
print(haversine((cf.xList[0],cf.yList[0]),(cf.xList[19],cf.yList[19])))



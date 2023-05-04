import requests
from coord_field import CoordField
from haversine import haversine, Unit, inverse_haversine, Direction
import math



# url = "https://ava-iimm3tykgq-uc.a.run.app/coordinate?h=1&r=1&s=.1&longitudeCoord=37&latitudeCoord=82"
# url_test = "http://127.0.0.1:5000/testAPI?h=1&r=1&s=.1&longitudeCoord=37&latitudeCoord=82"

# payload={}
# headers = {
#   'x-api-key': 'Av@Ap1K3y'
# }

# response = requests.request("GET", url_test, headers=headers, data=payload)
# print(len(response.text))
# print(response.text)
cf = CoordField(15,-15,3,1)
cf.fillField()
# print(cf.xList)
# print(cf.yList)

print(len(cf.longitude_list))

d = haversine((cf.latitude_list[0],cf.longitude_list[0]),(cf.latitude_list[1],cf.longitude_list[1]))
print(d)
# print(haversine((cf.latitude_list[1],cf.longitude_list[1]),(cf.latitude_list[2],cf.longitude_list[2])))
# print(haversine((cf.latitude_list[0],cf.longitude_list[0]),(cf.latitude_list[5],cf.longitude_list[5])))

# diff = abs(d - .05)
# print(diff)

# print(f"latitude value: {cf.latitude_list[12]} longitude value: {cf.longitude_list[12]}")


for i in range(len(cf.latitude_list)):
    print(f"({cf.longitude_list[i]},{cf.latitude_list[i]})")
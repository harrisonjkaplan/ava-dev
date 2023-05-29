
import os
import traceback

from custom_exception import CustomException
from olympus import Olympus
from olympians import Olympians 
from analytics import Analytics
from flask import Flask, request, jsonify

app = Flask(__name__)

# # API_KEY = os.environ.get('AVA_API_KEY')

# @app.before_request
# def before_request():
#     # header_api_key = request.headers.get('x-api-key', None)

#     # # Check if API key header is present
#     # if header_api_key is None:
#     #     return jsonify(message = "x-api-key header is missing"), 400

#     # # Verify API key
#     # if header_api_key != API_KEY:
#     #     return jsonify(message = "Unauthorized"), 401

@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = '*'
    header['Access-Control-Allow-Methods'] = '*'
    return response


@app.route('/coordinate', methods=['GET'])
def generate_result():
    try:
        h = request.args.get('h', default=1, type=float)
        r = request.args.get('r', default=1, type=float)
        s = request.args.get('s', default=.1, type=float)
        longitudeCoord = request.args.get('longitudeCoord', default=0, type=int)
        latitudeCoord = request.args.get('latitudeCoord', default=0, type=int)
        
        print(f'h: {h}, r: {r}, s:{s}, longitudeCoord:{longitudeCoord}, latitudeCoord:{latitudeCoord}')
        oly = Olympus(longitudeCoord,latitudeCoord,h,r,s)
        areas = oly.multH(0,15)
        heights = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

        returnList = oly.getAPIReturnList()
        print(returnList)
        
        # oly.visualize(areas,heights)

        ana = Analytics(r,h,s,oly.fam)
        ana.calc_view_areas()
        return jsonify(result = returnList), 200
    except CustomException as ce:
        return jsonify(message = ce.message), 400
    except Exception as e:
        pyback.print_exc()
        return jsonify(message = "something went wrong"), 500


@app.route('/testAPI', methods=['GET'])
def generate_result2():
    try:
        h = request.args.get('h', default=1, type=float)
        r = request.args.get('r', default=1, type=float)
        s = request.args.get('s', default=.1, type=float)
        longitudeCoord = request.args.get('longitudeCoord', default=0, type=int)
        latitudeCoord = request.args.get('latitudeCoord', default=0, type=int)
        
        print(f'h: {h}, r: {r}, s:{s}, longitudeCoord:{longitudeCoord}, latitudeCoord:{latitudeCoord}')
        oly = Olympus(longitudeCoord,latitudeCoord,h,r,s)
        areas = oly.multH(0,15)
        heights = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

        returnList = oly.getAPIReturnList()
        print(returnList)
        
        # oly.visualize(areas,heights)

        ana = Analytics(r,h,s,oly.fam)
        ana.calc_view_areas()
        returnMessage = "this is a test of the new api"
        returnTestList = [returnList, returnMessage]
        return jsonify(result = returnTestList), 200
    except CustomException as ce:
        return jsonify(message = ce.message), 400
    except Exception as e:
        traceback.print_exc()
        return jsonify(message = "something went wrong"), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

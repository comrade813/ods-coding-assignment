import json
from flask import Flask, jsonify
from database import DB

from sql import SELECT_ALL_AIRPORTS, \
                SELECT_FLIGHTS_FROM_ORIGIN, \
                SELECT_FLIGHTS_TO_DESTINATION, \
                SELECT_FLIGHTS_FROM_ORIGIN_TO_DESTINATION

from error import BAD_ORIGIN, \
                  BAD_DESTINATION, \
                  NO_AIRPORT_CHOSEN, \
                  DB_QUERY_ERR

from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config.from_pyfile('settings.py')
from settings import PROD

if not PROD:
    app.config['CORS_HEADERS'] = 'Content-Type'
    CORS(app, supports_credentials=True)

db = DB()

@app.route('/airports/', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_airports():
    data = db.read(SELECT_ALL_AIRPORTS)
    airports = [{"value": "ANY", "label": "Any"}]
    for code, name in data:
        if name is None:
            airports.append({"value": code, "label": f"{code}"})
        else:
            airports.append({"value": code, "label": f"{name} ({code})"})
    return jsonify(airports), 200

@app.route('/<origin>/<destination>/', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_flights(origin: str, destination: str):

    if len(origin) != 3 or not origin.isupper():
        return BAD_ORIGIN, 200
    if len(destination) != 3 or not destination.isupper():
        return BAD_DESTINATION, 200

    try:
        data = None
        if origin == "ANY":
            if destination == "ANY":
                return NO_AIRPORT_CHOSEN, 400
            else:
                data = db.read(SELECT_FLIGHTS_TO_DESTINATION, (destination,))
        else:
            if destination == "ANY":
                data = db.read(SELECT_FLIGHTS_FROM_ORIGIN, (origin,))
            else:
                data = db.read(SELECT_FLIGHTS_FROM_ORIGIN_TO_DESTINATION, (origin, destination))
        if data == None:
            raise RuntimeError("Data is null")
        return jsonify(data), 200
    except Exception:
        return DB_QUERY_ERR, 200

app.run(debug=True)

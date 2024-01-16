from flask import Flask, request

from flask_restful import Api, Resource

import requests

app = Flask(__name__)

api = Api(app)

class Sun(Resource):

   def get(self, lat, lng):

       url = f"https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}"

       response = requests.get(url)

       data = response.json()

       return {'data' : data}, 200

api.add_resource(Sun, "/sun/<string:lat>/<string:lng>")


if __name__ == '__main__':

   app.run(host="0.0.0.0", port=6767)

   app.run()
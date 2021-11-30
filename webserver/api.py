from flask_restful import Resource, Api
from flask import Flask, request
from dotenv import load_dotenv
import handler as Handler
from os import getenv


if load_dotenv('config/.env'):
    if (getenv('NHSKEY') is None):
        print("No api key found")
        exit()

# Instantiate the app
app = Flask(__name__)
api = Api(app)


class ByName(Resource):
    def get(self):
        name = request.args.get('name')
        types = request.args.get('type')
        num = request.args.get('num') or 3

        if name is None or types is None:
            return 'name or organisation type is required to search', 404

        resJSON = Handler.dispatchRequest(f'''{{"filter": "{Handler.constructFilterStr(types)}",
                "searchFields": "OrganisationName,OrganisationAliases",
                "search": "{name}",
                "select": "OrganisationName,Address1,Address2,Address3,City,County,Postcode,OpeningTimes",
                "top": {num},
                "skip": 0,
                "count": true}}''').json()

        if 'value' in resJSON:
            # Not sure this is the right http error code
            return resJSON['value'] if len(resJSON['value']) is not 0 else 204


# Create routes
api.add_resource(ByName, '/name')


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

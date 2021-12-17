from flask_restful import Resource, Api
from flask import Flask, request
import handler as Handler


# Instantiate the app
app = Flask(__name__)
api = Api(app)


class ByName(Resource):
    def get(self):
        name = request.args.get('q')
        types = request.args.get('type')
        num = request.args.get('num') or 3

        if name is None or name is "" or types is None or types is "":
            return 'name or organisation type is required to search', 404

        resJSON = Handler.dispatchRequest(f'''{{"filter": "{Handler.constructFilterStr(types)}",
                "searchFields": "OrganisationName,OrganisationAliases",
                "search": "{name}",
                "select": "OrganisationID,OrganisationName,Address1,Address2,Address3,City,County,Postcode,OpeningTimes",
                "top": {num},
                "skip": 0,
                "count": true}}''').json()

        if 'value' in resJSON:
            # Not sure this is the right http error code
            return resJSON['value'] if len(resJSON['value']) is not 0 else 204
        else:
            return 501  # IMPLEMENT HANDLE IF RESPONSE INCORRECT


class ByPostcode(Resource):
    def get(self):
        pc = request.args.get('q')
        types = request.args.get('type')
        num = request.args.get('num') or 3

        if pc is None or pc is "" or types is None or types is "":
            return 'postcode or organisation type is required to search', 404

        resJSON = Handler.dispatchRequest(f'''{{"filter": "{Handler.constructFilterStr(types)}",
                "top": {num}}}''',
                                          "https://api.nhs.uk/service-search/search-postcode-or-place?api-version=1&search=" +
                                          pc.replace(" ", "")).json()

        if 'value' in resJSON:
            return resJSON['value'] if len(resJSON['value']) is not 0 else 204
        else:
            return 501


# Create routes
api.add_resource(ByName, '/n')
api.add_resource(ByPostcode, '/pc')


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

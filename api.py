#!/usr/bin/env python
from flask import Flask
from flask_restful import Resource, Api, abort
import web_parser

app = Flask(__name__)
api = Api(app)


class License(Resource):
    def get(self, license_id=None):
        if license_id is None:
            licenses = web_parser.get_licenses()
            return dict(licenses=licenses)
        try:
            return web_parser.get_license(license_id, False)
        except ValueError:
            abort(404, message="License {} doesn't exist".format(license_id))

class Rules(Resource):
    def get(self):
        rules = web_parser.get_rules()
        return dict(rules=rules)


api.add_resource(License, '/', '/licenses', '/licenses/', '/licenses/<string:license_id>')
api.add_resource(Rules, '/rules')


if __name__ == '__main__':
    app.run(port=8080)

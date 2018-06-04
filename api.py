#!/usr/bin/env python
from flask import Flask
from flask_restful import Resource, Api, abort
import web_parser
import os

import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
api = Api(app)

app.url_map.strict_slashes = False


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


api.add_resource(License, '/', '/licenses', '/licenses/<string:license_id>')
api.add_resource(Rules, '/rules')


@app.route('/status')
def status():
    return 'OK'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ['PORT']))

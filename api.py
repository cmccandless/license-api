#!/usr/bin/env python
from flask import Flask
from flask_restful import Resource, Api, abort
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import web_parser
import os

import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"],
)
api = Api(app)

app.url_map.strict_slashes = False

disabled = (
    "License API disabled due to excessive requests. "
    "If you see this message, please comment on the issue at "
    "https://github.com/cmccandless/license-api/issues/2"
)

class License(Resource):
    def get(self, license_id=None):
        # if license_id is None:
        #     licenses = web_parser.get_licenses()
        #     return dict(licenses=licenses)
        # try:
        #     return web_parser.get_license(license_id, False)
        # except ValueError:
        #     abort(404, message="License {} doesn't exist".format(license_id))
        return abort(503, message=disabled)

class Rules(Resource):
    def get(self):
        # rules = web_parser.get_rules()
        # return dict(rules=rules)
        return abort(503, message=disabled)


api.add_resource(License, '/', '/licenses', '/licenses/<string:license_id>')
api.add_resource(Rules, '/rules')


@app.route('/status')
@limiter.exempt
def status():
    # return 'OK'
    abort(503, message=disabled)


@app.route('/version')
def version():
    with open('VERSION.txt') as f:
        return f.read()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ['PORT']))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
#import numpy as np
import vmodel
import pandas as pd
import json

app = Flask(__name__)
api = Api(app)# create new model object
# data = json.dumps({"contract_address": '0xBBa205283253E7aDB8Be4A0b03600c9AB4924974',
#                         "token_id": '1000'})

parser = reqparse.RequestParser()
parser.add_argument('query')
columns = ['contract_address','token_id']

class Valuation(Resource):
    
    def post(self):
        args = parser.parse_args()
        user_query = args['query']
        # user_query = str(data)
        query_dict = json.loads(user_query) 
        add = query_dict['contract_address']
        ntoken = query_dict['token_id']
        print(ntoken)
        #        results = pm.estimation(df_traits, contract_address, ntoken)
        results = vmodel.ValuationModel.estimation(add, ntoken)
        # results = {'nft_contract': add, 'token_id': ntoken, 
        #             'value': 0.119, 'confidence': 0.03}
        return jsonify(results)
  
api.add_resource(Valuation, '/')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

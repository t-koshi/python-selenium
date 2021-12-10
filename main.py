import datetime
import os
import json

from flask import Flask
from flask import *

from fx_rate.utility import get_fx_rate

app = Flask(__name__)


@app.route('/fx-rate', methods=['GET'])
def get():
    usd_jpy = get_fx_rate()
    res = 'timestamp={}, USDJPY={}'.format(
        datetime.datetime.utcnow() + datetime.timedelta(hours=9), usd_jpy)
    params = {
        'id':coupon_code,
        'title':benefit,
        'value':usd_jpy
    }
    return jsonify(params)

if __name__ == '__main__':
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.run(host=host, port=port, debug=True)

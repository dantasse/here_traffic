#!/usr/bin/env python

# Trying to test out the Here API to see how it works.

# I think config.txt should look like this:
# [here]
# appId=(your app ID here)
# appCode=(your app code here)
# 
# more details: https://docs.python.org/2/library/configparser.html#examples
#
# more about the requests library at: http://docs.python-requests.org/en/latest/
# 1. install pip (if you don't have it) from here: http://pip.readthedocs.org/en/latest/installing.html
# 2. install requests with "pip install requests"
import requests, ConfigParser, pprint

config = ConfigParser.ConfigParser()
config.read('config.txt')
appId = config.get('here', 'appId')
appCode = config.get('here', 'appCode')

# >>> payload = {'key1': 'value1', 'key2': 'value2'}
# >>> r = requests.get("http://httpbin.org/get", params=payload)
url_params = {'app_id': appId, 'app_code': appCode, 'bbox': '39.8485715,-86.0969867;39.8358934,-86.0757964'}
url = 'http://traffic.cit.api.here.com/traffic/6.1/flow.json'
resp = requests.get(url, params=url_params)

resp_json = resp.json()

pprint.pprint(resp_json)
# print resp_json['CREATED_TIMESTAMP']

# what does it all mean:
# http://traffic.cit.api.here.com/traffic/6.0/xsd/flow.xsd?app_id=DemoAppId01082013GAL%20&app_code=AJKnXv84fjrb0KIHawS0Tg

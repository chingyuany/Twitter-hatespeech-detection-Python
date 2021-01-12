import json
import requests
from hatebase import HatebaseAPI


key = "TuwmngrrxcytZkgqyfvtpdUb4yjsKsru"

hatebase = HatebaseAPI({"key": key})
filters = {'is_about_nationality': "false", 'is_about_ethnicity':"false",'is_about_religion':"false",'is_about_gender':"false",'is_about_sexual_orientation':"false",'is_about_disability':"false",'is_about_class':"true", 'language': 'ENG', 'country': 'US', 'year': "2015"}
format = "json"
json_response = hatebase.getSightings(filters=filters, format=format)

with open('classOnly2015.txt', 'w+') as outfile:
   	outfile.write(json.dumps(json_response, indent=4))

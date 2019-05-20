from getgauge.python import step, Messages
import requests
import json
from lib.helpers.json_helper import JSON_helper
from step_impl import *
from lib.api_helpers.people_count_api_helper  import People_count_api_helper




@step("Verify people count for country <country_name> is <people_count>")
def verify_people_count_for_is(country_name, people_count):
     res=call_api("GET","/api/peoplecount/{country_name}".format(country_name=country_name))
     assert res.status_code == requests.codes.ok
     actual_people_count=People_count_api_helper.get_people_count(res.json(),"res['details']['orgLevelHeadCount']['JobCategories']")
     assert int(people_count)==actual_people_count
from getgauge.python import step, Messages
import requests
import json
from lib.helpers.json_helper import JSON_helper
from step_impl import *


@step("Verify Head Count Trend")
def verify_head_count_trend():
     res=call_api("GET","/api/getHeadCountTrend")
     assert res.status_code == requests.codes.ok
     res=JSON_helper.remove_json_timestamp(res.json())
     assert  json.dumps(res) in JSON_helper.read_json_from_file("head_count_trend.json") 
     


@step("Verify Attrition Trend")
def verify_attrition_trend():
     res=call_api("GET","/api/getAttritionTrend")
     assert res.status_code == requests.codes.ok
     res=JSON_helper.remove_json_timestamp(res.json())
     assert  json.dumps(res) in JSON_helper.read_json_from_file("attrition_trend.json") 
    

@step("Verify Revenue Data")
def verify_revenue_data():
     res=call_api("GET","/api/getRevenue")
     assert res.status_code == requests.codes.ok
     res=JSON_helper.remove_json_timestamp(res.json())
     assert  json.dumps(res) in JSON_helper.read_json_from_file("revenue_data.json") 
     


@step("Verify Revenue Trend")
def verify_revenue_trend():
     res=call_api("GET","/api/getRevenueTrend")
     assert res.status_code == requests.codes.ok
     res=JSON_helper.remove_json_timestamp(res.json())
     assert  json.dumps(res) in JSON_helper.read_json_from_file("revenue_trend.json") 
    

@step("Verify AR aging Data")
def verify_ar_aging_data():
     res=call_api("GET","/api/getARReport")
     assert res.status_code == requests.codes.ok
     res=JSON_helper.remove_json_timestamp(res.json())
     assert  json.dumps(res) in JSON_helper.read_json_from_file("ar_aging_data.json") 

@step("Verify mobile Dashboard Data")
def verify_mobile_dashboard_data():
     res=call_api("GET","/api/mobile/dashboard")
     assert res.status_code == requests.codes.ok
     res=JSON_helper.remove_json_timestamp(res.json())
     assert  json.dumps(res) in JSON_helper.read_json_from_file("mobile_dashboard_data.json") 
     
@step("Verify Attrition details")
def verify_attrition_details():
     res=call_api("GET","/api/attrition")
     assert res.status_code == requests.codes.ok
     res=JSON_helper.remove_json_timestamp(res.json())
     assert  json.dumps(res) in JSON_helper.read_json_from_file("attrition_details.json") 

@step("Verify Attrition on Account level for <account>")
def verify_attrition_on_account_level(account):
     res=call_api("GET","/api/attrition/account/{account}".format(account=account))
     assert res.status_code == requests.codes.ok
     attrition_exits_for_account=JSON_helper.get_value_from_api_response_for_key(res.json(),"res['attrition'][0]['exits']")
     expected_attrition_exits=JSON_helper.get_key_value_from_json_file("attrition_details.json","['attrition'][0]['accounts']","name","exits",account) 
     assert  attrition_exits_for_account==expected_attrition_exits



@step("Verify Attrition on DD level for <dd>")
def verify_attrition_on_dd_level(dd):
     res=call_api("GET","/api/attrition/dd/{dd}".format(dd=dd))
     assert res.status_code == requests.codes.ok
     attrition_exits_for_account=JSON_helper.get_value_from_api_response_for_key(res.json(),"res['attrition'][0]['exits']")
     expected_attrition_exits=JSON_helper.get_key_value_from_json_file("attrition_details.json","['attrition'][0]['dds']","name","exits",dd) 
     assert  attrition_exits_for_account==expected_attrition_exits

@step("Verify current Months invoice details")
def verify_current_months_invoice_details():
     res=call_api("GET","/api/getInvoice/v2")
     assert res.status_code == requests.codes.ok
   

@step("Verify pyramid band on org level")
def verify_pyramid_band_on_org_level():
     res=call_api("GET","/api/pyramid/band/org")
     assert res.status_code == requests.codes.ok
     res=JSON_helper.remove_json_timestamp(res.json())
     assert  json.dumps(res) in JSON_helper.read_json_from_file("attrition_details.json") 


@step("Verify pyramid band on dd level")
def verify_pyramid_band_on_dd_level():
     res=call_api("GET","/api/pyramid/band/dd")
     assert res.status_code == requests.codes.ok
     res=JSON_helper.remove_json_timestamp(res.json())
     assert  json.dumps(res) in JSON_helper.read_json_from_file("attrition_details.json") 

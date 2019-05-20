from getgauge.python import step, Messages
import requests
import json
from lib.helpers.json_helper import JSON_helper
from step_impl import *



@step("Verify Bsm Half Yearly Details")
def verify_BSM_half_yearly_details():
     res=call_api("GET","/api/bsm/getBsmHalfYearlyDetails")
     assert res.status_code == requests.codes.ok
    

@step("Verify Vertical details")
def verify_verical_details():
     res=call_api("GET","/api/bsm/getVerticals")
     assert res.status_code == requests.codes.ok
     

@step("Verify All halfs")
def verify_all_half():
     res=call_api("GET","/api/bsm/getAllHalfs")
     assert res.status_code == requests.codes.ok
    


@step("Verify all BU with client for half as <halfId>")
def verify_all_BU_with_client(halfId):
     res=call_api("GET","/api/bsm/getAllBuWithClient?halfId={halfId}".format(halfId=halfId))
     assert res.status_code == requests.codes.ok
    

@step("Verify BSM details for client <clientId> and halfId as <halfId>")
def verify_BSM_details_by_client_id(clientId,halfId):
     res=call_api("GET","/api/bsm/getBsmByClient?halfId={halfId}&clientId={clientId}".format(halfId=halfId,clientId=clientId))
     assert res.status_code == requests.codes.ok
    

     


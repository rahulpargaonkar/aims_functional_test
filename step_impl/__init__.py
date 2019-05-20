import requests
import json
from step_impl import Aimsconstants
import ipdb


headers = {
    "Cookie": "_GA_user_bearer=E79DB638A3DBB1D15A3138EC57BF1C57C671C57D4181D82CB7F324BA1E74FDDDFC458B025DD67506989618587EC1F713FE5673AFE9FD7339EC7F88255DB15C19CE0886EB4496B5CCD585DCE6E5C9657CEDA07366"
    }

def call_api(method,url,data=""):
    print(url)
    if data=="":
     response = requests.request(method,Aimsconstants.AIMS_HOST_URL+url, headers=headers)   
     return response
    else:   
     response = requests.request(method,Aimsconstants.AIMS_HOST_URL+url, headers=headers)   
     return response
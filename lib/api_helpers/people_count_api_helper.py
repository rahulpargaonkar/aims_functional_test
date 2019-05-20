import os,json,ipdb
from lib.helpers.json_helper import JSON_helper
class People_count_api_helper:
 
 @staticmethod
 def get_people_count(res,key):
     res_dict = JSON_helper.get_dictionary(res,key)
     people_count= sum(list(res_dict.values()))
     print(int(people_count))
     return int(people_count)
     
import os,json,ipdb
class JSON_helper:
 
 @staticmethod
 def read_json_from_file(filename):
    path =os.path.abspath("resources/"+filename)   
    with open(path, 'r') as myfile:
      json_data = json.load(myfile)
      #print(json.dumps(json_data))
      return json.dumps(json_data)

 @staticmethod
 def remove_json_timestamp(json_obj):
     if 'jsonUpdatedTimestamp' in json_obj: 
      del json_obj['jsonUpdatedTimestamp']
     return  json_obj

 @staticmethod
 def get_value_from_api_response_for_key(res,key):
    print(type(eval(key)))
    return eval(key)

 @staticmethod
 def get_key_value_from_json_file(filename,key,attribute,match_key,account):
  path =os.path.abspath("resources/"+filename)   
  with open(path, 'r') as myfile:
    json_data= json.loads(json.dumps(json.load(myfile)))
    #print(json_data['attrition'][0]['accounts'])
    json1=eval("json_data"+key)
    for items in json1:
      if items[attribute]==account:   
        return items[match_key]


 @staticmethod
 def get_dictionary(res,key1):
    return eval(key1)

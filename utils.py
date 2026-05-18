import requests


def requeteJson(api):
    rq = requests.get(api)
    return rq.json() if rq.status_code == 200 else {}

def filterUser_list(user_list, filter_element="e"):
    return [ user for user in user_list if user.get("company") and filter_element.lower() in user.get("company").get("name").lower() ]
    
def transformData(user_data: dict):
    return {"id" : user_data.get("id"),
            "full_name" : user_data.get("name"),
            "email" : user_data.get("email"),
            "city" : user_data.get("address",{}).get("city")
            }

def myFormatData(user_list, notNone=False):
    "notNone pour enlever des utilisateurs avec des champs manquants (None) "
    if notNone:
        return [ transformData(user_data) for user_data in user_list if "None" in transformData(user_data).values() ]
    return [ transformData(user_data) for user_data in user_list ]
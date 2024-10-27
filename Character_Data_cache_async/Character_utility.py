import json

def initialize_json_file(file_path):
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json_file.write('')
        
def headers_data(api_key):
    headers = {
        "x-nxopen-api-key": api_key
    }
    
    return headers

def file_mode(file_path, add_file, mode):
    with open(file_path, mode, encoding='utf-8') as json_file:
        json.dump(list(add_file), json_file, ensure_ascii=False, indent=4)
        json_file.write('\n')
        
def response_ocid(response):
    if response.status_code == 200:
        ocid = response.json()['ocid']
        return ocid
    elif response.status_code == 400:
        print("Bad Request")
        return None
    elif response.status_code == 403:
        print("Forbidden")
        return None
    elif response.status_code == 429:
        print("too many Requests")
        return None
    elif response.status_code == 500:
        print("Internal Server Error")
        return None
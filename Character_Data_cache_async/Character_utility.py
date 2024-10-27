def initialize_json_file(file_path):
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json_file.write('')
        
def headers_data(api_key):
    headers = {
        "x-nxopen-api-key": api_key
    }
    
    return headers
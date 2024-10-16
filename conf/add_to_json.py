import json
from config import unpack_json
import os

class add_to_json:
    
    json_name = 0
    
    def __init__(self, json_name):
        self.json_name = json_name
        if os.getcwd()[-4:len(os.getcwd())] != 'conf':
            os.chdir('./conf')
    
    def check_last_added(self):
        unpack_json(json_name=self.json_name)
        uncpacked_json = unpack_json('binds.json')
        last_added = list(uncpacked_json.keys())[-1]
        return last_added
        
        
if __name__ == '__main__':
    work_with_json = add_to_json('binds.json')
    print(work_with_json.check_last_added())
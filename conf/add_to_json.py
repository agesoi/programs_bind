import json
from config import unpack_json, path_input
import os


class add_to_json:
    
    json_name:str = 0
    
    def __init__(self, json_name:str):
        
        self.json_name = json_name
        
        if os.getcwd()[-4:len(os.getcwd())] != 'conf':
            os.chdir('./conf')
    
    def check_last_added(self):
        
        unpack_json(json_name=self.json_name)
        
        uncpacked_json = unpack_json(self.json_name)
        last_added = list(uncpacked_json.keys())[-1]
        last_added = last_added[0:-1]+ str(int(last_added[len(last_added)-1])+1)
        return last_added
 
    def add_app(self, path:str):
        path = path.strip('"')
        # print(path.rfind('/'))
        name_app = path.strip('"')[path.rfind('/')+1:len(path)-4]
        
        done_dict = {self.check_last_added():{'name':str(name_app), 'path':str(path)}}
        lastes:dict = unpack_json(self.json_name)
        lastes.update(done_dict)
        with open(self.json_name, 'w', encoding='utf-8')as file:
        # return done_dict
            json.dump(lastes, file, ensure_ascii=False, indent=4)
        return 0
        # print(path.strip('"'))
        
if __name__ == '__main__':
    work_with_json = add_to_json('binds.json')
    path = path_input()
    # work_with_json.add_app(path)
    
    print(work_with_json.add_app(path))
    # print(work_with_json.check_last_added())
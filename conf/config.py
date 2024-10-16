import json
import os


def path_input():
    path = input("select file path: ")
    slash = '\\'
    path = path.replace(slash,'/' )
    return path



def unpack_json (json_name):
    with open(json_name, 'r') as f:
        data = json.load(f)
        return data


# print(path)

# class edit_config:

#     def __init__():


if __name__ == '__main__':
    # print(path_input())
    # print(os.system('dir'))
    print(os.getcwd())
    if os.getcwd()[-4:len(os.getcwd())] != 'conf':
        os.chdir('./conf')
         
    # print(os.getcwd()[-4:len(os.getcwd())])    
    # print(unpack_json())
    unpacked_json = unpack_json('binds.json')
    # print(unpacked_json)
    for i in uncpacked_json.keys():
        print(i)
import json
import os.path

class JsonUtils:
    def __init__(self):
        pass
    # Check if file exist or not
    def isExist(self, fileName):
        return os.path.isfile(fileName)

    # Create json file
    def create_file():
        data = {}
        data['urls'] = []
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)
        pass

    def add_url(self, url):
        if (self.isExist('data.json')):
            # Edit data file
            with open('data.json', 'r') as file:
                data = json.loads(file)
                data['urls'].append({
                    'url': url
                })

            with open("data.json", "w") as jsonFile:
                json.dump(data, file)
        else:
            create_file()
            # Edit data file
            with open('data.json', 'r+') as file:
                data = json.loads(file)
                data['urls'].append({
                    'url': url
                })

# test = JsonUtils()
# test.init()

# if os.path.isfile('data.json'):
#     print ("File exist")
# else:
#     print ("File not exist")
#     data = {}
#     data['people'] = []
#     data['people'].append({
#         'name': 'Scott',
#         'website': 'stackabuse.com',
#         'from': 'Nebraska'
#     })

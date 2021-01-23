from constant import File
import json

class FileUtils:
    def __init__(self):
        pass

    def create(self):
        data = {}
        data['urls'] = []
        data['urls'].append({
            'url': 'test'
        })
        self.write(data, File.NAME)
        pass

    def write(self, data, file_name):
        with open(file_name, 'w') as file:
            json.dump(data, file)
        pass

    def read(self, file_name):
        with open(file_name, encoding='utf-8') as file:
            arr = json.load(file)
            return arr
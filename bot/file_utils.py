'''
  File Utils, handle file process.
'''
import json
from constant import File

class FileUtils:
    '''
    File Utils handle file processing
    '''

    def __init__(self):
        pass

    def create(self):
        '''TODO Unecessary process'''
        data = {}
        data['urls'] = []
        data['urls'].append({
            'url': 'test'
        })
        self.write(data, File.NAME)

    def write(self, data, file_name):
        '''Write user input to file'''
        with open(file_name, 'w') as file:
            json.dump(data, file)

    def read(self, file_name):
        '''Read json from file'''
        with open(file_name, encoding='utf-8') as file:
            arr = json.load(file)
            return arr

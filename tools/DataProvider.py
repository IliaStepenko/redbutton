import os

import requests


class DataProvider:
    base_url = 'http://127.0.0.1:8000/redbutton/'
    priority_method = 'priority'
    bsystem_method = 'bslist'
    auth_token = ''

    def __init__(self):
        self.auth_token = self.get_auth_token()

    def get_auth_token(self):
        if self.auth_token == '':
            path = os.path.expanduser("~") + '\Documents\Redbutton'
            file = open(path + "\Temp", "r")
            self.auth_token = file.read()
        return self.auth_token




    def get_business_system(self):

        url = self.base_url + self.bsystem_method
        headers = {'Authorization': self.get_auth_token()}

        try:
            response = requests.get(url, headers = headers )
            if response.status_code == 200:
                return [item['name'] for item in response.json()]
        except:
            print("load business system error")


    def get_priority_list(self):

        url = self.base_url + self.priority_method
        headers = {'Authorization': self.auth_token}

        try:
            response = requests.get(url, headers= headers)
            if response.status_code == 200:
                return [item['ru_name'] for item in response.json()]
        except:
            print("load priority error")
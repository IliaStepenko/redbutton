import os

import requests

class UserManager:

    base_url = base_url = 'http://127.0.0.1:8000/account/'
    login_method = 'login/'

    def authenticate(self, username, password):

        try :
            data = {'username':username, 'password':password}
            response = requests.post(self.base_url + self.login_method, data=data)
            path = os.path.expanduser("~") + '\Documents\Redbutton'
            file = open(path + "\Temp", "w")
            file.write('Token '+ response.json()['token'])
            file.close()
            return True
        except:
            print("auth error")
            return False






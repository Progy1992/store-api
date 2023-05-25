import json
import os

class User:
    def __init__(self):
        self.users = self.__load_all_users()

    def __load_all_users(self):
        try:
            with open(os.path.join(os.path.dirname(__file__), '..', 'data/users.json'), 'r') as file:
                user_data = json.load(file)
            return user_data
        except Exception as e:
            raise Exception('Users not fetched')

    def login(self, username, password):
        print('Inside login method')
        print(username, password)
        try:
            for user in self.users:
                print(user['username'], user['password'])
                if user['username'] == username and user['password'] == password:
                    return user
            return None
        except Exception as e:
            raise Exception('Users not fetched')

    def get_user_by_id(self, id):
        try:
            for user in self.users:
                if user['id'] == id:
                    return user
            return None

        except Exception as e:
            raise Exception('User details not fetched')
        
    def get_all_users(self):
        try:
            return self.users
        except Exception as e:
            raise Exception('Users not fetched')
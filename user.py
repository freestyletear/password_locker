import pyperclip
import string
import random


class User:
    '''
    Class to create new user accounts and save the same to help in accesssing the password locker
    '''

    users_list = []

    def __init__(self, first_name, last_name, password):
        '''
        Method to define the properties of the object
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_user(self):
        '''
        save user details method into users_list
        '''
        User.users_list.append(self)

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


class Credential:
    '''
    Class that holds and saves user login details, social media accounts, credentials, passwords
    '''
    # Class Variables
    credentials_list = []

    @classmethod
    def confirm_user(cls, first_name, password):
        '''
		Method that checks if the name and password entered match entries in the users_list
		'''
        active_user = ''
        for user in User.users_list:
            if (user.first_name == first_name and user.password == password):
                active_user = user.first_name
        return active_user

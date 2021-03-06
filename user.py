import pyperclip
import string
import random


class User:
    '''
    Class to create new user accounts and save the same to help in accesssing the password locker
    '''

    users_list = []  # Empty user list

    def __init__(self, first_name, last_name, password):
        '''
        Method to define the properties of the object
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_user(self):
        '''
        save_user method saves user objects(details) into user_list
        '''
        User.users_list.append(self) #The append() method appends an element to the end of the list.

    def delete_user(self): #### Added from here
        '''
        delete_user method deletes a saved user(details) from the user_list
        '''

        User.user_list.remove(self) ##### To here


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

    def __init__(self, user_name, social_media, account_name, password):
        '''
        Method defining the properties each object will hold
        '''

        self.user_name = user_name
        self.social_media = social_media
        self.account_name = account_name
        self.password = password

    def save_credentials(self):
        '''
        Function to save new user credentials
        '''
        Credential.credentials_list.append(self)

    def generate_password():
        '''
        Function to generate random passwords for social media accounts
        '''
        pwchar = string.printable
        length = int(input('Enter password length desired: '))
        generate_password = ''
        for pwchar in range(length):
            generate_password += random.choice(pwchar)
        return generate_password

    @classmethod
    def display_credentials(cls):
        '''
        Class method to display the list of saved credentials
        '''
        return cls.credentials_list

    @classmethod
    def search_social_media(cls, social_media):
        '''
        Method that acccepts social media name and returns credentials matching the social media name
        '''
        for credential in cls.credentials_list:
            if credential.social_media == social_media:
                return credential

    @classmethod 
    def copy_password(cls, social_media):
        '''
		Class method that copies a credential's password of a specific social media site after the credential's social media name is entered
		'''
        collect_password = Credential.search_social_media(social_media)
        return pyperclip.copy(collect_password.password) 

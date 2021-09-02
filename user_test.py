import unittest  # Importing the unittest module
import pyperclip  # helps in copy and paste functions

from user import User, Credential


class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the users class behaviours
    Args:
        unittest.TestCase: Testcase class that helps create test cases
    '''

    def setUp(self):
        '''
        Function to help create user account details before each test
        '''
        self.new_user = User('Keith', 'James', 'freestyletear')

    def test_init_(self):
        '''
        Test to check creation of new user instance
        '''
        self.assertEqual(self.new_user.first_name, 'Keith')
        self.assertEqual(self.new_user.last_name, 'James')
        self.assertEqual(self.new_user.password, 'freestyletear')

    def test_save_user(self):
        '''
        Test to check if New user information is saved into the users_list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list), 1)

    class TestCredentials(unittest.TestCase):
        '''
        Test class that defines test cases for the credentials class behaviours
        Args:
            unittest.TestCase: Testcase class that helps create test cases
        '''

    def test_confirm_user(self):
        '''
        Function to confirm login details to active user
        '''
        self.new_user = User('Keith', 'James', 'freestyletear')
        self.new_user.save_user()
        userX = User('keith', 'James', 'freestyletear')
        userX.save_user()
        active_user = Credential.confirm_user('Keith', 'freestyletear')
        self.assertTrue(active_user)

    def setUp(self):
        '''
        Function to create social media account credentials before each test
        '''
        self.new_credential = Credential(
            'Vanessa', 'facebook', 'James', 'keishamapesa')

    def test__init__(self):
        '''
        Confirm that instance of credentials creation is as expected
        '''
        self.assertEqual(self.new_credential.user_name, 'Vanessa')
        self.assertEqual(self.new_credential.social_media, 'facebook')
        self.assertEqual(self.new_credential.account_name, 'James')
        self.assertEqual(self.new_credential.password, 'keishamapesa')

    def test_save_credentials(self):
        '''
        Test and confirm that the new credential information is being saved
        '''
        self.new_credential.save_credentials()
        self.assertEqual(len(Credential.credentials_list), 1)

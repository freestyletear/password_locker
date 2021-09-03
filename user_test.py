import unittest 
import pyperclip 

from user import User, Credential


class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the users class behaviours
    Args:
        unittest.TestCase: Testcase class that helps create test cases
    '''

    def setUp(self):
        '''
        Function to help create user account details before each test cases.
        '''
        self.new_user = User('Keith', 'James', 'freestyletear') # create contact object

    def test_init_(self):
        '''
        test_init test case to test if the object is initialized properly  for the creation of new user instance.
        '''
        self.assertEqual(self.new_user.first_name, 'Keith')
        self.assertEqual(self.new_user.last_name, 'James')
        self.assertEqual(self.new_user.password, 'freestyletear')

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object(new user information) is saved into the user list.

        '''
        self.new_user.save_user()  # saving the new user
        self.assertEqual(len(User.users_list), 1)

    def test_save_multiple_user(self): #### Added from here
        '''
            test_save_multiple_user to check if we can save multiple user objects to our user_list
            '''
        self.new_user.save_user()
        test_user = User("Vanessa", "james", "keishamapesa")  # new contact
        test_user.save_user()
        self.assertEqual(len(User.users_list), 2) ##### To here

    def test_delete_user(self):  # Added from here
        '''
            test_delete_contact to test if we can remove a contact from our contact list
            '''
        self.new_user.save_user()
        test_user = User("Vanessa", "james", "keishamapesa")  # new contact
        test_user.save_user()

        self.new_contact.delete_contact()  # Deleting a contact object
        self.assertEqual(len(User.contact_list), 1)  ####### To here

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

    def tearDown(self):
        '''
        tearDown method that does clean up and executes a set of instructions after each test case has run.
        '''
        User.users_list = []
        Credential.credentials_list = []

    def test_display_credentials(self):
        '''
        Test to confirm user can view the correct credential details
        '''
        self.new_credential.save_credentials()
        facebook = Credential('vanessa', 'facebook', 'James', 'keishamapesa')
        facebook.save_credentials()
        self.assertEqual(Credential.display_credentials(),
                         Credential.credentials_list)

    def test_search_social_media(self):
        '''
        Test to confirm if the method returns the correct social media credential
        '''
        self.new_credential.save_credentials()
        facebook = Credential('Vanessa', 'Facebook', 'James', 'keishamapesa')
        facebook.save_credentials()
        credential_exists = Credential.search_social_media('Facebook')
        self.assertEqual(credential_exists, facebook)

    def test_copy_password(self):  # uses pyperclip
        '''
        Test to check if the copy password method will copy the correct password from social media site specified
        '''
        self.new_credential.save_credentials()
        facebook = Credential('Vanessa', 'facebook', 'James', 'keishamapesa')
        facebook.save_credentials()
        Credential.copy_password('facebook')
        self.assertEqual(self.new_credential.password, pyperclip.paste())


if __name__ == '__main__':
    unittest.main()

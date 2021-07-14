from django.test import TestCase

from django.contrib.auth import get_user_model

class movies_crud_test(TestCase):

    def setUp(self):


        self.user = get_user_model().objects.create_user(
            username = 'suhaib',
            email = 'suhaib33@gmail.com',
            password = 'password'
        )

    def test_create_new_user(self):

        self.assertEquals(self.user.email,'suhaib33@gmail.com')
        self.assertEquals(self.user.username,'suhaib')
        

    def test_duplicate_emails(self):
        try:

            self.user2 = get_user_model().objects.create_user(
                username = 'suhaib',
                email = 'suhaib33@gmail.com',
                password = 'password'
            )
            
        except:
            print('email already in use')

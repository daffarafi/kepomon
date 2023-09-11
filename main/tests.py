from django.test import TestCase, Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_app_name_in_main(self) :
        response = Client().get('/main/')
        self.assertContains(response, "Kepomon")

    def test_name_in_main(self) :
        response = Client().get('/main/')
        self.assertContains(response, "Muhammad Daffa&#x27;I Rafi Prasetyo")

    def test_class_in_main(self) :
        response = Client().get('/main/')
        self.assertContains(response, "PBP A")

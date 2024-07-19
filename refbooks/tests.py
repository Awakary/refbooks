import requests
from django.test import TestCase


class ApiTestCase(TestCase):

    def test_get_refbooks_status_code_equals_200(self):
        response = requests.get("http://localhost:8000/refbooks/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], "application/json")
        response_body = response.json()
        self.assertEqual(type(response_body['refbooks']), list)

    def test_get_refbooks_elements_status_code_equals_200(self):
        response = requests.get("http://localhost:8000/refbooks/2/elements/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], "application/json")
        response_body = response.json()
        self.assertEqual(type(response_body['elements']), list)

    def test_get_refbooks_check_element_status_code_equals_200(self):
        response = requests.get("http://localhost:8000/refbooks/2/check_element/?code=CA01&value=Острый риносинусит")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], "application/json")
        response_body = response.json()
        self.assertEqual(response_body['code'], 'CA01')
        self.assertEqual(response_body['value'], 'Острый риносинусит')

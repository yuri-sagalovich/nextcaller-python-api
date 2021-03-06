from __future__ import unicode_literals
import unittest
try:
    from unittest import mock
except ImportError:
    import mock
try:
    from .base import BaseTestCase, BasePlatformTestCase
except (ValueError, ImportError):
    from pynextcaller.tests.base import BaseTestCase, BasePlatformTestCase


ADDRESS_NAME_JSON_RESULT_EXAMPLE = '''
{
    "records": [
        {
            "id": "97d949a413f4ea8b85e9586e1f2d9a",
            "first_name": "Jerry",
            "last_name": "Seinfeld",
            "name": "Jerry Seinfeld",
            "language": "English",
            "fraud_threat": "low",
            "spoof": "false",
            "phone": [
                {
                    "number": "2125558383",
                    "carrier": "Verizon Wireless",
                    "line_type": "LAN"
                }
            ],
            "address": [
                {
                    "city": "New York",
                    "extended_zip": "",
                    "country": "USA",
                    "line2": "Apt 5a",
                    "line1": "129 West 81st Street",
                    "state": "NY",
                    "zip_code": "10024"
                }
            ],
            "email": "demo@nextcaller.com",
            "social_links": [
                {
                    "followers": 1,
                    "type": "twitter",
                    "url": "https://twitter.com/nextcaller"
                },
                {
                    "type": "facebook",
                    "url": "https://www.facebook.com/nextcaller"
                },
                {
                    "type": "linkedin",
                    "url": "https://www.linkedin.com/company/next-caller"
                }
            ],
            "age": "45-54",
            "gender": "Male",
            "household_income": "50k-75k",
            "marital_status": "Single",
            "presence_of_children": "No",
            "home_owner_status": "Rent",
            "market_value": "350k-500k",
            "length_of_residence": "12 Years",
            "high_net_worth": "No",
            "occupation": "Entertainer",
            "education": "Completed College",
            "department": "not specified"
        }
    ]
}
'''

ADDRESS_NAME_DATA = {
    'first_name': 'Jerry',
    'last_name': 'Seinfeld',
    'address': '129 West 81st Street',
    'city': 'New York',
    'state': 'NY',
    'zip_code': '10024',
}


class AddressTestCase(BaseTestCase):

    def test_by_address(self):
        self.patch_http_request(ADDRESS_NAME_JSON_RESULT_EXAMPLE)
        res = self.client.get_by_name_address(ADDRESS_NAME_DATA)
        self.assertTrue(res['records'])
        self.assertEqual(res['records'][0]['email'], 'demo@nextcaller.com')
        self.assertEqual(res['records'][0]['first_name'], 'Jerry')
        self.assertEqual(res['records'][0]['last_name'], 'Seinfeld')


class PlatformAddressTestCase(BasePlatformTestCase):

    def test_by_address(self):
        self.patch_http_request(ADDRESS_NAME_JSON_RESULT_EXAMPLE)
        res = self.client.get_by_name_address(ADDRESS_NAME_DATA, self.account_id)
        self.assertTrue(res['records'])
        self.assertEqual(res['records'][0]['email'], 'demo@nextcaller.com')
        self.assertEqual(res['records'][0]['first_name'], 'Jerry')
        self.assertEqual(res['records'][0]['last_name'], 'Seinfeld')


if __name__ == '__main__':
    unittest.main()

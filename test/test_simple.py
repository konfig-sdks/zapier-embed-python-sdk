# coding: utf-8

"""
    Zapier Embed API

    The Zapier Embed API.

    The version of the OpenAPI document: 1.0.0
    Contact: contact@zapier.com
    Created by: https://help.zapier.com/hc/en-us
"""

import unittest

import os
from pprint import pprint
from zapier_embed_python_sdk import ZapierEmbed

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        zapierembed = ZapierEmbed(
        
            client_id = 'YOUR_CLIENT_ID',
            client_secret = 'YOUR_CLIENT_SECRET',,
        
            client_id = 'YOUR_CLIENT_ID',
            client_secret = 'YOUR_CLIENT_SECRET',
        )
        self.assertIsNotNone(zapierembed)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()

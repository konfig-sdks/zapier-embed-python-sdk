# coding: utf-8

"""
    Zapier Embed API

    The Zapier Embed API.

    The version of the OpenAPI document: 1.0.0
    Contact: contact@zapier.com
    Created by: https://help.zapier.com/hc/en-us
"""

import unittest
from unittest.mock import patch

import urllib3

import zapier_embed_python_sdk
from zapier_embed_python_sdk.paths.authentications import get
from zapier_embed_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestAuthentications(ApiTestMixin, unittest.TestCase):
    """
    Authentications unit test stubs
        Get Authentications
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()

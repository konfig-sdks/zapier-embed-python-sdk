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
from zapier_embed_python_sdk.paths.apps import get
from zapier_embed_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApps(ApiTestMixin, unittest.TestCase):
    """
    Apps unit test stubs
        Get Apps
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()

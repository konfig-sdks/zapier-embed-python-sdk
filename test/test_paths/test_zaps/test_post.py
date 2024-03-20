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
from zapier_embed_python_sdk.paths.zaps import post
from zapier_embed_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestZaps(ApiTestMixin, unittest.TestCase):
    """
    Zaps unit test stubs
        Create a Zap
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 201




if __name__ == '__main__':
    unittest.main()

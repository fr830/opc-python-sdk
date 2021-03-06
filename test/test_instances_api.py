# coding: utf-8

"""
    Instances

    An Oracle Compute Cloud Service instance is a virtual machine running a specific operating system and with CPU and memory resources that you specify. See <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=STCSG-GUID-F928F362-2DB6-4E45-843F-C269E0740A36\">About Instances</a> in <em>Using Oracle Compute Cloud Service (IaaS)</em>.<p>You can view and delete instances using the HTTP requests listed below.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.instances_api import InstancesApi


class TestInstancesApi(unittest.TestCase):
    """ InstancesApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.instances_api.InstancesApi()

    def tearDown(self):
        pass

    def test_delete_instance(self):
        """
        Test case for delete_instance

        Delete an Instance
        """
        pass

    def test_discover_instance(self):
        """
        Test case for discover_instance

        Retrieve Names of all Instances and Subcontainers in a Container
        """
        pass

    def test_discover_root_instance(self):
        """
        Test case for discover_root_instance

        Retrieve Names of Containers
        """
        pass

    def test_get_instance(self):
        """
        Test case for get_instance

        Retrieve Details of an Instance
        """
        pass

    def test_list_instance(self):
        """
        Test case for list_instance

        Retrieve Details of all Instances in a Container
        """
        pass

    def test_update_instance(self):
        """
        Test case for update_instance

        Update an Instance
        """
        pass


if __name__ == '__main__':
    unittest.main()

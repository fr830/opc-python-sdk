# coding: utf-8

"""
    IPNetworks

     An IP network allows you to define an IP subnet in your account. The size of the IP subnet and the set IP addresses in the subnet are determined by the IP address prefix that you specify while creating the IP network. These IP addresses aren't part of the common pool of Oracle-provided IP addresses used by the shared network. When you add an instance to an IP network, the instance is assigned an IP address in that subnet. You can assign IP addresses to instances either statically or dynamically, depending on your business needs. So you have complete control over the IP addresses assigned to your instances. For more information, see <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=STCSG-GUID-B62FE52B-CD56-43D9-AB42-354D5C8C5AA1\">Managing IP Networks</a> in <em>Using Oracle Compute Cloud Service (IaaS)</em>

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class HourlyInterval(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, hourly_interval=None):
        """
        HourlyInterval - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'hourly_interval': 'int'
        }

        self.attribute_map = {
            'hourly_interval': 'hourlyInterval'
        }

        self._hourly_interval = hourly_interval

    @property
    def hourly_interval(self):
        """
        Gets the hourly_interval of this HourlyInterval.
        Hours to wait before starting the next backup

        :return: The hourly_interval of this HourlyInterval.
        :rtype: int
        """
        return self._hourly_interval

    @hourly_interval.setter
    def hourly_interval(self, hourly_interval):
        """
        Sets the hourly_interval of this HourlyInterval.
        Hours to wait before starting the next backup

        :param hourly_interval: The hourly_interval of this HourlyInterval.
        :type: int
        """

        self._hourly_interval = hourly_interval

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, HourlyInterval):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
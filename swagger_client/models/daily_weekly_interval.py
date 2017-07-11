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


class DailyWeeklyInterval(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, user_time_zone=None, time_of_day=None, days_of_week=None):
        """
        DailyWeeklyInterval - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'user_time_zone': 'str',
            'time_of_day': 'str',
            'days_of_week': 'list[str]'
        }

        self.attribute_map = {
            'user_time_zone': 'userTimeZone',
            'time_of_day': 'timeOfDay',
            'days_of_week': 'daysOfWeek'
        }

        self._user_time_zone = user_time_zone
        self._time_of_day = time_of_day
        self._days_of_week = days_of_week

    @property
    def user_time_zone(self):
        """
        Gets the user_time_zone of this DailyWeeklyInterval.
        Any IANA time zone. e.g: America/Los_Angeles

        :return: The user_time_zone of this DailyWeeklyInterval.
        :rtype: str
        """
        return self._user_time_zone

    @user_time_zone.setter
    def user_time_zone(self, user_time_zone):
        """
        Sets the user_time_zone of this DailyWeeklyInterval.
        Any IANA time zone. e.g: America/Los_Angeles

        :param user_time_zone: The user_time_zone of this DailyWeeklyInterval.
        :type: str
        """

        self._user_time_zone = user_time_zone

    @property
    def time_of_day(self):
        """
        Gets the time_of_day of this DailyWeeklyInterval.
        Time of the day to run a backup

        :return: The time_of_day of this DailyWeeklyInterval.
        :rtype: str
        """
        return self._time_of_day

    @time_of_day.setter
    def time_of_day(self, time_of_day):
        """
        Sets the time_of_day of this DailyWeeklyInterval.
        Time of the day to run a backup

        :param time_of_day: The time_of_day of this DailyWeeklyInterval.
        :type: str
        """
        if time_of_day is not None and not re.search('([01]?[0-9]|2[0-3]):[0-5][0-9]', time_of_day):
            raise ValueError("Invalid value for `time_of_day`, must be a follow pattern or equal to `/([01]?[0-9]|2[0-3]):[0-5][0-9]/`")

        self._time_of_day = time_of_day

    @property
    def days_of_week(self):
        """
        Gets the days_of_week of this DailyWeeklyInterval.
        Days of the week to run a backup

        :return: The days_of_week of this DailyWeeklyInterval.
        :rtype: list[str]
        """
        return self._days_of_week

    @days_of_week.setter
    def days_of_week(self, days_of_week):
        """
        Sets the days_of_week of this DailyWeeklyInterval.
        Days of the week to run a backup

        :param days_of_week: The days_of_week of this DailyWeeklyInterval.
        :type: list[str]
        """
        allowed_values = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
        if not set(days_of_week).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `days_of_week` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(days_of_week)-set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._days_of_week = days_of_week

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
        if not isinstance(other, DailyWeeklyInterval):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

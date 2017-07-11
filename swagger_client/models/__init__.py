# coding: utf-8

"""
    IPNetworks

     An IP network allows you to define an IP subnet in your account. The size of the IP subnet and the set IP addresses in the subnet are determined by the IP address prefix that you specify while creating the IP network. These IP addresses aren't part of the common pool of Oracle-provided IP addresses used by the shared network. When you add an instance to an IP network, the instance is assigned an IP address in that subnet. You can assign IP addresses to instances either statically or dynamically, depending on your business needs. So you have complete control over the IP addresses assigned to your instances. For more information, see <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=STCSG-GUID-B62FE52B-CD56-43D9-AB42-354D5C8C5AA1\">Managing IP Networks</a> in <em>Using Oracle Compute Cloud Service (IaaS)</em>

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from .daily_weekly_interval import DailyWeeklyInterval
from .hourly_interval import HourlyInterval
from .interval import Interval
from .ip_network_list_response import IpNetworkListResponse
from .ip_network_post_request import IpNetworkPostRequest
from .ip_network_put_request import IpNetworkPutRequest
from .ip_network_response import IpNetworkResponse

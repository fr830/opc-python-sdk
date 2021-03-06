# coding: utf-8

"""
    IPAssociations

    An IP association is a link between an IP reservation and the vcable of an instance. A vcable is an attachment point to a specific network interface of an instance. A vcable is created automatically when an instance is created and is deleted when the instance is deleted.<p>You can create, delete, and view IP associations using the HTTP requests listed below.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class IPAssociationPostRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'parentpool': 'str',
        'vcable': 'str'
    }

    attribute_map = {
        'parentpool': 'parentpool',
        'vcable': 'vcable'
    }

    def __init__(self, parentpool=None, vcable=None):
        """
        IPAssociationPostRequest - a model defined in Swagger
        """

        self._parentpool = None
        self._vcable = None

        self.parentpool = parentpool
        self.vcable = vcable

    @property
    def parentpool(self):
        """
        Gets the parentpool of this IPAssociationPostRequest.
        <ul><li>To associate a temporary IP address from the pool, specify ippool:/oracle/public/ippool.</li><li>To associate a persistent IP address, specify ipreservation:ipreservation_name, where ipreservation_name is three-part name of an existing IP reservation in the <code>/Compute-identity_domain/user/object_name</code> format. For more information about how to create an IP reservation, see <a class=\"xref\" href=\"op-ip-reservation--post.html\">Create an IP Reservation</a>.</li><ul>

        :return: The parentpool of this IPAssociationPostRequest.
        :rtype: str
        """
        return self._parentpool

    @parentpool.setter
    def parentpool(self, parentpool):
        """
        Sets the parentpool of this IPAssociationPostRequest.
        <ul><li>To associate a temporary IP address from the pool, specify ippool:/oracle/public/ippool.</li><li>To associate a persistent IP address, specify ipreservation:ipreservation_name, where ipreservation_name is three-part name of an existing IP reservation in the <code>/Compute-identity_domain/user/object_name</code> format. For more information about how to create an IP reservation, see <a class=\"xref\" href=\"op-ip-reservation--post.html\">Create an IP Reservation</a>.</li><ul>

        :param parentpool: The parentpool of this IPAssociationPostRequest.
        :type: str
        """
        if parentpool is None:
            raise ValueError("Invalid value for `parentpool`, must not be `None`")

        self._parentpool = parentpool

    @property
    def vcable(self):
        """
        Gets the vcable of this IPAssociationPostRequest.
        <p>The three-part name of the vcable ID of the instance that you want to associate with an IP address. The three-part name is in the format: <code>/Compute-<em>identity_domain</em>/<em>user</em>/<em>object</em></code>.<p>For more information about the vcable of an instance, see <a class=\"xref\" href=\"op-instance-{name}-get.html\">Retrieve Details of an Instance</a>.

        :return: The vcable of this IPAssociationPostRequest.
        :rtype: str
        """
        return self._vcable

    @vcable.setter
    def vcable(self, vcable):
        """
        Sets the vcable of this IPAssociationPostRequest.
        <p>The three-part name of the vcable ID of the instance that you want to associate with an IP address. The three-part name is in the format: <code>/Compute-<em>identity_domain</em>/<em>user</em>/<em>object</em></code>.<p>For more information about the vcable of an instance, see <a class=\"xref\" href=\"op-instance-{name}-get.html\">Retrieve Details of an Instance</a>.

        :param vcable: The vcable of this IPAssociationPostRequest.
        :type: str
        """
        if vcable is None:
            raise ValueError("Invalid value for `vcable`, must not be `None`")

        self._vcable = vcable

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
        if not isinstance(other, IPAssociationPostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

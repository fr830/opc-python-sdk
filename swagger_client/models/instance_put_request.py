# coding: utf-8

"""
    Instances

    An Oracle Compute Cloud Service instance is a virtual machine running a specific operating system and with CPU and memory resources that you specify. See <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=STCSG-GUID-F928F362-2DB6-4E45-843F-C269E0740A36\">About Instances</a> in <em>Using Oracle Compute Cloud Service (IaaS)</em>.<p>You can view and delete instances using the HTTP requests listed below.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InstancePutRequest(object):
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
        'attributes': 'dict(str, str)',
        'boot_order': 'list[int]',
        'desired_state': 'str',
        'entry': 'int',
        'hostname': 'str',
        'imagelist': 'str',
        'label': 'str',
        'name': 'str',
        'networking': 'dict(str, object)',
        'reverse_dns': 'bool',
        'shape': 'str',
        'sshkeys': 'list[str]',
        'storage_attachments': 'list[str]',
        'tags': 'list[str]'
    }

    attribute_map = {
        'attributes': 'attributes',
        'boot_order': 'boot_order',
        'desired_state': 'desired_state',
        'entry': 'entry',
        'hostname': 'hostname',
        'imagelist': 'imagelist',
        'label': 'label',
        'name': 'name',
        'networking': 'networking',
        'reverse_dns': 'reverse_dns',
        'shape': 'shape',
        'sshkeys': 'sshkeys',
        'storage_attachments': 'storage_attachments',
        'tags': 'tags'
    }

    def __init__(self, attributes=None, boot_order=None, desired_state=None, entry=None, hostname=None, imagelist=None, label=None, name=None, networking=None, reverse_dns=None, shape=None, sshkeys=None, storage_attachments=None, tags=None):
        """
        InstancePutRequest - a model defined in Swagger
        """

        self._attributes = None
        self._boot_order = None
        self._desired_state = None
        self._entry = None
        self._hostname = None
        self._imagelist = None
        self._label = None
        self._name = None
        self._networking = None
        self._reverse_dns = None
        self._shape = None
        self._sshkeys = None
        self._storage_attachments = None
        self._tags = None

        if attributes is not None:
          self.attributes = attributes
        if boot_order is not None:
          self.boot_order = boot_order
        if desired_state is not None:
          self.desired_state = desired_state
        if entry is not None:
          self.entry = entry
        if hostname is not None:
          self.hostname = hostname
        if imagelist is not None:
          self.imagelist = imagelist
        if label is not None:
          self.label = label
        self.name = name
        if networking is not None:
          self.networking = networking
        if reverse_dns is not None:
          self.reverse_dns = reverse_dns
        if shape is not None:
          self.shape = shape
        if sshkeys is not None:
          self.sshkeys = sshkeys
        if storage_attachments is not None:
          self.storage_attachments = storage_attachments
        if tags is not None:
          self.tags = tags

    @property
    def attributes(self):
        """
        Gets the attributes of this InstancePutRequest.
        A dictionary of attributes to be made available to the instance. A value with the key \"userdata\" will be made available in an EC2-compatible manner.

        :return: The attributes of this InstancePutRequest.
        :rtype: dict(str, str)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """
        Sets the attributes of this InstancePutRequest.
        A dictionary of attributes to be made available to the instance. A value with the key \"userdata\" will be made available in an EC2-compatible manner.

        :param attributes: The attributes of this InstancePutRequest.
        :type: dict(str, str)
        """

        self._attributes = attributes

    @property
    def boot_order(self):
        """
        Gets the boot_order of this InstancePutRequest.
        Boot order list.

        :return: The boot_order of this InstancePutRequest.
        :rtype: list[int]
        """
        return self._boot_order

    @boot_order.setter
    def boot_order(self, boot_order):
        """
        Sets the boot_order of this InstancePutRequest.
        Boot order list.

        :param boot_order: The boot_order of this InstancePutRequest.
        :type: list[int]
        """

        self._boot_order = boot_order

    @property
    def desired_state(self):
        """
        Gets the desired_state of this InstancePutRequest.
        Desired state for the instance.<p>* Set the value of the <code>desired_state</code> parameter as <code>shutdown</code> to shut down the instance.<p>* Set the value of the <code>desired_state</code> parameter as <code>running</code> to restart an instance that you had previously shutdown. The instance is restarted without losing any of the instance data or configuration.

        :return: The desired_state of this InstancePutRequest.
        :rtype: str
        """
        return self._desired_state

    @desired_state.setter
    def desired_state(self, desired_state):
        """
        Sets the desired_state of this InstancePutRequest.
        Desired state for the instance.<p>* Set the value of the <code>desired_state</code> parameter as <code>shutdown</code> to shut down the instance.<p>* Set the value of the <code>desired_state</code> parameter as <code>running</code> to restart an instance that you had previously shutdown. The instance is restarted without losing any of the instance data or configuration.

        :param desired_state: The desired_state of this InstancePutRequest.
        :type: str
        """

        self._desired_state = desired_state

    @property
    def entry(self):
        """
        Gets the entry of this InstancePutRequest.
        Optional imagelistentry number (default will be used if not specified).

        :return: The entry of this InstancePutRequest.
        :rtype: int
        """
        return self._entry

    @entry.setter
    def entry(self, entry):
        """
        Sets the entry of this InstancePutRequest.
        Optional imagelistentry number (default will be used if not specified).

        :param entry: The entry of this InstancePutRequest.
        :type: int
        """

        self._entry = entry

    @property
    def hostname(self):
        """
        Gets the hostname of this InstancePutRequest.
        The hostname for this instance.

        :return: The hostname of this InstancePutRequest.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this InstancePutRequest.
        The hostname for this instance.

        :param hostname: The hostname of this InstancePutRequest.
        :type: str
        """

        self._hostname = hostname

    @property
    def imagelist(self):
        """
        Gets the imagelist of this InstancePutRequest.
        Name of imagelist to be launched.

        :return: The imagelist of this InstancePutRequest.
        :rtype: str
        """
        return self._imagelist

    @imagelist.setter
    def imagelist(self, imagelist):
        """
        Sets the imagelist of this InstancePutRequest.
        Name of imagelist to be launched.

        :param imagelist: The imagelist of this InstancePutRequest.
        :type: str
        """

        self._imagelist = imagelist

    @property
    def label(self):
        """
        Gets the label of this InstancePutRequest.
        A label assigned by the user, specifically for defining inter-instance relationships.

        :return: The label of this InstancePutRequest.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this InstancePutRequest.
        A label assigned by the user, specifically for defining inter-instance relationships.

        :param label: The label of this InstancePutRequest.
        :type: str
        """

        self._label = label

    @property
    def name(self):
        """
        Gets the name of this InstancePutRequest.
        Multipart name of the instance that you want to update.

        :return: The name of this InstancePutRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this InstancePutRequest.
        Multipart name of the instance that you want to update.

        :param name: The name of this InstancePutRequest.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def networking(self):
        """
        Gets the networking of this InstancePutRequest.
        Mapping of <device name> to network specifiers for virtual NICs to be attached to this instance.

        :return: The networking of this InstancePutRequest.
        :rtype: dict(str, object)
        """
        return self._networking

    @networking.setter
    def networking(self, networking):
        """
        Sets the networking of this InstancePutRequest.
        Mapping of <device name> to network specifiers for virtual NICs to be attached to this instance.

        :param networking: The networking of this InstancePutRequest.
        :type: dict(str, object)
        """

        self._networking = networking

    @property
    def reverse_dns(self):
        """
        Gets the reverse_dns of this InstancePutRequest.
        Add PTR records for the hostname.

        :return: The reverse_dns of this InstancePutRequest.
        :rtype: bool
        """
        return self._reverse_dns

    @reverse_dns.setter
    def reverse_dns(self, reverse_dns):
        """
        Sets the reverse_dns of this InstancePutRequest.
        Add PTR records for the hostname.

        :param reverse_dns: The reverse_dns of this InstancePutRequest.
        :type: bool
        """

        self._reverse_dns = reverse_dns

    @property
    def shape(self):
        """
        Gets the shape of this InstancePutRequest.
        Type of instance, as defined on site configuration.

        :return: The shape of this InstancePutRequest.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this InstancePutRequest.
        Type of instance, as defined on site configuration.

        :param shape: The shape of this InstancePutRequest.
        :type: str
        """

        self._shape = shape

    @property
    def sshkeys(self):
        """
        Gets the sshkeys of this InstancePutRequest.
        SSH keys that will be exposed to the instance.

        :return: The sshkeys of this InstancePutRequest.
        :rtype: list[str]
        """
        return self._sshkeys

    @sshkeys.setter
    def sshkeys(self, sshkeys):
        """
        Sets the sshkeys of this InstancePutRequest.
        SSH keys that will be exposed to the instance.

        :param sshkeys: The sshkeys of this InstancePutRequest.
        :type: list[str]
        """

        self._sshkeys = sshkeys

    @property
    def storage_attachments(self):
        """
        Gets the storage_attachments of this InstancePutRequest.
        List of dictionaries containing storage attachment Information.

        :return: The storage_attachments of this InstancePutRequest.
        :rtype: list[str]
        """
        return self._storage_attachments

    @storage_attachments.setter
    def storage_attachments(self, storage_attachments):
        """
        Sets the storage_attachments of this InstancePutRequest.
        List of dictionaries containing storage attachment Information.

        :param storage_attachments: The storage_attachments of this InstancePutRequest.
        :type: list[str]
        """

        self._storage_attachments = storage_attachments

    @property
    def tags(self):
        """
        Gets the tags of this InstancePutRequest.
        A list of strings which will tag the instance for the end-user's uses. Can be queried (?).

        :return: The tags of this InstancePutRequest.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this InstancePutRequest.
        A list of strings which will tag the instance for the end-user's uses. Can be queried (?).

        :param tags: The tags of this InstancePutRequest.
        :type: list[str]
        """

        self._tags = tags

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
        if not isinstance(other, InstancePutRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

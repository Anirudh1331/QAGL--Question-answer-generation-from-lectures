# coding: utf-8

"""
    Speech Services API v3.0

    Speech Services API v3.0.  # noqa: E501

    OpenAPI spec version: v3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class ModelManifest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'model': 'EntityReference',
        'model_files': 'list[ModelFile]',
        'properties': 'dict(str, object)'
    }

    attribute_map = {
        'model': 'model',
        'model_files': 'modelFiles',
        'properties': 'properties'
    }

    def __init__(self, model=None, model_files=None, properties=None, _configuration=None):  # noqa: E501
        """ModelManifest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._model = None
        self._model_files = None
        self._properties = None
        self.discriminator = None

        self.model = model
        self.model_files = model_files
        self.properties = properties

    @property
    def model(self):
        """Gets the model of this ModelManifest.  # noqa: E501


        :return: The model of this ModelManifest.  # noqa: E501
        :rtype: EntityReference
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this ModelManifest.


        :param model: The model of this ModelManifest.  # noqa: E501
        :type: EntityReference
        """
        if self._configuration.client_side_validation and model is None:
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501

        self._model = model

    @property
    def model_files(self):
        """Gets the model_files of this ModelManifest.  # noqa: E501

        The model files of this model.  # noqa: E501

        :return: The model_files of this ModelManifest.  # noqa: E501
        :rtype: list[ModelFile]
        """
        return self._model_files

    @model_files.setter
    def model_files(self, model_files):
        """Sets the model_files of this ModelManifest.

        The model files of this model.  # noqa: E501

        :param model_files: The model_files of this ModelManifest.  # noqa: E501
        :type: list[ModelFile]
        """
        if self._configuration.client_side_validation and model_files is None:
            raise ValueError("Invalid value for `model_files`, must not be `None`")  # noqa: E501

        self._model_files = model_files

    @property
    def properties(self):
        """Gets the properties of this ModelManifest.  # noqa: E501

        The configuration for running this model in a container.  # noqa: E501

        :return: The properties of this ModelManifest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ModelManifest.

        The configuration for running this model in a container.  # noqa: E501

        :param properties: The properties of this ModelManifest.  # noqa: E501
        :type: dict(str, object)
        """
        if self._configuration.client_side_validation and properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ModelManifest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ModelManifest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelManifest):
            return True

        return self.to_dict() != other.to_dict()

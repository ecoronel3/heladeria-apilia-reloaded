# coding: utf-8

"""
    Heladería Via Apilia

    API de la Heladería Via Apilia. A través de esta API se pueden consultar los gustos de helado y realizar pedidos.   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: devs@heladeria-apilia.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PedidoIdPotesBody(object):
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
        'peso': 'PesoDePote',
        'gustos': 'list[str]'
    }

    attribute_map = {
        'peso': 'peso',
        'gustos': 'gustos'
    }

    def __init__(self, peso=None, gustos=None):  # noqa: E501
        """PedidoIdPotesBody - a model defined in Swagger"""  # noqa: E501
        self._peso = None
        self._gustos = None
        self.discriminator = None
        self.peso = peso
        self.gustos = gustos

    @property
    def peso(self):
        """Gets the peso of this PedidoIdPotesBody.  # noqa: E501


        :return: The peso of this PedidoIdPotesBody.  # noqa: E501
        :rtype: PesoDePote
        """
        return self._peso

    @peso.setter
    def peso(self, peso):
        """Sets the peso of this PedidoIdPotesBody.


        :param peso: The peso of this PedidoIdPotesBody.  # noqa: E501
        :type: PesoDePote
        """
        if peso is None:
            raise ValueError("Invalid value for `peso`, must not be `None`")  # noqa: E501

        self._peso = peso

    @property
    def gustos(self):
        """Gets the gustos of this PedidoIdPotesBody.  # noqa: E501

        los gustos de helado en este pote  # noqa: E501

        :return: The gustos of this PedidoIdPotesBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._gustos

    @gustos.setter
    def gustos(self, gustos):
        """Sets the gustos of this PedidoIdPotesBody.

        los gustos de helado en este pote  # noqa: E501

        :param gustos: The gustos of this PedidoIdPotesBody.  # noqa: E501
        :type: list[str]
        """
        if gustos is None:
            raise ValueError("Invalid value for `gustos`, must not be `None`")  # noqa: E501

        self._gustos = gustos

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
        if issubclass(PedidoIdPotesBody, dict):
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
        if not isinstance(other, PedidoIdPotesBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
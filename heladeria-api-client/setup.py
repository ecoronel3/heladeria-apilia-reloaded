# coding: utf-8

"""
    Heladería Via Apilia

    API de la Heladería Via Apilia. A través de esta API se pueden consultar los gustos de helado y realizar pedidos.   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: devs@heladeria-apilia.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "swagger-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Heladería Via Apilia",
    author_email="devs@heladeria-apilia.com",
    url="",
    keywords=["Swagger", "Heladería Via Apilia"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    API de la Heladería Via Apilia. A través de esta API se pueden consultar los gustos de helado y realizar pedidos.   # noqa: E501
    """
)
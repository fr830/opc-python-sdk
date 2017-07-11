# swagger_client
 An IP network allows you to define an IP subnet in your account. The size of the IP subnet and the set IP addresses in the subnet are determined by the IP address prefix that you specify while creating the IP network. These IP addresses aren't part of the common pool of Oracle-provided IP addresses used by the shared network. When you add an instance to an IP network, the instance is assigned an IP address in that subnet. You can assign IP addresses to instances either statically or dynamically, depending on your business needs. So you have complete control over the IP addresses assigned to your instances. For more information, see <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=STCSG-GUID-B62FE52B-CD56-43D9-AB42-354D5C8C5AA1\">Managing IP Networks</a> in <em>Using Oracle Compute Cloud Service (IaaS)</em>

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = swagger_client.IPNetworksApi()
body = swagger_client.IpNetworkPostRequest() # IpNetworkPostRequest | 
cookie = 'cookie_example' # str | The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. (optional)

try:
    # Create an IP Network
    api_response = api_instance.add_ip_network(body, cookie=cookie)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPNetworksApi->add_ip_network: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*IPNetworksApi* | [**add_ip_network**](docs/IPNetworksApi.md#add_ip_network) | **POST** /network/v1/ipnetwork/ | Create an IP Network
*IPNetworksApi* | [**delete_ip_network**](docs/IPNetworksApi.md#delete_ip_network) | **DELETE** /network/v1/ipnetwork/{name} | Delete an IP Network
*IPNetworksApi* | [**get_ip_network**](docs/IPNetworksApi.md#get_ip_network) | **GET** /network/v1/ipnetwork/{name} | Retrieve Details of an IP Network
*IPNetworksApi* | [**list_ip_network**](docs/IPNetworksApi.md#list_ip_network) | **GET** /network/v1/ipnetwork/{container}/ | Retrieve Details of all IP Networks in a Container
*IPNetworksApi* | [**update_ip_network**](docs/IPNetworksApi.md#update_ip_network) | **PUT** /network/v1/ipnetwork/{name} | Update an IP Network


## Documentation For Models

 - [DailyWeeklyInterval](docs/DailyWeeklyInterval.md)
 - [HourlyInterval](docs/HourlyInterval.md)
 - [Interval](docs/Interval.md)
 - [IpNetworkListResponse](docs/IpNetworkListResponse.md)
 - [IpNetworkPostRequest](docs/IpNetworkPostRequest.md)
 - [IpNetworkPutRequest](docs/IpNetworkPutRequest.md)
 - [IpNetworkResponse](docs/IpNetworkResponse.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



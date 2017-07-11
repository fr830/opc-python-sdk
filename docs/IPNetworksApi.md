# swagger_client.IPNetworksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_ip_network**](IPNetworksApi.md#add_ip_network) | **POST** /network/v1/ipnetwork/ | Create an IP Network
[**delete_ip_network**](IPNetworksApi.md#delete_ip_network) | **DELETE** /network/v1/ipnetwork/{name} | Delete an IP Network
[**get_ip_network**](IPNetworksApi.md#get_ip_network) | **GET** /network/v1/ipnetwork/{name} | Retrieve Details of an IP Network
[**list_ip_network**](IPNetworksApi.md#list_ip_network) | **GET** /network/v1/ipnetwork/{container}/ | Retrieve Details of all IP Networks in a Container
[**update_ip_network**](IPNetworksApi.md#update_ip_network) | **PUT** /network/v1/ipnetwork/{name} | Update an IP Network


# **add_ip_network**
> IpNetworkResponse add_ip_network(body, cookie=cookie)

Create an IP Network

Creates an IP network. An IP network allows you to define an IP subnet in your account. With an IP network you can isolate instances by creating separate IP networks and adding instances to specific networks. Traffic can flow between instances within the same IP network, but by default each network is isolated from other networks and from the public Internet.<p><b>Required Role: </b> To complete this task, you must have the <code>Compute_Operations</code> role. If this role isn't assigned to you or you're not sure, then ask your system administrator to ensure that the role is assigned to you in Oracle Cloud My Services. See <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=MMOCS-GUID-54C2E747-7D5B-451C-A39C-77936178EBB6\">Modifying User Roles</a> in <em>Managing and Monitoring Oracle Cloud</em>.

### Example 
```python
from __future__ import print_statement
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IpNetworkPostRequest**](IpNetworkPostRequest.md)|  | 
 **cookie** | **str**| The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. | [optional] 

### Return type

[**IpNetworkResponse**](IpNetworkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/oracle-compute-v3+json
 - **Accept**: application/oracle-compute-v3+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ip_network**
> delete_ip_network(name, cookie=cookie)

Delete an IP Network

<b>Required Role: </b> To complete this task, you must have the <code>Compute_Operations</code> role. If this role isn't assigned to you or you're not sure, then ask your system administrator to ensure that the role is assigned to you in Oracle Cloud My Services. See <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=MMOCS-GUID-54C2E747-7D5B-451C-A39C-77936178EBB6\">Modifying User Roles</a> in <em>Managing and Monitoring Oracle Cloud</em>.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IPNetworksApi()
name = 'name_example' # str | The three-part name (<code>/Compute-<em>identity_domain</em>/<em>user</em>/<em>object</em></code>) of the IP network.
cookie = 'cookie_example' # str | The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. (optional)

try: 
    # Delete an IP Network
    api_instance.delete_ip_network(name, cookie=cookie)
except ApiException as e:
    print("Exception when calling IPNetworksApi->delete_ip_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The three-part name (&lt;code&gt;/Compute-&lt;em&gt;identity_domain&lt;/em&gt;/&lt;em&gt;user&lt;/em&gt;/&lt;em&gt;object&lt;/em&gt;&lt;/code&gt;) of the IP network. | 
 **cookie** | **str**| The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/oracle-compute-v3+json
 - **Accept**: application/oracle-compute-v3+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ip_network**
> IpNetworkResponse get_ip_network(name, cookie=cookie)

Retrieve Details of an IP Network

<b>Required Role: </b>To complete this task, you must have the <code>Compute_Monitor</code> or <code>Compute_Operations</code> role. If this role isn't assigned to you or you're not sure, then ask your system administrator to ensure that the role is assigned to you in Oracle Cloud My Services. See <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=MMOCS-GUID-54C2E747-7D5B-451C-A39C-77936178EBB6\">Modifying User Roles</a> in <em>Managing and Monitoring Oracle Cloud</em>.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IPNetworksApi()
name = 'name_example' # str | The three-part name (<code>/Compute-<em>identity_domain</em>/<em>user</em>/<em>object</em></code>) of the IP network.
cookie = 'cookie_example' # str | The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. (optional)

try: 
    # Retrieve Details of an IP Network
    api_response = api_instance.get_ip_network(name, cookie=cookie)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPNetworksApi->get_ip_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The three-part name (&lt;code&gt;/Compute-&lt;em&gt;identity_domain&lt;/em&gt;/&lt;em&gt;user&lt;/em&gt;/&lt;em&gt;object&lt;/em&gt;&lt;/code&gt;) of the IP network. | 
 **cookie** | **str**| The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. | [optional] 

### Return type

[**IpNetworkResponse**](IpNetworkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/oracle-compute-v3+json
 - **Accept**: application/oracle-compute-v3+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ip_network**
> IpNetworkListResponse list_ip_network(container, cookie=cookie)

Retrieve Details of all IP Networks in a Container

Retrieves details of all the IP networks that are available in the specified container.<p><b>Required Role: </b>To complete this task, you must have the <code>Compute_Monitor</code> or <code>Compute_Operations</code> role. If this role isn't assigned to you or you're not sure, then ask your system administrator to ensure that the role is assigned to you in Oracle Cloud My Services. See <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=MMOCS-GUID-54C2E747-7D5B-451C-A39C-77936178EBB6\">Modifying User Roles</a> in <em>Managing and Monitoring Oracle Cloud</em>.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IPNetworksApi()
container = 'container_example' # str | <p><code>/Compute-<em>identity_domain</em>/<em>user</em></code> or <p><code>/Compute-<em>identity_domain</em></code>
cookie = 'cookie_example' # str | The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. (optional)

try: 
    # Retrieve Details of all IP Networks in a Container
    api_response = api_instance.list_ip_network(container, cookie=cookie)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPNetworksApi->list_ip_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container** | **str**| &lt;p&gt;&lt;code&gt;/Compute-&lt;em&gt;identity_domain&lt;/em&gt;/&lt;em&gt;user&lt;/em&gt;&lt;/code&gt; or &lt;p&gt;&lt;code&gt;/Compute-&lt;em&gt;identity_domain&lt;/em&gt;&lt;/code&gt; | 
 **cookie** | **str**| The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. | [optional] 

### Return type

[**IpNetworkListResponse**](IpNetworkListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/oracle-compute-v3+json
 - **Accept**: application/oracle-compute-v3+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ip_network**
> IpNetworkResponse update_ip_network(name, body, cookie=cookie)

Update an IP Network

You can update an IP network and change the specified IP address prefix for the network after you've created the network and attached instances to it. However, when you change an IP address prefix, it could cause the IP addresses currently assigned to existing instances to fall outside the specified IP network. If this happens, all traffic to and from those vNICs will be dropped.<p>If the IP address of an instance is dynamically allocated, stopping the instance orchestration and restarting it will reassign a valid IP address from the IP network to the instance.<p>However, if the IP address of an instance is static - that is, if the IP address is specified in the instance orchestration while creating the instance - then the IP address can't be updated by stopping the instance orchestration and restarting it. You would have to manually update the orchestration to assign a valid IP address to the vNIC attached to that IP network.<p>It is therefore recommended that if you update an IP network, you only expand the network by specifying the same IP address prefix but with a shorter prefix length. For example, you can expand 192.168.1.0/24 to 192.168.1.0/20. Don't, however, change the IP address. This ensures that all IP addresses that have been currently allocated to instances remain valid in the updated IP network.<p><b>Required Role: </b> To complete this task, you must have the <code>Compute_Operations</code> role. If this role isn't assigned to you or you're not sure, then ask your system administrator to ensure that the role is assigned to you in Oracle Cloud My Services. See <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=MMOCS-GUID-54C2E747-7D5B-451C-A39C-77936178EBB6\">Modifying User Roles</a> in <em>Managing and Monitoring Oracle Cloud</em>.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IPNetworksApi()
name = 'name_example' # str | The three-part name (<code>/Compute-<em>identity_domain</em>/<em>user</em>/<em>object</em></code>) of the IP network.
body = swagger_client.IpNetworkPutRequest() # IpNetworkPutRequest | 
cookie = 'cookie_example' # str | The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. (optional)

try: 
    # Update an IP Network
    api_response = api_instance.update_ip_network(name, body, cookie=cookie)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPNetworksApi->update_ip_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The three-part name (&lt;code&gt;/Compute-&lt;em&gt;identity_domain&lt;/em&gt;/&lt;em&gt;user&lt;/em&gt;/&lt;em&gt;object&lt;/em&gt;&lt;/code&gt;) of the IP network. | 
 **body** | [**IpNetworkPutRequest**](IpNetworkPutRequest.md)|  | 
 **cookie** | **str**| The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. | [optional] 

### Return type

[**IpNetworkResponse**](IpNetworkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/oracle-compute-v3+json
 - **Accept**: application/oracle-compute-v3+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


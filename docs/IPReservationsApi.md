# swagger_client.IPReservationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_ip_reservation**](IPReservationsApi.md#add_ip_reservation) | **POST** /ip/reservation/ | Create an IP Reservation
[**delete_ip_reservation**](IPReservationsApi.md#delete_ip_reservation) | **DELETE** /ip/reservation/{name} | Delete an IP Reservation
[**discover_ip_reservation**](IPReservationsApi.md#discover_ip_reservation) | **GET** /ip/reservation/{container} | Retrieve Names of all IP Reservations and Subcontainers in a Container
[**discover_root_ip_reservation**](IPReservationsApi.md#discover_root_ip_reservation) | **GET** /ip/reservation/ | Retrieve Names of Containers
[**get_ip_reservation**](IPReservationsApi.md#get_ip_reservation) | **GET** /ip/reservation/{name} | Retrieve Details of an IP Reservation
[**list_ip_reservation**](IPReservationsApi.md#list_ip_reservation) | **GET** /ip/reservation/{container}/ | Retrieve Details of all IP Reservations in a Container
[**update_ip_reservation**](IPReservationsApi.md#update_ip_reservation) | **PUT** /ip/reservation/{name} | Update an IP Reservation


# **add_ip_reservation**
> IPReservationResponse add_ip_reservation(body, cookie=cookie)

Create an IP Reservation

Creates an IP reservation. After creating an IP reservation, you can associate it with an instance by using the HTTP request, POST /ipassociation/ <a class=\"xref\" href=\"op-ip-association--post.html\">(Create an IP Association)</a>.<p><b>Required Role: </b>To complete this task, you must have the <code>Compute_Operations</code> role. If this role isn't assigned to you or you're not sure, then ask your system administrator to ensure that the role is assigned to you in Oracle Cloud My Services. See <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=MMOCS-GUID-54C2E747-7D5B-451C-A39C-77936178EBB6\">Modifying User Roles</a> in <em>Managing and Monitoring Oracle Cloud</em>.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IPReservationsApi()
body = swagger_client.IPReservationPostRequest() # IPReservationPostRequest | 
cookie = 'cookie_example' # str | The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. (optional)

try: 
    # Create an IP Reservation
    api_response = api_instance.add_ip_reservation(body, cookie=cookie)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPReservationsApi->add_ip_reservation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IPReservationPostRequest**](IPReservationPostRequest.md)|  | 
 **cookie** | **str**| The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. | [optional] 

### Return type

[**IPReservationResponse**](IPReservationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/oracle-compute-v3+json
 - **Accept**: application/oracle-compute-v3+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ip_reservation**
> delete_ip_reservation(name, cookie=cookie)

Delete an IP Reservation

When you no longer need an IP reservation, you can delete it. Ensure that no instance is using the IP reservation that you want to delete.<p><b>Required Role: </b>To complete this task, you must have the <code>Compute_Operations</code> role. If this role isn't assigned to you or you're not sure, then ask your system administrator to ensure that the role is assigned to you in Oracle Cloud My Services. See <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=MMOCS-GUID-54C2E747-7D5B-451C-A39C-77936178EBB6\">Modifying User Roles</a> in <em>Managing and Monitoring Oracle Cloud</em>.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IPReservationsApi()
name = 'name_example' # str | <p>The three-part name of the object (<code>/Compute-<em>identity_domain</em>/<em>user</em>/<em>object</em></code>).
cookie = 'cookie_example' # str | The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. (optional)

try: 
    # Delete an IP Reservation
    api_instance.delete_ip_reservation(name, cookie=cookie)
except ApiException as e:
    print("Exception when calling IPReservationsApi->delete_ip_reservation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| &lt;p&gt;The three-part name of the object (&lt;code&gt;/Compute-&lt;em&gt;identity_domain&lt;/em&gt;/&lt;em&gt;user&lt;/em&gt;/&lt;em&gt;object&lt;/em&gt;&lt;/code&gt;). | 
 **cookie** | **str**| The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/oracle-compute-v3+json
 - **Accept**: application/oracle-compute-v3+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discover_ip_reservation**
> IPReservationDiscoverResponse discover_ip_reservation(container, cookie=cookie)

Retrieve Names of all IP Reservations and Subcontainers in a Container

Retrieves the names of objects and subcontainers that you can access in the specified container.<p><b>Required Role: </b>To complete this task, you must have the <code>Compute_Monitor</code> or <code>Compute_Operations</code> role. If this role isn't assigned to you or you're not sure, then ask your system administrator to ensure that the role is assigned to you in Oracle Cloud My Services. See <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=MMOCS-GUID-54C2E747-7D5B-451C-A39C-77936178EBB6\">Modifying User Roles</a> in <em>Managing and Monitoring Oracle Cloud</em>.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IPReservationsApi()
container = 'container_example' # str | Specify <code>/Compute-<i>identityDomain</i>/<i>user</i>/</code> to retrieve the names of objects that you can access. Specify <code>/Compute-<i>identityDomain</i>/</code> to retrieve the names of containers that contain objects that you can access.
cookie = 'cookie_example' # str | The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. (optional)

try: 
    # Retrieve Names of all IP Reservations and Subcontainers in a Container
    api_response = api_instance.discover_ip_reservation(container, cookie=cookie)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPReservationsApi->discover_ip_reservation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container** | **str**| Specify &lt;code&gt;/Compute-&lt;i&gt;identityDomain&lt;/i&gt;/&lt;i&gt;user&lt;/i&gt;/&lt;/code&gt; to retrieve the names of objects that you can access. Specify &lt;code&gt;/Compute-&lt;i&gt;identityDomain&lt;/i&gt;/&lt;/code&gt; to retrieve the names of containers that contain objects that you can access. | 
 **cookie** | **str**| The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. | [optional] 

### Return type

[**IPReservationDiscoverResponse**](IPReservationDiscoverResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/oracle-compute-v3+json
 - **Accept**: application/oracle-compute-v3+directory+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discover_root_ip_reservation**
> IPReservationDiscoverResponse discover_root_ip_reservation(cookie=cookie)

Retrieve Names of Containers

Retrieves the names of containers that contain objects that you can access. You can use this information to construct the multipart name of an object.<p><b>Required Role: </b>To complete this task, you must have the <code>Compute_Monitor</code> or <code>Compute_Operations</code> role. If this role isn't assigned to you or you're not sure, then ask your system administrator to ensure that the role is assigned to you in Oracle Cloud My Services. See <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=MMOCS-GUID-54C2E747-7D5B-451C-A39C-77936178EBB6\">Modifying User Roles</a> in <em>Managing and Monitoring Oracle Cloud</em>.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IPReservationsApi()
cookie = 'cookie_example' # str | The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. (optional)

try: 
    # Retrieve Names of Containers
    api_response = api_instance.discover_root_ip_reservation(cookie=cookie)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPReservationsApi->discover_root_ip_reservation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cookie** | **str**| The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. | [optional] 

### Return type

[**IPReservationDiscoverResponse**](IPReservationDiscoverResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/oracle-compute-v3+json
 - **Accept**: application/oracle-compute-v3+directory+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ip_reservation**
> IPReservationResponse get_ip_reservation(name, cookie=cookie)

Retrieve Details of an IP Reservation

Retrieves details of an IP reservation. You can use this request to verify whether the POST and PUT HTTP requests were completed successfully.<p><b>Required Role: </b>To complete this task, you must have the <code>Compute_Monitor</code> or <code>Compute_Operations</code> role. If this role isn't assigned to you or you're not sure, then ask your system administrator to ensure that the role is assigned to you in Oracle Cloud My Services. See <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=MMOCS-GUID-54C2E747-7D5B-451C-A39C-77936178EBB6\">Modifying User Roles</a> in <em>Managing and Monitoring Oracle Cloud</em>.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IPReservationsApi()
name = 'name_example' # str | <p>The three-part name of the object (<code>/Compute-<em>identity_domain</em>/<em>user</em>/<em>object</em></code>).
cookie = 'cookie_example' # str | The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. (optional)

try: 
    # Retrieve Details of an IP Reservation
    api_response = api_instance.get_ip_reservation(name, cookie=cookie)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPReservationsApi->get_ip_reservation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| &lt;p&gt;The three-part name of the object (&lt;code&gt;/Compute-&lt;em&gt;identity_domain&lt;/em&gt;/&lt;em&gt;user&lt;/em&gt;/&lt;em&gt;object&lt;/em&gt;&lt;/code&gt;). | 
 **cookie** | **str**| The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. | [optional] 

### Return type

[**IPReservationResponse**](IPReservationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/oracle-compute-v3+json
 - **Accept**: application/oracle-compute-v3+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ip_reservation**
> IPReservationListResponse list_ip_reservation(container, permanent=permanent, used=used, tags=tags, cookie=cookie)

Retrieve Details of all IP Reservations in a Container

Retrieves details of the IP reservations that are available in the specified container and match the specified query criteria. If you don't specify any query criteria, then details of all the IP reservations in the container are displayed. To filter the search results, you can pass one or more of the following query parameters, by appending them to the URI in the following syntax:<p><code>?parameter1=value1&ampparameter2=value2&ampparameterN=valueN</code><p><b>Required Role: </b>To complete this task, you must have the <code>Compute_Monitor</code> or <code>Compute_Operations</code> role. If this role isn't assigned to you or you're not sure, then ask your system administrator to ensure that the role is assigned to you in Oracle Cloud My Services. See <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=MMOCS-GUID-54C2E747-7D5B-451C-A39C-77936178EBB6\">Modifying User Roles</a> in <em>Managing and Monitoring Oracle Cloud</em>.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IPReservationsApi()
container = 'container_example' # str | <p><code>/Compute-<em>identity_domain</em>/<em>user</em></code>
permanent = true # bool | <code>true</code> indicates that the IP reservation has a persistent public IP address. You can associate either a temporary or a persistent public IP address with an instance when you create the instance.<p>Temporary public IP addresses are assigned dynamically from a pool of public IP addresses. When you associate a temporary public IP address with an instance, if the instance is restarted or is deleted and created again later, its public IP address might change. (optional)
used = true # bool | <code>true</code> indicates that the IP reservation is associated with an instance. (optional)
tags = ['tags_example'] # list[str] | A comma-separated list of strings which helps you to identify IP reservations. (optional)
cookie = 'cookie_example' # str | The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. (optional)

try: 
    # Retrieve Details of all IP Reservations in a Container
    api_response = api_instance.list_ip_reservation(container, permanent=permanent, used=used, tags=tags, cookie=cookie)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPReservationsApi->list_ip_reservation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container** | **str**| &lt;p&gt;&lt;code&gt;/Compute-&lt;em&gt;identity_domain&lt;/em&gt;/&lt;em&gt;user&lt;/em&gt;&lt;/code&gt; | 
 **permanent** | **bool**| &lt;code&gt;true&lt;/code&gt; indicates that the IP reservation has a persistent public IP address. You can associate either a temporary or a persistent public IP address with an instance when you create the instance.&lt;p&gt;Temporary public IP addresses are assigned dynamically from a pool of public IP addresses. When you associate a temporary public IP address with an instance, if the instance is restarted or is deleted and created again later, its public IP address might change. | [optional] 
 **used** | **bool**| &lt;code&gt;true&lt;/code&gt; indicates that the IP reservation is associated with an instance. | [optional] 
 **tags** | [**list[str]**](str.md)| A comma-separated list of strings which helps you to identify IP reservations. | [optional] 
 **cookie** | **str**| The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. | [optional] 

### Return type

[**IPReservationListResponse**](IPReservationListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/oracle-compute-v3+json
 - **Accept**: application/oracle-compute-v3+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ip_reservation**
> IPReservationResponse update_ip_reservation(name, body, cookie=cookie)

Update an IP Reservation

Changes the <code>permanent</code> field of an IP reservation from <code>false</code> to <code>true</code> or vice versa.<p>You can use this command when, for example, you want to delete an instance but retain its autoallocated public IP address as a permanent IP reservation for use later with another instance. In such a case, before deleting the instance, change the permanent field of the IP reservation from <code>false</code> to <code>true</code>.<p>Note that if you change the permanent field of an IP reservation to<code>false</code>, and if the reservation is not associated with an instance, then the reservation will be deleted.<p>You can also update the tags that are used to identify the IP reservation.<p><b>Required Role: </b>To complete this task, you must have the <code>Compute_Operations</code> role. If this role isn't assigned to you or you're not sure, then ask your system administrator to ensure that the role is assigned to you in Oracle Cloud My Services. See <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=MMOCS-GUID-54C2E747-7D5B-451C-A39C-77936178EBB6\">Modifying User Roles</a> in <em>Managing and Monitoring Oracle Cloud</em>.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IPReservationsApi()
name = 'name_example' # str | <p>The three-part name of the object (<code>/Compute-<em>identity_domain</em>/<em>user</em>/<em>object</em></code>).
body = swagger_client.IPReservationPutRequest() # IPReservationPutRequest | 
cookie = 'cookie_example' # str | The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. (optional)

try: 
    # Update an IP Reservation
    api_response = api_instance.update_ip_reservation(name, body, cookie=cookie)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPReservationsApi->update_ip_reservation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| &lt;p&gt;The three-part name of the object (&lt;code&gt;/Compute-&lt;em&gt;identity_domain&lt;/em&gt;/&lt;em&gt;user&lt;/em&gt;/&lt;em&gt;object&lt;/em&gt;&lt;/code&gt;). | 
 **body** | [**IPReservationPutRequest**](IPReservationPutRequest.md)|  | 
 **cookie** | **str**| The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. | [optional] 

### Return type

[**IPReservationResponse**](IPReservationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/oracle-compute-v3+json
 - **Accept**: application/oracle-compute-v3+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# swagger_client.IPAssociationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_ip_association**](IPAssociationsApi.md#add_ip_association) | **POST** /ip/association/ | Create an IP Association
[**delete_ip_association**](IPAssociationsApi.md#delete_ip_association) | **DELETE** /ip/association/{name} | Delete an IP Association
[**discover_ip_association**](IPAssociationsApi.md#discover_ip_association) | **GET** /ip/association/{container} | Retrieve Names of all IP Associations and Subcontainers in a Container
[**discover_root_ip_association**](IPAssociationsApi.md#discover_root_ip_association) | **GET** /ip/association/ | Retrieve Names of Containers
[**get_ip_association**](IPAssociationsApi.md#get_ip_association) | **GET** /ip/association/{name} | Retrieve Details of an IP Association
[**list_ip_association**](IPAssociationsApi.md#list_ip_association) | **GET** /ip/association/{container}/ | Retrieve Details of all IP Associations in a Container


# **add_ip_association**
> IPAssociationResponse add_ip_association(body, cookie=cookie)

Create an IP Association

Creates an association between an IP address and the vcable ID of an instance.<p><b>Required Role: </b>To complete this task, you must have the <code>Compute_Operations</code> role. If this role isn't assigned to you or you're not sure, then ask your system administrator to ensure that the role is assigned to you in Oracle Cloud My Services. See <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=MMOCS-GUID-54C2E747-7D5B-451C-A39C-77936178EBB6\">Modifying User Roles</a> in <em>Managing and Monitoring Oracle Cloud</em>.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IPAssociationsApi()
body = swagger_client.IPAssociationPostRequest() # IPAssociationPostRequest | 
cookie = 'cookie_example' # str | The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. (optional)

try: 
    # Create an IP Association
    api_response = api_instance.add_ip_association(body, cookie=cookie)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPAssociationsApi->add_ip_association: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IPAssociationPostRequest**](IPAssociationPostRequest.md)|  | 
 **cookie** | **str**| The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. | [optional] 

### Return type

[**IPAssociationResponse**](IPAssociationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/oracle-compute-v3+json
 - **Accept**: application/oracle-compute-v3+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ip_association**
> delete_ip_association(name, cookie=cookie)

Delete an IP Association

Deletes the specified IP association. Use this HTTP request when you want to change the public IP address of an instance or if you no longer need a public IP address for the instance.<p><b>Required Role: </b>To complete this task, you must have the <code>Compute_Operations</code> role. If this role isn't assigned to you or you're not sure, then ask your system administrator to ensure that the role is assigned to you in Oracle Cloud My Services. See <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=MMOCS-GUID-54C2E747-7D5B-451C-A39C-77936178EBB6\">Modifying User Roles</a> in <em>Managing and Monitoring Oracle Cloud</em>.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IPAssociationsApi()
name = 'name_example' # str | The three-part name of the object (<code>/Compute-<em>identity_domain</em>/<em>user</em>/<em>object</em></code>).
cookie = 'cookie_example' # str | The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. (optional)

try: 
    # Delete an IP Association
    api_instance.delete_ip_association(name, cookie=cookie)
except ApiException as e:
    print("Exception when calling IPAssociationsApi->delete_ip_association: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The three-part name of the object (&lt;code&gt;/Compute-&lt;em&gt;identity_domain&lt;/em&gt;/&lt;em&gt;user&lt;/em&gt;/&lt;em&gt;object&lt;/em&gt;&lt;/code&gt;). | 
 **cookie** | **str**| The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/oracle-compute-v3+json
 - **Accept**: application/oracle-compute-v3+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discover_ip_association**
> IPAssociationDiscoverResponse discover_ip_association(container, cookie=cookie)

Retrieve Names of all IP Associations and Subcontainers in a Container

Retrieves the names of objects and subcontainers that you can access in the specified container.<p><b>Required Role: </b>To complete this task, you must have the <code>Compute_Monitor</code> or <code>Compute_Operations</code> role. If this role isn't assigned to you or you're not sure, then ask your system administrator to ensure that the role is assigned to you in Oracle Cloud My Services. See <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=MMOCS-GUID-54C2E747-7D5B-451C-A39C-77936178EBB6\">Modifying User Roles</a> in <em>Managing and Monitoring Oracle Cloud</em>.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IPAssociationsApi()
container = 'container_example' # str | Specify <code>/Compute-<i>identityDomain</i>/<i>user</i>/</code> to retrieve the names of objects that you can access. Specify <code>/Compute-<i>identityDomain</i>/</code> to retrieve the names of containers that contain objects that you can access.
cookie = 'cookie_example' # str | The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. (optional)

try: 
    # Retrieve Names of all IP Associations and Subcontainers in a Container
    api_response = api_instance.discover_ip_association(container, cookie=cookie)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPAssociationsApi->discover_ip_association: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container** | **str**| Specify &lt;code&gt;/Compute-&lt;i&gt;identityDomain&lt;/i&gt;/&lt;i&gt;user&lt;/i&gt;/&lt;/code&gt; to retrieve the names of objects that you can access. Specify &lt;code&gt;/Compute-&lt;i&gt;identityDomain&lt;/i&gt;/&lt;/code&gt; to retrieve the names of containers that contain objects that you can access. | 
 **cookie** | **str**| The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. | [optional] 

### Return type

[**IPAssociationDiscoverResponse**](IPAssociationDiscoverResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/oracle-compute-v3+json
 - **Accept**: application/oracle-compute-v3+directory+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discover_root_ip_association**
> IPAssociationDiscoverResponse discover_root_ip_association(cookie=cookie)

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
api_instance = swagger_client.IPAssociationsApi()
cookie = 'cookie_example' # str | The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. (optional)

try: 
    # Retrieve Names of Containers
    api_response = api_instance.discover_root_ip_association(cookie=cookie)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPAssociationsApi->discover_root_ip_association: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cookie** | **str**| The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. | [optional] 

### Return type

[**IPAssociationDiscoverResponse**](IPAssociationDiscoverResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/oracle-compute-v3+json
 - **Accept**: application/oracle-compute-v3+directory+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ip_association**
> IPAssociationResponse get_ip_association(name, cookie=cookie)

Retrieve Details of an IP Association

<b>Required Role: </b>To complete this task, you must have the <code>Compute_Monitor</code> or <code>Compute_Operations</code> role. If this role isn't assigned to you or you're not sure, then ask your system administrator to ensure that the role is assigned to you in Oracle Cloud My Services. See <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=MMOCS-GUID-54C2E747-7D5B-451C-A39C-77936178EBB6\">Modifying User Roles</a> in <em>Managing and Monitoring Oracle Cloud</em>.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IPAssociationsApi()
name = 'name_example' # str | The three-part name of the object (<code>/Compute-<em>identity_domain</em>/<em>user</em>/<em>object</em></code>).
cookie = 'cookie_example' # str | The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. (optional)

try: 
    # Retrieve Details of an IP Association
    api_response = api_instance.get_ip_association(name, cookie=cookie)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPAssociationsApi->get_ip_association: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The three-part name of the object (&lt;code&gt;/Compute-&lt;em&gt;identity_domain&lt;/em&gt;/&lt;em&gt;user&lt;/em&gt;/&lt;em&gt;object&lt;/em&gt;&lt;/code&gt;). | 
 **cookie** | **str**| The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. | [optional] 

### Return type

[**IPAssociationResponse**](IPAssociationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/oracle-compute-v3+json
 - **Accept**: application/oracle-compute-v3+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ip_association**
> IPAssociationListResponse list_ip_association(container, parentpool=parentpool, reservation=reservation, vcable=vcable, cookie=cookie)

Retrieve Details of all IP Associations in a Container

Retrieves details of the IP associations that are available in the specified container and match the specified query criteria. If you don't specify any query criteria, then details of all the IP associations in the container are displayed. To filter the search results, you can pass one or more of the following query parameters, by appending them to the URI in the following syntax:<p><code>?parameter1=value1&ampparameter2=value2&ampparameterN=valueN</code><p><b>Required Role: </b>To complete this task, you must have the <code>Compute_Monitor</code> or <code>Compute_Operations</code> role. If this role isn't assigned to you or you're not sure, then ask your system administrator to ensure that the role is assigned to you in Oracle Cloud My Services. See <a target=\"_blank\" href=\"http://www.oracle.com/pls/topic/lookup?ctx=stcomputecs&id=MMOCS-GUID-54C2E747-7D5B-451C-A39C-77936178EBB6\">Modifying User Roles</a> in <em>Managing and Monitoring Oracle Cloud</em>.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IPAssociationsApi()
container = 'container_example' # str | <code>/Compute-<em>identity_domain</em>/<em>user</em></code> or <p><code>/Compute-<em>identity_domain</em></code>
parentpool = 'parentpool_example' # str | Use this option if you want to retrieve details of temporary IP addresses from the pool. Specify <code>ippool:/oracle/public/ippool</code> as the value. (optional)
reservation = 'reservation_example' # str | Use this option if you want to retrieve details of a specific persistent IP address. Specify the name of the reservation in the format, <code>ipreservation:<em>ipreservation_name</em></code>, where <code><em>ipreservation_name</em></code> is three-part name of an existing IP reservation in the <code>/Compute-<em>identity_domain</em>/<em>user</em>/<em>object</em></code> format. (optional)
vcable = 'vcable_example' # str | vcable ID of the instance that you want to associate with the IP reservation.<p>For more information about the vcable of an instance, see <a class=\"xref\" href=\"op-instance-{name}-get.html\">Retrieve Details of an Instance</a>. (optional)
cookie = 'cookie_example' # str | The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. (optional)

try: 
    # Retrieve Details of all IP Associations in a Container
    api_response = api_instance.list_ip_association(container, parentpool=parentpool, reservation=reservation, vcable=vcable, cookie=cookie)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IPAssociationsApi->list_ip_association: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container** | **str**| &lt;code&gt;/Compute-&lt;em&gt;identity_domain&lt;/em&gt;/&lt;em&gt;user&lt;/em&gt;&lt;/code&gt; or &lt;p&gt;&lt;code&gt;/Compute-&lt;em&gt;identity_domain&lt;/em&gt;&lt;/code&gt; | 
 **parentpool** | **str**| Use this option if you want to retrieve details of temporary IP addresses from the pool. Specify &lt;code&gt;ippool:/oracle/public/ippool&lt;/code&gt; as the value. | [optional] 
 **reservation** | **str**| Use this option if you want to retrieve details of a specific persistent IP address. Specify the name of the reservation in the format, &lt;code&gt;ipreservation:&lt;em&gt;ipreservation_name&lt;/em&gt;&lt;/code&gt;, where &lt;code&gt;&lt;em&gt;ipreservation_name&lt;/em&gt;&lt;/code&gt; is three-part name of an existing IP reservation in the &lt;code&gt;/Compute-&lt;em&gt;identity_domain&lt;/em&gt;/&lt;em&gt;user&lt;/em&gt;/&lt;em&gt;object&lt;/em&gt;&lt;/code&gt; format. | [optional] 
 **vcable** | **str**| vcable ID of the instance that you want to associate with the IP reservation.&lt;p&gt;For more information about the vcable of an instance, see &lt;a class&#x3D;\&quot;xref\&quot; href&#x3D;\&quot;op-instance-{name}-get.html\&quot;&gt;Retrieve Details of an Instance&lt;/a&gt;. | [optional] 
 **cookie** | **str**| The Cookie: header must be included with every request to the service. It must be set to the value of the set-cookie header in the response received to the POST /authenticate/ call. | [optional] 

### Return type

[**IPAssociationListResponse**](IPAssociationListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/oracle-compute-v3+json
 - **Accept**: application/oracle-compute-v3+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


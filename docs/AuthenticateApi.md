# swagger_client.AuthenticateApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_authenticate**](AuthenticateApi.md#add_authenticate) | **POST** /authenticate/ | Authenticate User


# **add_authenticate**
> add_authenticate(body)

Authenticate User

<b>Note:</b> This request returns an authentication token in the <code>Set-Cookie</code> response header. The token expires after 30 minutes. A valid (that is, unexpired) authentication token must be included in every request to the service, in the <code>Cookie</code>: request header. The client making the API call must examine the cookie expiry time and discard it if the cookie has expired. Requests sent with expired cookies will result in an <code>Unauthorized</code> error in the response.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticateApi()
body = swagger_client.Authenticate() # Authenticate | 

try: 
    # Authenticate User
    api_instance.add_authenticate(body)
except ApiException as e:
    print("Exception when calling AuthenticateApi->add_authenticate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Authenticate**](Authenticate.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/oracle-compute-v3+json
 - **Accept**: application/oracle-compute-v3+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


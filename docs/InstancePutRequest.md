# InstancePutRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **dict(str, str)** | A dictionary of attributes to be made available to the instance. A value with the key \&quot;userdata\&quot; will be made available in an EC2-compatible manner. | [optional] 
**boot_order** | **list[int]** | Boot order list. | [optional] 
**desired_state** | **str** | Desired state for the instance.&lt;p&gt;* Set the value of the &lt;code&gt;desired_state&lt;/code&gt; parameter as &lt;code&gt;shutdown&lt;/code&gt; to shut down the instance.&lt;p&gt;* Set the value of the &lt;code&gt;desired_state&lt;/code&gt; parameter as &lt;code&gt;running&lt;/code&gt; to restart an instance that you had previously shutdown. The instance is restarted without losing any of the instance data or configuration. | [optional] 
**entry** | **int** | Optional imagelistentry number (default will be used if not specified). | [optional] 
**hostname** | **str** | The hostname for this instance. | [optional] 
**imagelist** | **str** | Name of imagelist to be launched. | [optional] 
**label** | **str** | A label assigned by the user, specifically for defining inter-instance relationships. | [optional] 
**name** | **str** | Multipart name of the instance that you want to update. | 
**networking** | **dict(str, object)** | Mapping of &lt;device name&gt; to network specifiers for virtual NICs to be attached to this instance. | [optional] 
**reverse_dns** | **bool** | Add PTR records for the hostname. | [optional] 
**shape** | **str** | Type of instance, as defined on site configuration. | [optional] 
**sshkeys** | **list[str]** | SSH keys that will be exposed to the instance. | [optional] 
**storage_attachments** | **list[str]** | List of dictionaries containing storage attachment Information. | [optional] 
**tags** | **list[str]** | A list of strings which will tag the instance for the end-user&#39;s uses. Can be queried (?). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



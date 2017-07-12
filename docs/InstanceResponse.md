# InstanceResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Shows the default account for your identity domain. | [optional] 
**attributes** | **dict(str, str)** | A dictionary of attributes to be made available to the instance. A value with the key \&quot;userdata\&quot; will be made available in an EC2-compatible manner. | [optional] 
**availability_domain** | **str** | The availability domain the instance is in | [optional] 
**boot_order** | **list[int]** | Boot order list. | [optional] 
**desired_state** | **str** | Desired state for the instance. The value can be &lt;code&gt;shutdown&lt;/code&gt; or &lt;code&gt;running&lt;/code&gt; to shutdown an instance or to restart a previously shutdown instance respectively. | [optional] 
**disk_attach** | **str** | A label assigned by the user to identify disks. | [optional] 
**domain** | **str** | The default domain to use for the hostname and for DNS lookups. | [optional] 
**entry** | **int** | Optional imagelistentry number (default will be used if not specified). | [optional] 
**error_reason** | **str** | The reason for the instance going to error state, if available. | [optional] 
**fingerprint** | **str** | SSH server fingerprint presented by the instance. | [optional] 
**hostname** | **str** | The hostname for this instance. | [optional] 
**hypervisor** | **dict(str, str)** | A dictionary of hypervisor-specific attributes. | [optional] 
**image_format** | **str** | The format of the image. | [optional] 
**imagelist** | **str** | Name of imagelist to be launched. | [optional] 
**ip** | **str** | IP address of the instance. | [optional] 
**label** | **str** | A label assigned by the user, specifically for defining inter-instance relationships. | [optional] 
**name** | **str** | Multipart name of the instance. | [optional] 
**networking** | **dict(str, object)** | Mapping of &lt;device name&gt; to network specifiers for virtual NICs to be attached to this instance. | [optional] 
**placement_requirements** | **list[str]** | A list of strings specifying arbitrary tags on nodes to be matched on placement. | [optional] 
**platform** | **str** | The OS platform for the instance. | [optional] 
**priority** | **str** | The priority at which this instance will be run. | [optional] 
**quota** | **str** | Not used | [optional] 
**quota_reservation** | **str** | Reference to the QuotaReservation, to be destroyed with the instance. | [optional] 
**relationships** | [**list[dict(str, str)]**](dict.md) | A list of relationship specifications to be satisfied on this instance&#39;s placement | [optional] 
**resolvers** | **list[str]** | Resolvers to use instead of the default resolvers. | [optional] 
**reverse_dns** | **bool** | Add PTR records for the hostname. | [optional] 
**shape** | **str** | Type of instance, as defined on site configuration. | [optional] 
**site** | **str** | Site to run on. | [optional] 
**sshkeys** | **list[str]** | SSH keys that will be exposed to the instance. | [optional] 
**start_time** | **str** | Start time of the instance. | [optional] 
**state** | **str** | State of the instance. | [optional] 
**storage_attachments** | **list[str]** | List of dictionaries containing storage attachment Information. | [optional] 
**tags** | **list[str]** | Comma-separated list of strings used to tag the instance. | [optional] 
**uri** | **str** | Uniform Resource Identifier | [optional] 
**vcable_id** | **str** | vCable for this instance. | [optional] 
**virtio** | **bool** | Specify if the devices created for the instance are virtio devices. If not specified, the default will come from the cluster configration file. | [optional] 
**vnc** | **str** | IP address and port of the VNC console for the instance. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



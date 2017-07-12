from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
from swagger_client.configuration import Configuration
from swagger_client.api_client import ApiClient
import os

if os.environ.get('OPC_ENDPOINT'):
	endpoint = os.environ.get('OPC_ENDPOINT')
else:
	endpoint = 'https://api-z50.compute.us6.oraclecloud.com'

if os.environ.get('OPC_DOMAIN'):
	domain = os.environ.get('OPC_DOMAIN')
else:
	domain = 'citiccloud'

if os.environ.get('OPC_USER'):
	user = os.environ.get('OPC_USER')
else:
	user = 'greg.huang@oracle.com'

if os.environ.get('OPC_PASSWORD'):
	passwrod = os.environ.get('OPC_PASSWORD')
else:
	password = 'Guoguo@1101'

config=Configuration()
if os.environ.get('http_proxy'):
	config.proxy=os.environ.get('http_proxy')

config.host= endpoint
auth = swagger_client.AuthenticateApi(ApiClient(config))
body = swagger_client.Authenticate(user='/Compute-' + domain + '/' + user, password=password)
ret = auth.add_authenticate(body)
cookie = ret[2]['Set-Cookie']

#ip_network = swagger_client.IPNetworksApi(ApiClient(config))
#api_response = ip_network.list_ip_network(container='Compute-citiccloud', cookie=cookie)

ipresev = swagger_client.IPReservationsApi(ApiClient(config))
api_response = ipresev.list_ip_reservation(container='Compute-citiccloud', cookie=cookie)
pprint(api_response)

ipreass = swagger_client.IPAssociationsApi(ApiClient(config))
api_response = ipreass.list_ip_association(container='Compute-citiccloud', cookie=cookie)

pprint(api_response)
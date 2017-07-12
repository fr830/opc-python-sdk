from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
from swagger_client.configuration import Configuration
from swagger_client.api_client import ApiClient
import os
import random
pprint('######### Begin ##########')
def random_digits(length):
    return '{0:06d}'.format(int(random.random() * (10 ** length)))[1:]

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

container = 'Compute-' + domain
schema = '/' + container + '/' + user + '/'

# Setup Auth info

config.host= endpoint
config.safe_chars_for_path_param = b'/'

auth = swagger_client.AuthenticateApi(ApiClient(config))
body = swagger_client.Authenticate(user='/' + container + '/' + user, password=password)
ret = auth.add_authenticate(body)
cookie = ret[2]['Set-Cookie']

# Get a new IP
ipReserv = swagger_client.IPReservationsApi(ApiClient(config))
req = swagger_client.IPReservationPostRequest(name= schema + 'change-me' + '-' + random_digits(10),
											  parentpool='/oracle/public/ippool',
											  permanent=True)
reservIp = ipReserv.add_ip_reservation(body=req, cookie=cookie)

# Delete old Assosiation
vcable = '/Compute-citiccloud/greg.huang@oracle.com/02427c4a-0136-4b79-b1ab-d67000121cab'
ipAssoc = swagger_client.IPAssociationsApi(ApiClient(config))
assocList = ipAssoc.list_ip_association(container='Compute-citiccloud', cookie=cookie)
for ass in assocList.result:
	if ass.vcable == vcable:
		pprint('Delete old IP Association: ' + ass.ip);
		ipAssoc.delete_ip_association(name=ass.name[1:], cookie=cookie)
		pprint('###################')

# Associate new IP to Instance

req = swagger_client.IPAssociationPostRequest(vcable=vcable, parentpool='ipreservation:' + reservIp.name)
assocIp = ipAssoc.add_ip_association(body=req, cookie=cookie)

pprint('Associate new IP. New Association:'+ assocIp.ip)
pprint('###################')

# Delete old Res IP
reservIpList = ipReserv.list_ip_reservation(container=container, cookie=cookie)
for ip in reservIpList.result:
	if (not ip.used) and ('change-me' in ip.name):
		pprint('Delete IP Reservation: ' + ip.ip)
		ipReserv.delete_ip_reservation(name=ip.name[1:], cookie=cookie)


pprint('######### End ##########')
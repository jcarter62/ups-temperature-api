from ups_snmp import UpsSnmp as snmp
import json
from devicelist import DeviceList

devList = DeviceList().devices()

for device in devList:
    dev = snmp(device['ip'])
    data = dev.get_json()
    s = 'name: {}, location: {}, temp: {}'
    s = s.format(data['name'], data['location'], data['temperature'])
    print s

# s = snmp('192.168.5.99').get_json()

# print 's = ' + str(s)

# from snmp_cmds import Session
from easysnmp import Session

# SNMP Community String (Read-Only)
SNMP_COMMUNITY = 'public'
NAME_OID = '1.3.6.1.2.1.1.5.0'
LOCATION_OID = '1.3.6.1.2.1.1.6.0'
TEMPERATURE_OID = '1.3.6.1.4.1.318.1.1.10.2.3.2.1.4.1'


class UpsSnmp:

    def __init__(self, ip):
        self.ip = ip
        self.state = ''
        self.name = ''
        self.location = ''
        self.temperature = 0
        self.result = {
            'name': '',
            'location': '',
            'temperature': 0.0
        }
        self.get_snmp_data()

    def get_snmp_data(self):
        try:
            my_device = Session(ipaddress=self.ip)

            data = my_device.get_some(oids = [NAME_OID, LOCATION_OID, TEMPERATURE_OID])
            self.name = data[0][1]
            self.location = data[1][1]
            self.temperature = float(data[2][1])
            if self.temperature < 50.0:
                # This is in C, need to convert to F
                self.temperature = (float(self.temperature) * (9.0 / 5.0)) + 32.0
        except Exception as e :
            print( str(e) )
            self.name = ''
            self.location = ''
            self.temperature = 0.0


        self.result = {
            'name': self.name,
            'location': self.location,
            'temperature': self.temperature
        }
        return

    def get_json(self):
        return self.result

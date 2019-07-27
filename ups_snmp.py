from pysnmp.entity.rfc3413.oneliner import cmdgen

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
        cmd_gen = cmdgen.CommandGenerator()

        error_indication, error_status, error_index, var_binds = cmd_gen.getCmd(
                cmdgen.CommunityData(SNMP_COMMUNITY, mpModel=0),
                cmdgen.UdpTransportTarget((self.ip, 161)),
                NAME_OID, LOCATION_OID, TEMPERATURE_OID)

        if error_indication or error_status:
            self.state = error_indication
        else:
            self.name = var_binds[0][1]
            self.location = var_binds[1][1]
            self.temperature = float(var_binds[2][1])

            if self.temperature < 50:
                # This is in C, need to convert to F
                self.temperature = (float(self.temperature) * (9.0 / 5.0)) + 32.0

        self.result = {
            'name': self.name,
            'location': self.location,
            'temperature': self.temperature
        }
        return

    def get_json(self):
        return self.result


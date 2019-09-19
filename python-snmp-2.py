#!/usr/bin/python3
from pysnmp.hlapi import *
import datetime

class SNMP_QUERY():
    def __init__(self):
        pass
    
    def __del__(self):
        pass


def snmp_query(host, community, oid):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(community),
               UdpTransportTarget((host, 161)),
               ContextData(),
               ObjectType(ObjectIdentity(oid)),
               lookupMib=False))

    if errorIndication:
        print(errorIndication)
    else:
        if errorStatus:
            print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex)-1] or '?'
                )
            )
        else:
            for name, val in varBinds:
                return(str(val))  
                
def main():
    # Network Device
    host = '10.3.2.121'
    community = 'public'

    # MOXA Access Point name
    overviewModelName = '.1.3.6.1.4.1.8691.15.33.1.1.1.0'
    overviewUpTime = '.1.3.6.1.4.1.8691.15.33.1.1.4.0'

    result = {}
    result['Model Name'] = snmp_query(host, community, overviewModelName)
    result['Up Time'] = snmp_query(host, community, overviewUpTime)
   

    # # Get access point name
    # result['Model Name'] = snmp_query(host, community, overviewModelName)
    # result['Up Time'] = snmp_query(host, community, overviewUpTime)

    print(result)

# Check if the program was called directly - if it was call the main program
if __name__ == '__main__':
    main()
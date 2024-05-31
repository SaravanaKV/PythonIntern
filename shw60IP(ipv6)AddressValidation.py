'''
IPv4 addresses are 32 bits long, expressed in decimal format separated by periods
(e.g., 192.168.0.1).       "octet(2^8)

In IPv4, an octet is a group of 8 bits, and each octet is represented in decimal format ranging from 0 to 255.
So, an IPv4 address consists of four octets separated by periods, with each octet representing a number from 0 to 255.

IPv6 addresses are 128 bits long, expressed in hexadecimal format separated by colons
(e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334).  "hexadecet"(2^16)
    In IPv6, an address is represented by 128 bits, divided into eight groups of 16 bits each.
    Each group is represented in hexadecimal format, allowing for a range of values from 0000 to FFFF.
    In hexadecimal, each digit represents 4 bits, so each group can represent a value from 0 to 65535.
'''
import sys
ipAddress= input('Enter the IP address : ').lower()       #'1223:3423:234f:df9f:1223:3423:23af:df45'
hexadecets=ipAddress.split(':')
if len(hexadecets) != 8:
    print('IP must contain 8 hexadecet')
    return()
validChar=set('0123456789abcdef')
for hexadecet in hexadecets:
    if len(hexadecet) != 4:
        print('Hexadecet must contain 4 element')
        return()
    for hexa in hexadecet:
        if not hexa in validChar:
            print('Hexadecet value must be in hexadicimal(0-9,a-f)')
            return()
print('Valid IP address')


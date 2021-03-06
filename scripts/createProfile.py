#!/usr/bin/env python
# encoding: utf-8
"""
createProfile.py

creates a provider profile for gigaset phones


"""

import sys
import os


FILE = "d_tonline_de.bin"
HEADER = {0: "2402102240",0x40:FILE}
KEY_VALUE = {
"S_SIP_DOMAIN":"tel.t-online.de",
"S_SIP_REALM":"tel.t-online.de",
"S_SIP_SERVER":"tel.t-online.de",
"S_SIP_REGISTRAR":"tel.t-online.de",
"I_SIP_SERVER_PORT":5060,
"I_SIP_REGISTRAR_PORT":5060,
"B_SIP_USE_STUN":True,
"S_STUN_SERVER":"stun.t-online.de",
"S_SIP_PROVIDER_NAME":"T-Online",
"B_SHOW_USERID_DURING_WIZARD":True,
"S_INFO_SERVICE_URL": "http://info.gigaset.net/info/request.do",
"I_WEB_LABELING": 0,
"S_RAP_URL_1":"http://info.gigaset.net/info/menu.jsp",
"B_RAP_ENABLE":True,
"S_AVAILABLE_OTDP": "kttgengshbse",
"B_ENABLE_SHCNET_MESSENGER":True,
"B_SHOW_USER_FIRMWARE_URL":True,
"B_SHOW_INFO_SERVICE_SERVER_ADVICE":True,
"B_SHOW_QUESTION_MARK_IN_WEB":True,
}

KEY_VALUE_ORIG = {
"S_SIP_DOMAIN":"tel.t-online.de",
"S_SIP_REALM":"tel.t-online.de",
"S_SIP_SERVER":"tel.t-online.de",
"S_SIP_REGISTRAR":"tel.t-online.de",
"I_SIP_SERVER_PORT":5060,
"I_SIP_REGISTRAR_PORT":5060,
"B_SIP_USE_STUN":True,
"S_STUN_SERVER":"stun.t-online.de",
"S_SIP_PROVIDER_NAME":"T-Online",
"B_SHOW_USERID_DURING_WIZARD":True,
"S_INFO_SERVICE_URL": "http://timex.fsnphp.t-online.de/feeds/mediaphone/MediaPhone.xml",
"I_WEB_LABELING": 3,
"S_RAP_URL_1":"http://info.gigaset.net/info/menu.jsp",
"B_RAP_ENABLE":False,
"S_AVAILABLE_OTDP": "dt",
"B_ENABLE_SHCNET_MESSENGER":False,
"B_SHOW_USER_FIRMWARE_URL":False,
"B_SHOW_INFO_SERVICE_SERVER_ADVICE":False,
"B_SHOW_QUESTION_MARK_IN_WEB":False,
}



def int_to_chr(val):
    """docstring for int_to_chr"""
    out = ""
    for i in (24, 16, 8, 0):
        t = (val >> i)%256
        out += chr(t)
    return out

def encodeField(value, header_type=-1):
    t = type(value)
    if (t==type(True)):
        #boolean
        h = 3
        value=chr(value)
    elif (t==type(1)):
        h = 4
        value=int_to_chr(value)
    elif (t==type({'a':1}) or t==type((1,2)) or t==type([3,4])):
        a,b = value
        h=1
        value = encodeField(a,2)
        value += encodeField(b)
    elif (t==type("a")):
        h = 5
        value = str(value+'\x00')
    else:
        raise Exception("value not recognized")
    if (header_type!=-1):
        out = chr(header_type)
    else:
        out = chr(h)
    out += chr(len(value))
    out += value
    return out


def main():
    f = open(FILE,"wb") 
    for k,v in HEADER.items():
        f.write(encodeField(v,k))
    for a in KEY_VALUE.items():
        f.write(encodeField(a))
    f.close()


if __name__ == '__main__':
    main()


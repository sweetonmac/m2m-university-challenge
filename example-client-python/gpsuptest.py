##########
# IMPORT #
##########

import json
import Queue
import re
#import serial
import subprocess
import sys
import threading
import time
import traceback
import urllib2
from cookielib import CookieJar


####################
# Global Variables #
####################

teamname = "Team 02"  # Change displayString value to reflect your team name
M2MserverUrl = "http://203.42.134.72/api/position"  # Target M2M server for JSON upload
DELAY = 5


def postJsonM2MServer(targetUrl, latitude, longitude, timedateUTC, imei, imsi, cpuID, displayString):
    """Upload values to targetUrl"""
    print "[ -- ] Posting data to M2M Server"
    cookieJar = CookieJar()
    arbitraryText = "UTC Timestamp is " + str(timedateUTC)
    print "       DisplayString:", str(displayString), " ArbitraryText:", str(arbitraryText)
    print "       Posting GPS coordinates lat:", str(latitude), "and long:", str(longitude)
    print "       imei:", str(imei), " imsi:", str(imsi), " cpuID:", str(cpuID)
    postdata = json.dumps({"latitude": str(latitude), "longitude": str(longitude), "timestampUTC": str(timedateUTC),
                    "imei": str(imei), "imsi": str(imsi), "cpuID": str(cpuID),
                    "displayString": str(displayString), "arbitraryText": str(arbitraryText)})
    o2 = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
    o2.addheaders = [ ('Content-Type', 'application/json')]
    resp2  = o2.open(targetUrl, postdata)
    UploadResult = resp2.getcode()
    if UploadResult == 200:
        print "[ OK ] Upload Sucessful"
    else:
        print "[FAIL] Upload HTTP Error", UploadResult
    return UploadResult


print "program started"
testpostresult = postJsonM2MServer(M2MserverUrl, -25.345, 131.035, '2014-01-01 00:00:00', 'imei', 'imsi', 'cpuID', teamname) # Test Command Only
print testpostresult
time.sleep(DELAY)

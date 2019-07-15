# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import sys
import os
import re
import requests
import test

regex = r"img(?:.+)src(?:\s+)?=(?:\s+)?\"(http[^\"]+)\""

class ExternalImages(test.Test):
        def check(self, source, text):
                for line in text.split("\n"):
                        matches = re.finditer(regex, line, re.MULTILINE)
                        for matchNum, match in enumerate(matches, start=1):
                                print ("Match {matchNum} was found in {source} at {start}-{end}".format(matchNum = matchNum, start = match.start(), end = match.end(), source = source))
                                
                                for groupNum in range(0, len(match.groups())):
                                        if "smallseotools" in match.group(groupNum):
                                                continue
                                        self.ret += 1
                                        groupNum = groupNum + 1
                                        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
                                        
                                        try:
                                                request = requests.get(match.group(groupNum))
                                                if request.status_code == 200:
                                                        print('Web site exists')
                                                elif requests.exceptions.ConnectionError:
                                                        print("DNS lookup error")
                                                else:
                                                        print('Web site does not exist') 
                                        except Exception as e:
                                                print(e)             

check = ExternalImages()
check.ret = 0
check.run()

sys.exit(check.ret)

#!/usr/bin/env python

"""fortune-clf.py - print a random command from commandlinefu.com

Return a "fortune" from the website commandlinefu.com using python and the published API. Users can alias this to `fortune` if desired.
"""

import requests     #http://docs.python-requests.org/en/latest/index.html
import json         #formats strings once returned
#import re          #chop off url tail to make it shorter
                    # removed, I found a better way to make shortend URL
#import colorama    #considered but not used
                    #1. it's not a stock module, and color isn't important 
                    #2. since it serves up bash tips, I don't care if it
                    #   runs in powershell/DOS

# text tricks: http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python/287934#287934
textreset = "\x1B[m"
itextyellow = "\x1B[03;93m"  #yellow/italic
textyellow = "\x1B[02;93m"   #yellow

r = requests.get('http://www.commandlinefu.com/commands/random/json')
rstring = r.text            #data is now a string
rlist = json.loads(rstring) #data is now a list of one item
rdict = rlist[0]            #data is now a dictonary

print itextyellow + "fortune: " + textreset + rdict['summary']
print "Score: " + rdict['votes']
print textyellow + rdict['command'] + textreset
print "http://www.commandlinefu.com/commands/view/"+ rdict['id'] + "/"
print "--"


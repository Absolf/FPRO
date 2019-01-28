# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 20:32:28 2018

@author: laure
"""

import datetime;

now = datetime.datetime.now();

print('Now:',now.strftime('%H:%M'));

after_eight = now.hour + 8;
after_thirty = now.minute + 30;

if(after_eight>24):
    after_eight -= 24
elif(after_thirty > 60):
     after_thirty -= 60
print("Alarm:",str(after_eight)+":"+str(after_thirty));

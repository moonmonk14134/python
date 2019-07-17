import os
from subprocess import *
import shlex
import configparser
import datetime,time
import sys,smtplib


## get percentage
## cs= check_output(["df", "-lhP"])  ## do the same thing like Popen.communicate
cs= Popen(['df', '-lhP'], stdout=PIPE).communicate()[0]
ln=[]
for x in cs.decode('utf-8').split("\n"):
    ln[:] = []
    ln = x.split()
    if (ln[0].find("/dev") == 0):
      usage = ln[4].replace("%",'')
      if int(usage) >= 16:
        print("Critical: "+ ln[-1],ln[4])
        break
      elif int(usage) >= 10:
        print("Warming: "+ ln[-1],ln[4])




#s = smtplib.SMTP(conf.email_host)
#s.sendmail(conf.from_email,conf.rcipients,msg)
#sys.exit(1)

#sys.exit(0)

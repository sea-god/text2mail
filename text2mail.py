import re
import os
import sys


if len(sys.argv) !=3: 
  print "\t Usage: ./text2mail.py <list> domain\n"
  sys.exit(1)
  
try: 
    files = open(sys.argv[1], "r").readlines()
except(IOError): 
    print "[-] Error: Check your list path\n"
    sys.exit(1)

domain = sys.argv[2]

mails=[]
for file in files:
    contant = re.compile('[\w!#$%&\'*+/=?^_`{|}~-]+(?:\.[\w!#$%&\'*+/=?^_`{|}~-]+)*'+'@'+domain)
    mail = contant.findall(file)
    mails.extend(mail)
    mails = list(set(mails))
with open(domain+'.txt', 'wb+') as mail_file:
    for item in mails:
        mail_file.write(item + '\n')

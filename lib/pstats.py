#!/usr/bin/env python 
# vim: set ts=3 sw=3 sts=3 si ai et: 

# Copyright (c) 2013, Andres Aquino <andres.aquino(at)gmail.com>
# This file is licensed under the BSD License version 3 or later. 
# See the LICENSE file.

import sys
import os
from os import *
from time import *
from md5 import md5

# integer to binary
def bin(x):
   if x==0:
      return '0'
   else:
      return (bin(x/2)+str(x%2)).lstrip('0') or '0'

def toUnix(permissions):
   # 101
   perms = bin(int(permissions))
   if len(perms) == 1 and perms == '0':
      return '---'
   out = ''
   if perms[0] == '1':
      out = out + 'r'
   else:
      out = out + '-'

   if perms[1] == '1':
      out = out + 'w'
   else:
      out = out + '-'

   if perms[2] == '1':
      out = out + 'x'
   else:
      out = out + '-'
   return out

if len(sys.argv) <= 1:
   print 'Provide a filename'
   sys.exit(1)

srcfile = {}
srcfile['name'] = os.path.abspath(sys.argv[1])
srcfile['real'] = os.path.realpath(srcfile['name'])
try:
   srcfile['stats'] = os.stat(srcfile['name'])
   srcfile['md5sum'] = md5(file(srcfile['name']).read()).hexdigest()
except IOError:
   print 'Error, failed to get information about %s'%(sys.argv[0])
   exit(1)

#print srcfile['stats']
permissions = oct(srcfile['stats'].st_mode)[-3:]
srcfile['permissions'] = toUnix(permissions[0]) + toUnix(permissions[1]) + toUnix(permissions[2])
srcfile['mtime'] = strftime("%Y%m.%d",localtime(srcfile['stats'].st_mtime))
srcfile['atime'] = strftime("%Y%m.%d",localtime(srcfile['stats'].st_atime))
srcfile['ctime'] = strftime("%Y%m.%d",localtime(srcfile['stats'].st_ctime))

print '\n[ %s ]'%(os.path.basename(srcfile['name']))
print 'Path        : %s'%(srcfile['name'])
print 'Real        : %s'%(srcfile['real'])
print 'Size        : %s'%(srcfile['stats'].st_size)
print 'Permissions : %s'%(srcfile['permissions'])
print 'Date        : %s'%(srcfile['mtime'])
print 'User        : %s'%(srcfile['stats'].st_uid)
print 'Group       : %s'%(srcfile['stats'].st_gid)
print 'Digest      : %s'%(srcfile['md5sum'])
 

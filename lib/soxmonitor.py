#!/usr/bin/env python 
# vim: set ts=3 sw=3 sts=3 si ai et: 

# Copyright (c) 2013, Andres Aquino <andres.aquino(at)gmail.com>
# This file is licensed under the BSD License version 3 or later. 
# See the LICENSE file.

'''SOXMonitor: Sarbanes-Oxley Report

Usage: soxmonitor [options]

   -g, --group             Group of applications
   -c, --component         An individual component, must be exists in a group
   -e, --environment       Environment, some alias was created but is possible to define 
                           new enviroments, some aliases are 
                           (--prod, --dev, --int, --qa and --uat) 
                           or in GNU mode 
                           (-e=production, --environment=useracceptance, -e=integration)
                           Can you guess why..?
   -v, --verbose           Add more information to output, additionally create a new report
                           in vendor directory
   -h, --help
       --version

'''

import os
import sys
import re


from md5 import md5
from getopt import getopt
from ConfigParser import SafeConfigParser


# 
# main class application
class mainApp(object):

   def __init__(self):
      self.data = {}
      self['lib'] = os.environ['SOX_HOME'] + os.sep + 'lib' + os.sep
      self['config'] = os.environ['SOX_HOME'] + os.sep + 'config' + os.sep
      self['main'] = self['lib'] + 'soxmonitor.py'
      self['options'] = []
      self['options'].extend(['group=', 'component=', 'environment=', 'verbose', 'help', 'version'])
      self['options'].extend(['prod', 'dev', 'int', 'qa', 'uat'])

   def __getitem__(self, key): 
      return self.data[key]

   def __setitem__(self, key, item): 
      self.data[key] = item

   def getApplication(self):
      return self['main']
   
   def getOptions(self):
      return self['options']

   def isVerbose(self):
      return self['setup'].getboolean('main','verbose')

   def getConfiguration(self):
      stfile = self['config'] + 'soxmonitor.conf'
      try:
         self['setup'] = SafeConfigParser()
         self['setup'].read(stfile)
      except Exception, message:
         print 'Error:\n%s'%(message)
         exit(1)


#
# load application
app = mainApp()

if __name__ == '__main__':
   try:
      options, reminder = getopt(sys.argv[1:], 'g:c:e:vh', app.getOptions())
   except Exception, message:
      print __doc__
      sys.exit(0)

   app.getConfiguration()
   for option, argument in options: 
      if option in ['g','--group']:
         print 'group %s'%(argument)

      if option in ['-c', '--component']:
         print 'component%s'%(argument)

      if option in ['-e', '--environment']:
         print 'environment%s'%(argument)

      if option in ['-v', '--verbose']:
         # app.setVerbose() 
         print 'verbose'

      if option in ['-h','--help']:
         print __doc__
         sys.exit(0)

      if option in ['--version']:
         # take version from source file, ${SOX_HOME}/lib/soxmonitor.py
         mdfile = '00000000'
         try:
            srfile = file(app.getApplication()).read()
            mdfile = md5(srfile).hexdigest()
         except Exception, message:
            print 'Error:\n%s'%(message)
            exit(1)

         print 'SOXMonitor v.%s\n'%(mdfile[-6:])
         print ' Developed by Andres Aquino <aquino(at)hp.com>'
         print ' Codename: Barricade!'
         sys.exit(0)

   # ready!
   # app.setVerbose()
   # app.getReport('noe', 'production')
   # app.getReport('cci', 'production')
   # app.getReport('all', 'development')
   # app.save()
   # app.show()


# 

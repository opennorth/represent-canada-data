#coding: utf8

from ftplib import FTP
import os.path
from urlparse import urlparse

import boundaries
import requests

# @see Command#handle in boundaries/management/commands/loadshapefiles.py
boundaries.autodiscover('.')
all_sources = boundaries.registry

# Make sure URLs in definition files exist.
for slug, config in all_sources.items():
  # Check URLs.
  for key in ('source_url', 'licence_url', 'data_url'):
    if config.get(key):
      url = config[key]
      result = urlparse(url)
      if result.scheme == 'ftp':
        ftp = FTP(result.hostname)
        ftp.login(result.username, result.password)
        ftp.cwd(os.path.dirname(result.path))
        if os.path.basename(result.path) not in ftp.nlst():
          print "404 %s" % url
        ftp.quit()
      else:
        try:
          arguments = {'allow_redirects': True}
          if result.username:
            url = "%s://%s%s" % (result.scheme, result.hostname, result.path)
            arguments['auth'] = (result.username, result.password)
          response = requests.head(url, **arguments)
          status_code = response.status_code
          if status_code != 200:
            print "%d %s" % (status_code, url)
        except requests.exceptions.ConnectionError:
          print "404 %s" % url

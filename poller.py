#!/usr/bin/env python
import urllib2
import ssl


def poll(sites, timeout):
    for site in sites:
        print 'polling ' + site

        try:
            response = urllib2.urlopen(site, timeout=timeout)
            response.read()
        except urllib2.URLError as e:
            print e.code
        except ssl.SSLError as e:
            print e.message
        else:
            print 'ok'

if __name__ == '__main__':
    poll(sites=(
        'https://redmine.codegrove.org',
        'http://koodilehto.fi',
        'http://vakiopaine.net',
        ), timeout=5)

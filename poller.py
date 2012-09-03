#!/usr/bin/env python
import urllib2
import ssl

# Define the sites we want to poll and the timeout.
SITES = (
    'https://redmine.codegrove.org',
    'http://koodilehto.fi',
    'http://vakiopaine.net',
)
TIMEOUT = 5


def poll(sites, timeout):
    """Checks if the given URLs are online."""
    for site in sites:
        print 'Polling ' + site

        try:
            response = urllib2.urlopen(site, timeout=timeout)
            response.read()
        except urllib2.URLError as e:
            print e.code
        except ssl.SSLError as e:
            print e.message
        else:
            print 'OK'

if __name__ == '__main__':
    poll(SITES, timeout=TIMEOUT)


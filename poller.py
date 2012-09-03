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
    import gntp.notifier as notify
except ImportError:
    notify = None

def poll(sites, timeout, ok, error):
    for site in sites:
        ok('Polling ' + site)

        try:
            response = urllib2.urlopen(site, timeout=timeout)
            response.read()
        except urllib2.URLError as e:
            error(site + ' ' + e.code)
        except ssl.SSLError as e:
            error(site + ' ' + e.message)
        else:
            print 'OK'

def empty(data):
    pass

def output(data):
    if notify:
        notify.mini(data)
    else:
        print data

if __name__ == '__main__':
    poll(SITES, timeout=TIMEOUT, ok=empty, error=output)


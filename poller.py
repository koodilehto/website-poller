#!/usr/bin/env python
import urllib2
import ssl

try:
    import gntp.notifier as notify
except ImportError:
    notify = None

def poll(sites, timeout, ok, error):
    for site in sites:
        ok('polling ' + site)

        try:
            response = urllib2.urlopen(site, timeout=timeout)
            response.read()
        except urllib2.URLError as e:
            error(site + ' ' + e.code)
        except ssl.SSLError as e:
            error(site + ' ' + e.message)
        else:
            ok('ok')


def empty(data):
    pass


def output(data):
    if notify:
        notify.mini(data)
    else:
        print data


if __name__ == '__main__':
    poll(sites=(
        'https://redmine.codegrove.org',
        'http://koodilehto.fi',
        'http://vakiopaine.net',
        ), timeout=5, ok=empty, error=output)

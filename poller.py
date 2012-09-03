#!/usr/bin/env python
import urllib2
import ssl
import functools

# Define the sites we want to poll and the timeout.
SITES = (
    'https://redmine.codegrove.org',
    'http://koodilehto.fi',
    'http://vakiopaine.net',
    'http://thisshouldtimeout.net',
)
TIMEOUT = 5


try:
    import gntp.notifier

    notification = gntp.notifier.mini
except ImportError:
    try:
        import pygtk
        pygtk.require('2.0')
        import pynotify

        notification = functools.partial(
            pynotify.Notification,
            'Koodilehto Service Error'
        )
    except ImportError:
        def out(data):
            print data

        notification = out


def poll(sites, timeout, ok, error):
    """Checks if the given URLs are online."""
    for site in sites:
        ok('Polling ' + site)

        try:
            response = urllib2.urlopen(site, timeout=timeout)
            response.read()
        except urllib2.URLError as e:
            error(site + ' ' + str(e.code))
        except ssl.SSLError as e:
            error(site + ' ' + e.message)
        except Exception as e:
            error(site + ' ' + e.message)
        else:
            ok('OK')


def empty(data):
    pass


if __name__ == '__main__':
    poll(SITES, timeout=TIMEOUT, ok=empty, error=notification)

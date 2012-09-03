#!/usr/bin/env python
import urllib2
import ssl
import functools

# Define the sites we want to poll and the timeout.
SITES = (
    'https://redmine.codegrove.org',
    'http://koodilehto.fi',
    'http://vakiopaine.net',
)
TIMEOUT = 5


try:
    """For Mac OSX use Growl notifier."""
    import gntp.notifier

    notification = gntp.notifier.mini
except ImportError:
    """For Linux try using Pynotigy."""
    try:
        import pygtk
        pygtk.require('2.0')
        import pynotify

        notification = functools.partial(
            pynotify.Notification,
            'Koodilehto Service Error'
        )
    except ImportError:
        """All other systems get a printed line."""
        def out(data):
            print data

        notification = out


def poll(sites, timeout, ok, error):
    """Checks if the given URLs are online.
    sites - List of URLs to check.
    timeout - Timeout in seconds.
    ok - Which site we are checking.
    error - Error reporting function.
    """
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
    """Placeholder for now."""
    pass


if __name__ == '__main__':
    poll(SITES, timeout=TIMEOUT, ok=empty, error=notification)

# website-poller

Polls specified websites and alerts the administration if needed.

## Installation

On a Linux machine change the paths in ./install.sh run it or add the crontab entry yourself: @hourly DISPLAY=:0.0 /path/to/websitepoller > /dev/null

## Growl

Note that you need to install [GNTP](https://github.com/kfdm/gntp/) in your system if you want to use Growl (OS X).

## Python-Notify

On a Linux system you need python-notify.

## .websitepollerrc

You should have a .websitepollerrc file in the user's home directory. Contents are in JSON format, for example: 

[
"http://www.github.org",
"http://www.google.com"
]


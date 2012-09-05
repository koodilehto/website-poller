# website-poller

website-poller polls websites specified at `~/.websitepollerrc` (JSON) and alerts
using system notifications should some website fail to respond properly.

Define your `~/.websitepollerrc` like this:

```json
{
"user-agent":"Koodilehto Website Poller",
"websites":
[
"http://www.github.com",
"http://www.google.com"
]
}
```

## Installation

### Linux

Change the paths at ./install.sh and run it, or add the crontab entry yourself: `@hourly DISPLAY=:0.0 /path/to/websitepoller.py > /dev/null`

Make sure you have `python-notify2` installed in order for the notications to work.

### OS X

Make sure you have [GNTP](https://github.com/kfdm/gntp/) installed. Note that this depends on [Growl](http://growl.info/). Otherwise Linux instructions apply.

### Windows

No official support at the moment. Feel free to contribute.

## License

MIT. See LICENSE for more information.

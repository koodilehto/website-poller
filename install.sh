#!/bin/sh

# Install website-poller to the system.
sudo ./setup.py install

# Add the program to user's cronjobs.
CRON_TIME="@hourly DISPLAY=:0.0"
PROGRAM=$(which websitepoller)
PARAMS=" > /dev/null"
TO_CRON="$CRON_TIME $PROGRAM $PARAMS"

# Add to user's cronjobs.
(crontab -l; echo "$TO_CRON") | crontab -


#!/bin/sh

# Adds the program to user's cronjobs.

CRON_TIME="@hourly DISPLAY=:0.0"
PROGRAM="websitepoller"
PARAMS=" > /dev/null"

./setup.py install

TO_CRON="$CRON_TIME $PROGRAM $PARAMS"

# Add to user's cronjobs.
(crontab -l; echo "$TO_CRON") | crontab -


#!/bin/sh

# Adds the program to user's cronjobs.

CRON_TIME="@hourly DISPLAY=:0.0"
BIN_DIR="/usr/local/bin/"
PROGRAM="websitepoller.py"
PARAMS=" > /dev/null"

# Copy the program.
sudo cp $PROGRAM $BIN_DIR$PROGRAM

TO_CRON="$CRON_TIME $BIN_DIR$PROGRAM $PARAMS"

# Add to user's cronjobs.
(crontab -l; echo "$TO_CRON") | crontab -


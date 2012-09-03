#!/bin/sh

# Adds the program to user's cronjobs.

CRON_TIME="@hourly"
BIN_DIR="/usr/bin/"
PROGRAM="check_websites"
PARAMS=" > /dev/null"

# Copy the program.
sudo cp $PROGRAM $BIN_DIR$PROGRAM

TO_CRON="$CRON_TIME $BIN_DIR$PROGRAM $PARAMS"

# Add to user's cronjobs.
(crontab -l; echo "$TO_CRON") | crontab -


#!/bin/sh

# Adds the program to user's cronjobs.

BIN_DIR="/usr/bin/"
PROGRAM="check_websites"

# Copy the program.
sudo cp $PROGRAM $BIN_DIR$PROGRAM

TO_CRON="/usr/bin/$PROGRAM"

# Add to user's cronjobs.
(crontab -l; echo "$TO_CRON") | crontab -


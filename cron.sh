#!/bin/sh
# where are you?
CURRENT_DIRECTORY=$PWD
# write out current crontab to temp file
crontab -l > temp_cron_file
# echo new cron into cron file
echo "0 */4 * * * python3 $CURRENT_DIRECTORY/main.py" >> temp_cron_file
# install new cron file
crontab temp_cron_file
# remove temp file
rm temp_cron_file

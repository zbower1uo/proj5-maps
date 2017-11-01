#! /bin/bash
#
# Kill all current instances of server on this machine
#
#

# Grep for all running processes containing location_server in description
# EXCEPT the grep command itself; turn them into 'kill' commands and
# execute the commands with bash
#
ps -x | grep location_server | grep -v grep | \
    awk '{print "kill " $1}' | bash



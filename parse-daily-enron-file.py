#!/usr/bin/python
#
# NAME - parse-daily-enron-file.py
# Version 0.1 (Python 2.7)
#
# SYNOPSIS
# python ./parse-daily-enron-fily.py <CSVFileNameHere>
#
# DESCRIPTION
# Takes given CSV output and converts it to JSON format and then adds an attributes array to each record and populates it with the number of recipients for each event. It will also normalize some variables and compress the original to the archive directory (see README.markdown file for more info).
#
# AUTHOR
# Ethan Cudzilo, based on source info and data provided from ForcePoint.
#
# HISTORY:
# Date(YYYY/MM/DD):     Version:        Modified By:    Description of Change:
# 2018-11-11             0.1            Ethan Cudzilo	Creation

# Imports:
import csv
import json

csvFile = sys.argv[1]

# File definitions:
banana = "test123"
csvFile = open('file.csv', 'r')
jsonFile = open('file.json', 'w')

fildNames = ("time", "message identifier", "sender", "recipients", "topic", "mode")

reader = csv.DictReader( csvfile, fieldnames)

print "test"

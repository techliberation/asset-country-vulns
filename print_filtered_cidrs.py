#!/usr/bin/env python3
import sys
import IP2Location
import csv

iptools = IP2Location.IP2LocationIPTools()

CSV_FILTERED_FILE = "filtered-ipdb.csv"

with open(CSV_FILTERED_FILE) as f:
	csv_reader = csv.reader(f, delimiter=',')
	for row in csv_reader:
		ip_start, ip_end = iptools.decimal_to_ipv4(int(row[0])), iptools.decimal_to_ipv4(int(row[1]))
		cidrs = iptools.ipv4_to_cidr(ip_start, ip_end)
		for cidr in cidrs:
			print(cidr)

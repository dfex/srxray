#!/usr/bin/env python3

import openpyxl
import logging
import argparse

def flattenJunosConfig(junosConfig):
	"""Take a Junos configuration file in Junos (bracketed) format and flatten it into set format"""
	pass

def loadJunosConfig(pathToConfig):
	"""Open a Junos configuration file - if the file is in set format, return it, otherwise convert it to set format
	and return it"""
	JunosConfigFile = open(pathToConfig, "r")
	firstLine = JunosConfigFile.readline()
	JunosConfigFile.seek(0)
	if (firstLine.startswith("set version")):
		logging.info("File is in set format")
	elif (firstLine.startswith("## Last commit:") | firstLine.startswith("version")):
		logging.info("File is in JCONF format")
	else:
		logging.info("File does not appear to be a valid Junos configuration")
	JunosConfigFile.close()

def main():
	loadJunosConfig("0ffnet-srx210-gw.conf")
	loadJunosConfig("0ffnet-srx210-gw-set.conf")
	loadJunosConfig("randomcrap.conf")

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--log', choices=['INFO', 'DEBUG', 'WARN'], help="Debug logging level")
	args = parser.parse_args()
	logging.basicConfig(level=args.log)
	main()
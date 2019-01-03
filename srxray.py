#!/usr/bin/env python3

import openpyxl

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
		print("File is in set format")
	elif (firstLine.startswith("## Last commit:") | firstLine.startswith("version")):
		print("File is in JCONF format")
	else:
		print ("File does not appear to be a valid Junos configuration")
	JunosConfigFile.close()

loadJunosConfig("0ffnet-srx210-gw.conf")
loadJunosConfig("0ffnet-srx210-gw-set.conf")
loadJunosConfig("randomcrap.conf")

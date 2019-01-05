#!/usr/bin/env python3

import logging
import argparse

def flattenJunosConfig(JunosConfig):
	"""Take a Junos configuration file in bracketed format and flattens it into set format"""
	JunosSetConfig=[]
	JunosSetLine=['set ']
	for line in JunosConfig:
			if (line.endswith("{")):
				if (line.lstrip().startswith("protect:")):
					JunosSetLine[0]="protect "
					JunosSetLine.append(line.rstrip("{").lstrip().replace('protect: ','',1)) # Remove protect from within command without stripping
					JunosSetConfig.append(JunosSetLine[:]) # Copy by value, not reference
					JunosSetLine[0]="set "
				else:										
					JunosSetLine.append(line.rstrip("{").lstrip())
			elif (line.endswith(";")):
				if (line.lstrip().startswith("protect:")):
					# First create the line as normal without the protect statement:
					JunosSetLine.append(line.rstrip(";").lstrip(" ").replace('protect: ','',1)) # Remove protect from within command without stripping
					JunosSetConfig.append(JunosSetLine[:]) # Copy by value, not reference
					JunosSetLine.pop()
					# Now create the protected line without the parameter on the end:
					JunosSetLine[0]="protect "
					logging.debug(JunosSetLine)
					JunosSetLine.append(" ".join(line.rstrip(";").lstrip(" ").replace('protect: ','',1).split()[:2])) # Removes protect and only appends first 2 config elements - UGLY
					JunosSetConfig.append(JunosSetLine[:]) # Copy by value, not reference
					JunosSetLine[0]="set "
					JunosSetLine.pop()
				else:
					JunosSetLine.append(line.rstrip(";").lstrip())
					JunosSetConfig.append(JunosSetLine[:]) # Copy by value, not reference
					JunosSetLine.pop()
			elif (line.endswith("}")):
				JunosSetLine.pop()
	return(JunosSetConfig)

def loadJunosConfig(pathToConfig):
	"""Open a Junos configuration file - if the file is in set format, return it as a list, otherwise
	convert it to set format and then return it as a list and return it"""
	JunosConfig=[]
	with open(pathToConfig, "r") as JunosConfigFile:
		for line in JunosConfigFile:
			JunosConfig.append(line.rstrip())
		if (JunosConfig[0].startswith("set version")):
			logging.info("File is in set format")
			return JunosConfig
		elif (JunosConfig[0].startswith("## Last commit:") | JunosConfig[0].startswith("version")):
			logging.info("File is in JCONF format")
			return (flattenJunosConfig(JunosConfig))
		else:
			logging.info("File does not appear to be a valid Junos configuration")

def printJunosConfig(JunosConfig):
	for line in JunosConfig:
		for term in line:
			print (term, end="")
		print ()

def main():
	pass

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--log', choices=['INFO', 'DEBUG', 'WARN'], help="Debug logging level")
	args = parser.parse_args()
	logging.basicConfig(level=args.log)
	main()
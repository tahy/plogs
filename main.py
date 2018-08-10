#! /usr/bin/python

import logging
import os
import sys

from analyser.analyser import LogAnalyser

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger('logger')

if __name__ == "__main__":
	try:
		path = sys.argv[1]
	except IndexError:
		logger.error("Not enough arguments, use analyse.py <path_to_log>")
		exit()
	logger.info("Start parsing file: %s" % path)
	try:
		analyser = LogAnalyser(path)
	except LAFileNotFoundException as e:
		logger.error(e)
	logger.info("End parsing file")	
	print ("total sended: %d " % analyser.total_sended())
	print ("total failed: %d " % analyser.total_failed())
	print ("Example sended by email [katya@dalvl.ru] -- %d " \
			% analyser.sended_by_email('katya@dalvl.ru'))


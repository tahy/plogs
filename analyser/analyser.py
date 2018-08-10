"""module description: analyser class"""

import os
import re
from copy import deepcopy


class LogAnalyser():
	"""Class for analyse log file"""

	PATTERN_FROM = re.compile("^([^\s]+\s+){5}(\w{11}):\s+from=<([^\s]*)>(.*)$")
	PATTERN_TO = re.compile("^([^\s]+\s+){5}(\w{11}):\s+to=<([^\s]*)>(.*)status=(\w+)(.*)$")
	PATTERN_REMOVE = re.compile("^([^\s]+\s+){5}(\w{11}):\s+removed(.*)$")

	def __init__(self, path):
		self.failed = 0
		self.sended = 0
		self.path = path
		self.froms = {}
		self.result = {}

		if not os.path.exists(self.path):
			raise LAFileNotFoundException("File does not exist!")
		self.process()

	def sended_by_email(self, email):
		"""return count sended letters by from email"""
		return self.result[email]

	def total_sended(self):
		"""return total sended emails"""
		return self.sended
	
	def total_failed(self):
		"""return total failed emails"""
		return self.failed

	def add_from(self, email_id, email):
		self.froms.setdefault(email_id, {'sended': 0, 'from': email})

	def inc(self, email_id):
		item = self.froms.get(email_id, None)
		if item:
			item['sended'] += 1
			self.sended += 1

	def to_result(self, email_id):
		item = self.froms.get(email_id, None)
		if item:
			self.result[item['from']] = item['sended']
			del item

	def analyse(self, line):
		result = self.PATTERN_FROM.match(line)
		if result:
			groups = result.groups()
			self.add_from(groups[1], groups[2])
			return

		result = self.PATTERN_TO.match(line)
		if result:
			groups = result.groups()
			if groups[4] != 'sent':
				self.failed += 1 
			else:
				self.inc(groups[1])
			return
	
		result = self.PATTERN_REMOVE.match(line)
		if result:
			groups = result.groups()
			self.to_result(groups[1])
			return

	def process(self):
		with open(self.path) as f:
			for line in f:
				self.analyse(line)


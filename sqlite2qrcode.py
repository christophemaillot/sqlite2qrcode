#!/usr/bin/env python

import sys
import sqlite3
import re
import qrcode

class Converter:
	
	def convert(self, path):
		conn = sqlite3.connect(path)
		c = conn.cursor()
		c.execute("select * from accounts")
		rows = c.fetchall()
		for row in rows:
			name = re.sub('[^0-9a-zA-Z]+', '_', row[1])

			print name
			img = qrcode.make("otpauth://totp/" + row[1] + "?secret=" + row[2])
			img.save(name + ".png")

conv = Converter()
conv.convert(sys.argv[1])

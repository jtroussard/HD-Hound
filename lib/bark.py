#!/usr/bin/python3

import smtplib

from lib.testconfig import *
from lib import point

"""Provides functions necessary to transmit content via email.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

__author__     = "Jacques Troussard"
__copyright__  = "Copyright 2017, TekkSparrows"
__date__       = "Fri Aug 03 2017"
__version__    = "0.0.1"
__maintainer__ = "Jacques Troussard"
__email__      = "tekksparrows@gmail.com"
__status__     = "development"


def bark():
	# do stuff with point module to create email content
	# content which goes into the email
	content = point.createContent()
	from_head = "From: Hard Drive Hound <{}>\n".format(FROM_EMAIL)
	rece_head = "To: {} <{}>\n".format(RECE_EMAIL,RECE_EMAIL)
	subj_head = "Subject: Hard Drive Hound has found something interesting!\n\n"

	email_msg = from_head + rece_head + subj_head + content
	debuglevel = True

	try:
		# params (mail server:port) **ports may change** 465 is alternate?
		mail = smtplib.SMTP(SERVER, PORT)
		mail.set_debuglevel(debuglevel)

		# id yourself to the server (ehlo/hello)
		mail.ehlo()

		# start tls
		mail.starttls()

		# as per documention call ehlo again after tls
		mail.ehlo()

		# login to mail account
		mail.login(SNDR_EMAIL, SNDR_PASSW)

		# send email
		mail.sendmail(FROM_EMAIL, RECE_EMAIL, email_msg)

		# close connection
		mail.quit()
	except Exception as e:
		print(type(e))
		print(e)
		print ("Error sending mail")
		return None

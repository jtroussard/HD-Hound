#!/usr/bin/python3

"""Provides functions necessary to analyze data for content delivery.

Determines if parameters for price, brand, quality, whatever have been met. Also
creates content to be transmitted via email.

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

import pymongo
import pprint
from decimal import *
from pymongo import MongoClient


__author__     = "Jacques Troussard"
__copyright__  = "Copyright 2017, TekkSparrows"
__date__       = "Fri Aug 04 2017"
__version__    = "0.0.1"
__maintainer__ = "Jacques Troussard"
__email__      = "tekksparrows@gmail.com"
__status__     = "development"

# for now I am hard coding the db and collection, up to this point there is 
# very little functionality in this scrapper. I realize that db access should
# be separate from business logic now but I guess too late for that now.
def ConnectToMongo():
	try:
		client = MongoClient()
		return(client)
	except Exception as e:
		print(type(e))
		print(e)
		print ("Error connecting with MongoClient")
		return None


# Searches db for any records that meet conditions to send alert email
def valueTrigger():
	 conn = ConnectToMongo()
	 if conn == None:
	 	print ("Connection Error: valueTrigger aborted")
	 	return

	 # get database and collection
	 db = conn.price_hound
	 collection = db.hard_drives

	 # threshold is hardcoded to 38 gb per dollar
	 cursor = collection.find({ "GB_per_mu": { "$gt" : 38 } }).count()
	 return (cursor)

def priceErrorTrigger():
	conn = ConnectToMongo()
	if conn == None:
		print ("Connection Error: priceErrorTrigger aborted")
		return

	# get database and collection
	db = conn.price_hound
	collection = db.hard_drives
	
	# for now thresholds are hard coded. if additional checks need to be made
	# just add them in the list within the if statement. idea for future is to
	# print to an error log exactly which one triggered the boolean to be 
	# switched and maybe add additional details to help in debugging.
	result = False
	if collection.find({"$or": # command and start query filter
		[
		{"price": None}, # chk 1: soup parsing error
		{"GB_per_mu": {"$gt": 100}} # chk 2: gbmu calc error
		]
		}).count() > 0: # cursor modifications and comparator

		result = True
	return (result)

def createContent():
	conn = ConnectToMongo()
	if conn == None:
		print ("Connection Error: createContent aborted")
		return

	# get database and collection
	db = conn.price_hound
	collection = db.hard_drives

	bestValue = collection.find_one(sort = [('GB_per_mu',-1)])
	bvPrice = round(Decimal(bestValue['price']),2)
	bvLineLength = 13 + len(bestValue['description'])
	bvSpacer = ('.' * (80 - bvLineLength))
	bvLine = "Best Value: {}{}${}\nhttp://www.microcenter.com/{}\n\nOther Drives That Meet Your Requirments\n".format(
		bestValue['description'], bvSpacer, str(bvPrice), bestValue['link'])

	othersList = ""
	docCount = 0
	docTitle = ""
	docPrice = 0.00
	#docLineLength = 0
	#docSpacer = 0
	for doc in collection.find({"GB_per_mu": {"$gt": 38}}):
		docCount += 1
		docTitle = doc['description']
		docLeader = str(docCount) + ": " + docTitle + " "
		docLeader = docLeader.ljust(100, '.')
		docPrice = round(Decimal(doc['price']),2)
		#docLineLength = len(str(docCount)) + 2 + len(docTitle)
		#docSpacer = ('.' * (80 - docLineLength))
		docLine = docLeader + "$" + str(docPrice) + "\n"
		othersList += docLine
	content = bvLine + othersList

	return content

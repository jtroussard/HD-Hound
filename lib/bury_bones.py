#!/usr/bin/env python

"""Provides functions necessary to store, retieve & analyze data from hd hound.

findBones, makeSoup, and loadItems collect and parce the data scraped from 
microcenters webpage, under a non-specfic store. During development many of
the search parameters will be hardcoded. For this version the results will be
of internal hard drive units. ***Further functions will provide anaylsis(price
per GB/MB, lowest, highest etc.) and operational abilities(email alerts and
db actions --- might do a separate module for this)
"""

import pymongo
import pprint
from re import sub
from decimal import Decimal
from pymongo import MongoClient

__author__     = "Jacques Troussard"
__copyright__  = "Copyright 2017, TekkSparrows"
__date__       = "Fri Jun 23 2017"
__version__    = "0.0.1"
__maintainer__ = "Jacques Troussard"
__email__      = "tekksparrows@gmail.com"
__status__     = "Development"

# for now I am hard coding the db and collection, up to this point there is 
# very little functionality in this scrapper. once this first iteration is done
# this will be modified to allow for more control
def ConnectToMongo():
	try:
		client = MongoClient()
		return(client)
	except Exception as e:
		print(type(e))
		print(e)
		print ("Error connecting with MongoClient")
		return None

# If price exists, convert price and size data into a usable float and int
# determine size factor (TB/GB), and perform dimensional anaylsis, results
# gbpd, in Gigabytes per unit ($USD). Missing price info expressed with the
# string 'Unknown'. Since using mongodb I dont think that will be a major
# but I'm already running into some annoyances cause by this mixing of types
# when testing/queryuing the db in mongoshell. May change this to a negative
# number or something if a price is not found.
def calc_gpmu(price, size):
	gpmu = 0.0
	if price:
		p_value = float(sub(r'[^\d.]', '', price))
		s_factr = 0
		if 'TB' in size:
			s_factr = 1000
		else:
			s_factr = 1
		s_value = round(float(sub(r'[A-Z]', '', size)),1)
		gpmu = (s_value * s_factr)/p_value
	else:
		price = -1
		gpmu = -1
	return gpmu


def insert_doc(dt, brand, fid, name, price, link, size):
	conn = ConnectToMongo()
	if conn == None:
		print("Connection Error: Insert Doc Aborted")
		return
	
	# create collection var
	db = conn.price_hound
	collection = db.hard_drives

	# create collection counter vars for seq number and to use to check if
	# insert was successful
	original_count = collection.count()
	sequence = collection.count() + 1
	
	# calculate gigabyte per monetary unit and set up pretty printer (printer
	# was exclusivly for debugging during development... remove?)
	gpmu = calc_gpmu(price, size)
	pp = pprint.PrettyPrinter(indent=4)

	# Find out if document already exits by searching for microcenter item id
	# search for updates in item and make necessary changes. If document is new then insert new doc to db
	if collection.find_one( { 'foreign_id_number': fid, 'brand': brand, 'link': link } ):
		doc = collection.find_one( { 'foreign_id_number': fid, 'brand': brand, 'link': link } )
		# debug check doc before changes
		# pp.pprint(doc)
		# update last scrape value and check for price difference
		if doc['last_scrape'] != dt:
			collection.update_one( { '_id': doc['_id'] }, { '$set': { 'last_scrape': dt } } )
		if doc['price'] != price:
			print('item match found, updating record . . .')
			# create new history entry and perform update
			he_entry = {'he-date': doc['last_scrape'], 'he-price': doc['price'], 'he-gpmu': doc['GB_per_mu'] }
			collection.update_one( { '_id': doc['_id'] }, { '$set': { 'price': price, 'GB_per_mu': gpmu }, '$push': { 'history': he_entry } })
	else:
		collection.insert_one(
			{
				'seq' : sequence,
				'description' : name,
				'last_scrape' : dt,
				'brand' : brand,
				'foreign_id_number' : fid,
				'price' : price,
				'link' : link,
				'hd_size' : size,
				'GB_per_mu' : gpmu,
				'History' : [] # history is list to facilitate/be compatible w/ $push command
			}
		)
		# logic test to confirm document was added to collection
		if (original_count < collection.count()):
			print("\tDoc insert SUCCESSFUL")
		else:
			print("\tDoc insert UNSUCCESSFUL")
	# debug check doc for changes, reload doc variable to make comparision via console
	# doc = collection.find_one( { 'foreign_id_number': fid, 'brand': brand, 'link': link } )
	# pp.pprint(doc)

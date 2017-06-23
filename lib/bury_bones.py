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
import datetime
import bson
from bson.decimal128 import Decimal128 as d128
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

def ConnectToMongo():
	try:
		client = MongoClient()
		return(client)
	except Exception as e:
		print(type(e))
		print(e)
		print ("Error connecting with MongoClient")
		return None

def get_db(client, database):
	try:
		db = client.database
		return (db)
	except Exception as e:
		print(type(e))
		print(e)
		print ("Error getting database")
		return None

def get_collection(db_name, col_name):
	print("===MONGO-GETCOLLECTION===")
	try:
		conn = ConnectToMongo();
		db = conn.price_hound
		collection = db.hard_drives
		results = collection.find()
		print("\tresult test:{}".format(results))
		return (results)
	except Exception as e:
		print(type(e))
		print(e)
		print ("Error getting collection")

def insert_doc(dt, brand, fid, name, price, link, size):
	print("===MONGO-INSERTDOC===")
	print("\targs= {}, {}, {}, {}, {}, {}, {}".format(
			dt,
			brand,
			fid,
			name,
			price,
			link,
			size
			)
		)
	conn = ConnectToMongo();
	if conn == None:
		print("Connection Error: Insert Doc Aborted")
		return None
	
	db = conn.price_hound
	collection = db.hard_drives
	original_count = collection.count()
	sequence = collection.count() + 1

	if price:
            p_value = float(sub(r'[^\d.]', '', price))
	    s_factr = 0
	    if 'TB' in size:
	        s_factr = 1000
	    else:
	        s_factr = 1
	    s_value = int(sub(r'\D', '', size))
	    gbpd = (s_value * s_factr)/p_value
	    print ("gb per dollar:" + str(gbpd))
	else:
	   price = "Unknown"
	   gbpd = "Unknown"

	if collection.find_one({"foreign_id_number": fid}):
		print("if find one fid PASSED below find results")
		print(collection.find_one({"foreign_id_number": fid}))

	else:
		print("if find one fid FAILED below find results")
		print(collection.find_one({"foreign_id_number": fid}))

		collection.insert_one(
			{
				"seq" : sequence,
				"description" : name,
				"last_scrape" : dt,
				"brand" : brand,
				"foreign_id_number" : fid,
				"price" : price,
				"link" : link,
				"hd_size" : size,
				"price_per_GB" : gbpd
			}
		)
	
	if (original_count < collection.count()):
		print("\tDoc insert SUCCESSFUL")
	else:
		print("\tDoc insert UNSUCCESSFUL")

	print(collection.find({"seq": sequence}))


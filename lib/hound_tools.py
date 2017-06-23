#!/usr/bin/env python

"""Provides tools necessary for obtaining and parcing webscarbed data.

findBones, makeSoup, and loadItems collect and parce the data scraped from 
microcenters webpage, under a non-specfic store. During development many of
the search parameters will be hardcoded. For this version the results will be
of internal hard drive units. ***Further functions will provide anaylsis(price
per GB/MB, lowest, highest etc.) and operational abilities(email alerts and
db actions --- might do a separate module for this)
"""

import time
import datetime
import re
import bs4 as bs
import urllib.request

__author__     = "Jacques Troussard"
__copyright__  = "Copyright 2017, TekkSparrows"
__date__       = "Fri Jun 23 2017"
__version__    = "0.0.1"
__maintainer__ = "Jacques Troussard"
__email__      = "tekksparrows@gmail.com"
__status__     = "Development"

def findBones(page):
	# create url string for server request
	url_base = 'http://www.microcenter.com/search/search_results.aspx?'
	# filter is a list because microcenter cats are treated as filters in the case
	# filters need to be added for different products (brand, compaitility) they 
	# can simply be added to the url via a for loop reading the url_filt list
	list_filters = []
	# Hard code filter into a variable(Internal Hard Drives) and load element into 
	# list. Build filter list using for loop - future interations might have many
	# filters. '+' separate filters as per html source code obs for microcenter.
	filter_element_ihd = '4294945772'
	list_filters.append(filter_element_ihd)
	# create emptry string for filters and build with for loop
	url_filt = ""
	for attr in list_filters:
		if not url_filt:
			url_filt = "N=" + attr
		else:
			url_filt += "+" + attr
	# current page
	if page == 0:
		url_page = 1
	else:
		url_page = page
	# compile string for request
	url_string = url_base + url_filt + "&page=" + str(url_page) + "&myStore=false"
	# # debug check
	# print (url_string)
	return url_string

def getPageValue(soup):
	# record number of pages
	num_of_pages = int(soup.find("ul", {"class": "pages inline"}).find_all("li")[-2].text)
	# # test print page variable and do some math with it to confirm type
	# print (num_of_pages+100)
	return num_of_pages

def makeSoup(url_string):
	# load sauce, load soup
	sauce = urllib.request.urlopen(url_string).read()
	soup = bs.BeautifulSoup(sauce, 'lxml')

	# for testing purposes dump requests in text file and save to disk
	path = '/home/jacques/Projects/hdscrape/'
	filename = 'demo.html'

	# # debug/sample
	# f = open(path + filename, 'w')
	# f.write(str(soup))
	# print(f)
	return soup

# Returns list of items, where each item is a dict object
def loadItems(number_of_pages):
	# product_details list will contain raw info from <a> drilled down to each
	# product detail div. hd_results will contain list of dicts, essentially
	# the parced data from produict details.
	product_details = []
	hd_results = []
	num_of_items = 0
	links_used = []

	for i in range(number_of_pages):
		print ("Loading page #" + str(i+1) + " . . . .")
		url = findBones(i+1)
		links_used.append(url)
		soup = makeSoup(url)

		# load unordered list of products in grid variable
		grid = soup.body.section.article.find("ul", {"role": "tabpanel"})
		# # debug statement
		# print (grid)

		# find all porducts
		products = grid.find_all("div", {"class": "normal"})
		# # debug print statement
		# print (products)

		# # test print for variable products
		# count = 0
		for item in products:
			num_of_items += 1
		# 	print (str(count) + ": "  + str(item) + "\n\n")

		# load unparced data into products list
		for item in products:
			product_details.append(item.a)

		# tag counter
		t_count = 0
		# parce products list into dictionaries and load into hd_results list
		for item_tag in product_details:
			t_count += 1
			entry = 
				{
					'brand': item_tag['data-brand'],
					'id': item_tag['data-id'],
					'name': item_tag['data-name'],
					'price': item_tag['data-price'],
					'link': item_tag['href']
				}
			# for now i'm just parsing the name for the hardrive size
			# but in newer version I want to dig deeper and pull the data from
			# the actual item page.
			item_storage_size = ""
			p = re.search(re.compile([0-9]+((TB)|(GB))), entry['name'])
			if p.group():
				item_storage_size = p.group(0)
			else:
				item_storage_size = "Unknown"
			entry['hdSize': item_storage_size]

			hd_results.append(entry)
		print ("  " + str(t_count) + "tag(s) processed")
		# reset list for next page
		product_details = []

		# # nicely formatted test print of hd_results
		# count = 1
		# for res in hd_results:
		# 	print("entry number " + str(count) + ": ")

		# 	for key in res:
		# 		print (key + " - " + res[key])
		# 	print ("\n")
		# 	count += 1
	# debug/sample search result stats
	print ("number of entries recieved: " + str(num_of_items))
	for link in links_used:
		print (link + "\n")
	print ("length of list, hd_results: " + str(len(hd_results)))
	time.sleep(3)

	return hd_results





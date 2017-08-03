
import datetime
import pprint
import pymongo
from lib import hound_tools as ht
from lib import bury_bones as bb 

now = datetime.datetime.now()
pp = pprint.PrettyPrinter(indent=4)

string = ht.findBones(0) # builds url for request

soup = ht.makeSoup(string) # make initial soup
pages = ht.getPageValue(soup) # determine how many pages search query returned

results = ht.loadItems(pages) # parse data into results var for loading into db

# # test print results
pp.pprint(results)

# load items into db
for item in results:
	bb.insert_doc(item['dateScrapped'], item['brand'], item['id'], item['name'], item['price'], item['link'], item['hdSize'])

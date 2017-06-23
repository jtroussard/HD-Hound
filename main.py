
import datetime
import pprint
from lib import hound_tools as ht
from lib import bury_bones as bb 

now = datetime.datetime.now()
pp = pprint.PrettyPrinter(indent=4)

string = ht.findBones(0)

soup = ht.makeSoup(string)
pages = ht.getPageValue(soup)

results = ht.loadItems(pages)

# # test print results
# pp.pprint(results)

# load items into db
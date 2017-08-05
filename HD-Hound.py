
#!/usr/bin/env python

import datetime
import pymongo
from lib import sniff
from lib import bury
from lib import point
from lib import bark

"""Provides configuration information necessary to authenticate email.

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

# record datetime information
now = datetime.datetime.now()

string = sniff.findBones(0) # builds url for request

soup = sniff.makeSoup(string) # make initial soup
pages = sniff.getPageValue(soup) # determine how many pages search query returned

results = sniff.loadItems(pages) # parse data into results var for loading into db

# load items into db
for item in results:
	bury.insert_doc(item['dateScrapped'], item['brand'], item['id'], item['name'], item['price'], item['link'], item['hdSize'])

# if hound found something, send email
if point.valueTrigger() > 0 and not point.priceErrorTrigger() > 0:
	bark.bark()
else:
	print("HD hound didn't find anything interesting")

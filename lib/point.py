#!/usr/bin/env python

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
from pymongo import MongoClient

__author__     = "Jacques Troussard"
__copyright__  = "Copyright 2017, TekkSparrows"
__date__       = "Fri Aug 03 2017"
__version__    = "0.0.1"
__maintainer__ = "Jacques Troussard"
__email__      = "tekksparrows@gmail.com"
__status__     = "development"
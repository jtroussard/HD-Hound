import bs4 as bs
import urllib.request

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
url_page = 1
# last page: counter set to zero for a no results found sce. this is not proven
# or tested *** may not need *** HTML source discovery: ideas for page numbers
# you're going to have to make some internal check for the last page number,
# check google search didn't find any native function for extracting a specfic
# line item number (might want to research that more)
page_counter = 0

# compile string for request
url_string = url_base + url_filt + "&page=" + str(url_page)
# debug check
print (url_string)

# load sauce, load soup
sauce = urllib.request.urlopen(url_string).read()
soup = bs.BeautifulSoup(sauce, 'lxml')

# for testing purposes dump requests in text file and save to disk
path = '/home/jacques/Projects/hdscrape/'
filename = 'demo.html'

# load unordered list of products in grid variable
grid = soup.body.section.article.find("ul", {"role": "tabpanel"})
#print (grid)
# find all porducts
products = grid.find_all("h2")
product_details = []
hd_results = []
for item in products:
	product_details.append(item.a)
for item_tag in product_details:
	entry = {'brand': item_tag['data-brand'], 'id': item_tag['data-id'], 
		'name': item_tag['data-name'], 'price': item_tag['data-price'], 
		'link': item_tag['href'], }
	hd_results.append(entry)

counter = 1
for res in hd_results:
	print("entry number " + str(counter) + ": ")

	for key in res:
		print (key + " - " + res[key])
	print ("\n")
	counter += 1

f = open(path + filename, 'w')
f.write(str(soup))
print(f)



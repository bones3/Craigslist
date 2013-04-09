import re
import urllib2
import sys

keyword = sys.argv[1]

for keyword in sys.argv[1:]:

	# Retrieve the URL
	urlsfc = 'http://sfbay.craigslist.org' + \
	    '/search/jjj/sfc?query=' + keyword

	urleby = 'http://sfbay.craigslist.org' + \
	    '/search/jjj/eby?query=' + keyword 

	# Read contents
	contents_sf = urllib2.urlopen(urlsfc).read()
	contents_eby = urllib2.urlopen(urleby).read()
	# count.

	found = re.findall(r'Found: (\d+)', contents_sf)
	count_sf = int(found[0])

	found = re.findall(r'Found: (\d+)', contents_eby)
	count_eby = int(found[0])

	# Print results
	print '{keyword} jobs in SF: {count}'.format(
	    keyword=keyword, count=count_sf)

	print '{keyword} jobs in East Bay: {count}'.format(
	    keyword=keyword, count=count_eby)
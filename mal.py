import urllib2, string, variables, requests
from xml.dom.minidom import parseString

query = 'bleach'
get = '?q=' + query
r = requests.get('http://myanimelist.net/api/anime/search.xml' + get, auth = ('malgrabberirc', 'MALgrab'))


print r.status_code
print r.headers ['content-type']
print r.text


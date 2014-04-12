import variables, urllib2, json as simplejson, string, HTMLParser
from xml.dom.minidom import parseString

def mal2(send_data, msgarr, user):

	
	if len(msgarr) < 2 or 'hentai' in msgarr:
		send_data("PRIVMSG %s :No or Bad seatch string." % variables.channel)
	else:
		url = 'http://cdn.animenewsnetwork.com/encyclopedia/api.xml?title=~' + msgarr[0]
		file = urllib2.urlopen(url)
	
		data = file.read()
		file.close()
		dom = parseString(data)
		id = [elt.getAttribute('id') for elt in dom.getElementsByTagName('anime')]
		

		#print xmlTag		 #	For Testing ONLY
		#print xmlData		 #	For Testing ONLY
		#id = str(id)
		aniurl = 'http://www.animenewsnetwork.co.uk/encyclopedia/anime.php?id=' % id
		send_data("PRIVMSG %s: %s" % (variables.channel, aniurl) )
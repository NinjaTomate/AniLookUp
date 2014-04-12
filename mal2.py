import variables, urllib2, json as simplejson, string, HTMLParser
from xml.dom.minidom import parseString

def mal2(send_data, msgarr, user):
	if len(msgarr) < 2 or 'hentai' in msgarr:
		send_data("PRIVMSG %s :No or Bad seatch string." % variables.channel)
	else:
		file = urllib2.urlopen('http://cdn.animenewsnetwork.com/encyclopedia/api.xml?title=~%s' % msgarr)
		data = file.read()
		file.close()
		dom = parseString(data)

		xmlTag = dom.getElementsByTagName('id')[0].toxml()
		xmlData = xmlTag.replace('<anime id=', '').replace('</anime>', '')

		#print xmlTag		 #	For Testing ONLY
		#print xmlData		 #	For Testing ONLY

		send_data("PRIVMSG %s: http://www.animenewsnetwork.co.uk/encyclopedia/anime.php?id=%s" (variables.channel, id))
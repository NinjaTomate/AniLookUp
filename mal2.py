import variables, urllib2, json as simplejson, string, HTMLParser
from xml.dom import minidom

def mal2(send_data, msgarr, user):
	if len(msgarr) < 2 or 'hentai' in msgarr:
		send_data("PRIVMSG %s :No or Bad seatch string." % variables.channel)
	else:
		try:
			request = string.join(msgarr[1:])
			print request
			data = urllib2.urlopen('http://cdn.animenewsnetwork.com/encyclopedia/api.xml?title=%s' % request).read()
			xmldoc = minidom.parseString(data)
			xmlTag = xmldoc.getElementsByTagName('ann')
			print xmlTag
			print len(xmlTag)
			for s in xmlTag:
				print s.attributes['warning'].value

			#print xmlTag		 #	For Testing ONLY
			#print xmlData		 #	For Testing ONLY

			#send_data("PRIVMSG %s :http://www.animenewsnetwork.co.uk/encyclopedia/anime.php?id=%s" (variables.channel, id))
		except Exception as e:
			print e
			send_data("PRIVMSG %s :uwaaah?~~" % variables.channel)
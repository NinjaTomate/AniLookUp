#Code from YT lookup module by NinjaTomate (https://github.com/NinjaTomate/UpBot/blob/master/modules/yt.py)
import urllib2, urllib, string, HTMLParser
from xml.dom.minidom import parseString

def mal(send_data, msgarr, user):
	if len(msgarr) < 2:
		send_data("PRIVMSG %s :No or invalid search string supplied." % variables.channel)
	else:
		try:
			parser = HTMLParser.HTMLParser()
			query = string.join(msgarr)[3:]
			getTag = dom.getElementsByTagName
			url = "http://myanimelist.net/api/anime/search.xml?q=" % query
			print query
			file = urllib2.urlopen(url)
			data = file.read()
			file.close()
			dom = parseString(data)
			xmlID = getTag('id')
			xmlName = getTag('title')
			xmlType = getTag('type')
			xmlStatus = getTag('status')
			ID = xmlTag.replace('<id>','').replace('</id>','')
			Name = xmlTag.replace('<title>','').replace('</title>','')
			Type = xmlTag.replace('<type>','').replace('</type>','')
			Status = xmlTag.replace('<status>','').replace('</status>','')
			send_data("PRIVMSG %s :", Name, "http://myanimlist.net/anime/" % (ID, Type, Status, variables.channel))
		except:
			send_data("PRIVMSG %s : No anime found by that name, or incorrect name entered" % variables.channel)
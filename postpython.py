import urllib2, urllib

#url = 'http://192.168.1.3/epreuves/WEB/epreuve2/page2.php'
#data = urllib.urlencode({'login' : 'MyLogin', 'password' : 'MyPassword'})
#req = urllib2.Request(url, data)
#response = urllib2.urlopen(req)
d = 100
print d
 
url2 = "http://sarpinto.com/project/infus/send.php?level="+str(d)
#req2 = urllib2.Request(url2, data)
r2 = urllib2.urlopen(url2)
#print r2.read()

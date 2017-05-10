from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url= 'http://codeforces.com/contest/789/problem/A'

# opening up connection and grabbing the page
uClient = uReq(my_url)

#offloads content into variable
page_html = uClient.read()
#close 
uClient.close()

#html parsing
page_soup=soup(page_html, "html.parser")

inputs = page_soup.findAll("div", {"class":"input"})

f1 = open('testcases','w')

f1.write(str(len(inputs))+"\n")

for inp in inputs:
	xyz = str(inp.pre)
	xyz = xyz.replace("<br/>","\n")
	xyz = xyz.replace("<pre>","")
	xyz = xyz.replace("</pre>","")
	f1.write(xyz)
outputs = page_soup.findAll("div", {"class":"output"})

f2 = open('testsoln','w')

for op in outputs:
	xyz = str(op.pre)
	xyz = xyz.replace("<br/>","\n")
	xyz = xyz.replace("<pre>","")
	xyz = xyz.replace("</pre>","")
	f2.write(xyz)
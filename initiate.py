from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup

contestid='764'
pid='A'
my_url='http://codeforces.com/contest/'+contestid+'/problem/'+pid

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
idx = 1;

for inp in inputs:
	f = open('test'+str(idx), 'w')
	xyz = str(inp.pre)
	xyz = xyz.replace("<br/>","\n")
	xyz = xyz.replace("<pre>","")
	xyz = xyz.replace("</pre>","")
	f.write(xyz)
	idx=idx+1;

outputs = page_soup.findAll("div", {"class":"output"})
idx=1

for op in outputs:
	f = open('soln'+str(idx), 'w')
	xyz = str(op.pre)
	xyz = xyz.replace("<br/>","\n")
	xyz = xyz.replace("<pre>","")
	xyz = xyz.replace("</pre>","")
	idx=idx+1
	f.write(xyz)

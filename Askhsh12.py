import urllib2
import json
import webbrowser
par=raw_input("Bres xiliades suntages eukola kai grhgora!!Ti ulika exete sthn diathesh sas?: ")
api='http://food2fork.com/api/search?key=760769c535326e59a995f6621a0db324&q=';
lista=list(api)
lista.extend([par])
link=''.join(lista)
response = urllib2.urlopen(link)
html = response.read()
html=html.replace("<br>","")
html=html.strip()
lines=html.split("\n")
header= lines[0].split(",")
print "H suntagh sas exei: ",header[3];
response1 = urllib2.urlopen('https://api.punkapi.com/v2/beers/random')
html1 = response1.read()
html1=html1.replace("<br>","")
html1=html1.strip()
lines1=html1.split("\n")
header1= lines1[0].split(",")
print "H mpura sas exei: ",header1[1];
x=raw_input("Gia na metafertheite sto website ths suntaghs,wste na diabasete ton tropo paraskeuhs,eisagete to 0: ")
while x!="0":    
    x=raw_input("Gia na metafertheite sto website ths suntaghs,wste na diabasete ton tropo paraskeuhs,eisagete to 0: ")
x=list(header[4])
del x[0:16]
del x[-1]
link=''.join(x)
webbrowser.open(link)
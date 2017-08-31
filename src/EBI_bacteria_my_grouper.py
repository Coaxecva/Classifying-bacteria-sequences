from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen

r = urlopen("http://www.ebi.ac.uk/genomes/bacteria.html")
#print(r)

#soup = BeautifulSoup(r)
soup = BeautifulSoup(r, "lxml")
#print(type(soup))
#print(soup.prettify()[0:20])


#taxas = soup.find_all('a', {'target':'taxWindow'})
#print (type(taxas))
#print(taxas[0])

taxas = soup.find_all('td', {'colspan':'7'})

for taxa in taxas:
	print(taxa.getText())

#print("DONE")

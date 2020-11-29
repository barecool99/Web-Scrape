#libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup 
#the website you wanna scrap
url_to_scrape = "https://planetdesert.com/collections/cactus"
#opens url request
request_page = urlopen(url_to_scrape)
#read the page
page_html = request_page.read()
#close the request
request_page.close()
#.lxml parses the html
html_soup=BeautifulSoup(page_html,'lxml')
#go to the web and think of what u wanna grab
cactus_items=html_soup.find_all('div', class_= "grid-product__content")
#save it in this file
filename ='products.csv'
#open the file
f=open(filename,'w')
#file name headers with a space
headers='Title, Price \n'
#write the header
f.write(headers)
# put the cactuc item in an array and we find title and price 
for cactus in cactus_items:
    title = cactus.find('div', class_="grid-product__title").text
    price = cactus.find('div', class_="grid-product__price").text
#when writing into csv file, have commas seperated bc its csv files
    f.write(title + ','+ price)
# close the file after done
f.close()





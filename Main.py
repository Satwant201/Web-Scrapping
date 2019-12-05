### requests library is used for fetching the dta from a html page
import requests
import urllib.request
import time
## BeautifulSoup is a very cool library, you can also check out scrapy library ( highly autmoated and parameterized )
## to study more about this lib, refer https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup

## Target URL
url = 'http://web.mta.info/developers/turnstile.html'

response = requests.get(url)

## if the previuos command was successful, then 

soup = BeautifulSoup(response.text, “html.parser”)

## in scrapping, the whole intention is to pull labels satisfying either a string or a regex
## here i am planning to pull all labels containing "coders"

all_tags = soup.findAll('coders')

##This code gives us every line of code that has an <coders> tag in form of a "list"

# now lets try to actually reach out to some underlying url with tag "a"

single_tag = all_tags[12]
link = single_tag[‘href’]

download_url = 'http://web.mta.info/developers/'+ link
urllib.request.urlretrieve(download_url,'./’'link[link.find('/turnstile_')+1:]) 

note that a request command could take from few ms to to a few seconds, so when you try to run a loop, do keep sleep commands in the code


# Proxy List Generator
##### Scraps proxylist and gives a list of proxies along with port numbers..

## Highly Recommended for:
    1. Web Scrapers
    2. Web Crawlers
    3. Pen Testers
    4. People who want list of proxies in Bulk

## How it Works?
	It scraps [free-proxy-list.net] and extracts all the IPs and Port Numbers...
	
## requirements:
	1. requests
	2. BeautifulSoup
	3. html5lib
	
### run the following command before executing the script for the first time
	pip install requests BeautifulSoup4 html5lib
	
#### In case of the following error:
	AttributeError: module 'html5lib.treebuilders' has no attribute '_base'
#### run the following command 
	pip install --upgrade beautifulsoup4
	pip install --upgrade html5lib

## Usage
    Just import proxy_get in your code and call the function Proxy_List() for list of proxies

#### On Success:
    returns List of proxies
    example:
      [["192.168.1.1":"8080"],["localhost","8080"]]
    
#### On Failure:
    returns None
    
### Important:

    feel free to tweak it as much as you like.
    
    If you have any ideas or suggestions regarding the latter,mail me.
    (Email: gagangulyanig@gmail.com)

### Reference
	1. beautifulsoup, html5lib: module object has no attribute _base
	https://stackoverflow.com/questions/38447738/beautifulsoup-html5lib-module-object-has-no-attribute-base

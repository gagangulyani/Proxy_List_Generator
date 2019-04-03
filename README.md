# Proxy List Generator
##### Scraps proxylist and gives a list of proxies along with port numbers..

## Highly Recommended for:
    1. Web Scrapers
    2. Web Crawlers
    3. Pen Testers
    4. People who want list of proxies in Bulk

## How it Works?
	It scraps [free-proxy-list.net] and extracts all the IPs and Port Numbers...
	
## modules used:
	1. requests is being used for getting html content 
	2. BeautifulSoup is being used for extracting the content

## Usage
    Just import proxy_get in your code and call the function Proxy_List() for list of proxies

#### On Success:
    Returns List of proxies
    example:
      [["192.168.1.1":"8080"],["localhost","8080"]]
    
#### On Failure:
    Returns None
    
### Important:

    feel free to tweak it as much as you like.
    
    If you have any ideas or suggestions regarding the latter,mail me.
    (Email: gagangulyanig@gmail.com)

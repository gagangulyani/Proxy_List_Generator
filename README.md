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
    Just import proxy_get in your code and call the Proxy_List() function

#### On Success:
    Output will be displayed only is script is executed directly (without importing it)
    If Imported and Proxy_List() is called:
        Returns dictionary containing list of proxies and number of proxies retrieved
        example:
        {
            "list_of_proxies":[
                    {
                        'ip_address': '118.174.196.112',
                        'port': '36314',
                        'code': 'TH',
                        'country': 'Thailand',
                        'anonymity': 'elite proxy',
                        'google': 'no',
                        'https': 'yes',
                        'last_checked': '29 seconds ago'
                    },
                    {
                        'ip_address': '84.201.158.146',
                        'port': '3128',
                        'code': 'RU',
                        'country': 'Russian Federation',
                        'anonymity': 'elite proxy',
                        'google': 'no',
                        'https': 'yes',
                        'last_checked': '29 seconds ago'}] 
                    }
                    ...
                ],
            "count" : 2
        }    
    
#### On Failure:
##### 1. In case of failure of retrieval of Proxy List from free-proxy-list.net
    Output:
        Failed to get Proxy List :(
    Return:
        None
##### 2. In case of failure Bad Request or Redirection of free-proxy-list.net
    Output:
        Something Went Wrong while Getting Proxy List!
    Return:
        None

### Important:

    feel free to tweak it as much as you like.
    
    If you have any ideas or suggestions regarding the latter,mail me.
    (Email: gagangulyanig@gmail.com)

### Reference
	1. beautifulsoup, html5lib: module object has no attribute _base
	https://stackoverflow.com/questions/38447738/beautifulsoup-html5lib-module-object-has-no-attribute-base

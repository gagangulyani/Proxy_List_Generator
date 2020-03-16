# Proxy List Generator
### a simple python script which scraps free-proxy-list.net for proxies..

## Highly Recommended for:
    1. Web Scrapers
    2. Web Crawlers
    3. Pen Testers
    4. People who want list of proxies in Bulk

## How it Works?
	It scraps [free-proxy-list.net] and extracts all the IP Addresses, Port Numbers,Country Codes etc, which are available on the home page accessible via pagination.
	
## requirements:
	1. requests
	2. BeautifulSoup
	3. html5lib
	
## Preparing for running the Script
### run the following commands before executing the script
#### for installing requirements for running the script
	git clone https://github.com/gagangulyani/Proxy_List_Generator.git
	cd Proxy_List_Generator
	pip install -r requirements.txt
	
#### In case of the following error:
	AttributeError: module 'html5lib.treebuilders' has no attribute '_base'

#### run the following command 
	pip install --upgrade beautifulsoup4
	pip install --upgrade html5lib

## Running the Script [Option #1]
+ *Copy Paste* or *Move* **proxy_get.py** file in Current Working Directory of your project
+ Import `proxy_get` in your code: `from proxy_get import Proxy_List()` 
+ Call the `Proxy_List()` function
    
## Running the Script [Option #2]
	python proxy_get.py
  

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
            "count" : 300
        }    
    
#### On Failure:
##### 1. In case of failure of retrieval of Proxy List from free-proxy-list.net
	Output:
		Failed to get Proxy List :(
		Try Running the script again..
		
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

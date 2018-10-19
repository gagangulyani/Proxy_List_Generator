# Proxy List Retriever
## This module will get us list of proxies and port numbers 
### very useful for web scrapers and crawlers


## How it Works?
	
	It scraps free-proxy-list.net and extracts all the ips and port numbers in respect to their IPs..

	If Success:
		Returns List of proxies
		(example:[["192.168.1.1":"8080"],["localhost","8080"]])
	Else:
		Returns None
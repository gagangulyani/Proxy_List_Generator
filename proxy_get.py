"""
This script scraps "https://free-proxy-list.net/" and returns
list of proxies along with their port numbers,
"""

try:
	import requests
	# for getting html of free-proxy-list.net
except ImportError:
	print("\n\"requests\" is required for getting proxy list")
try:
	from bs4 import BeautifulSoup as bs
	# for scrapping list from html
except ImportError:
	print("\n\"bs4\" is required for getting proxy list")

def Proxy_List():
    """
    This function returns list of proxies abd returns None
    in case of failure.
    """

    url="https://free-proxy-list.net/"
    # site which will get us list of proxies..

    try:
        page=requests.get(url)
        # getting html content of site..
    except :
        print ("\nFailed to get Proxy List :(")
        # returns None if unable to get the html of the page
        return None

    if page.status_code!=200:
        print ("\nSomething Went Wrong while Getting Proxy List!\n")
    
    soup = bs(page.text,'html.parser') #creating soup object 
    c=1 # for skipping few irrelevant stuff
    proxies=[] #the list which will be returned
    
    l=[]
    
    for i in soup.find_all('tr'):
        for j in i:
            if j.name=="td" and ("." in j.text or j.text.isdigit()): # the secret sauce of finding ips
                #print (j.text)
                l.append(j.text)
                if c%2==0:
                    proxies.append(l)
                    l=[]
                c+=1
    
    return proxies


if __name__=='__main__':
    print(Proxy_List())

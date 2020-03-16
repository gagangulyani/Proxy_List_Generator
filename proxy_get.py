"""
This script scraps "https://free-proxy-list.net/" and returns
dictionary containing of proxies along with their port numbers,
"""

try:
    import requests
    from bs4 import BeautifulSoup as bs
except ImportError:
    exit()


def p_format(*args):
    ip_address, port, code, country, anonymity, google, https, last_checked = args
    
    return {
        "ip_address": ip_address,
        "port": port,
        "code": code,
        "country": country,
        "anonymity": anonymity,
        "google": google,
        "https": https,
        "last_checked": last_checked
    }


def Proxy_List():
    """
    This function returns list of proxies and returns None
    in case of failure.
    """

    # url of site containing proxies
    url = "https://free-proxy-list.net/"
    NUMBER_OF_ATTRIBUTES = 8
    try:
        # getting html content of site..
        page = requests.get(url)

    except:
        # returns None if unable to get source code of site
        print("\nFailed to get Proxy List :(\nTry Running the script again..")
        return None

    if page.status_code != 200:
        print("\nSomething Went Wrong while Getting Proxy List!\n")
        return None

    soup = bs(page.text, 'html.parser')  # creating soup object
    proxies = []  # final list of dictionaries each containing proxy info

    table = soup.find('table')
    tbody = table.tbody if table else None  # contains rows of IPs and Stuff

    if tbody:
        infos = tbody.find_all('tr')
        for info in infos:
            # each info is a tr from tbody of table
            # extracting info from table rows
            proxy_data_temp = [i.text for i in info]
            if len(proxy_data_temp) == NUMBER_OF_ATTRIBUTES:
                # after all attributes have been retrieved
                # from a row, it's time to format it properly.
                proxies.append(p_format(*proxy_data_temp))

        return {"list_of_proxies": proxies,
                "count": len(proxies)}


if __name__ == '__main__':
    result = Proxy_List()
    if result:
        print(result)

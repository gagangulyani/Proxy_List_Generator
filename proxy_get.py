"""
This script scraps "https://free-proxy-list.net/" and returns
list of proxies along with their port numbers,
"""

try:
    import requests
    from bs4 import BeautifulSoup as bs
except ImportError:
    exit()


def p_format(ip_address, port, code, country,
             anonymity, google, https, last_checked):
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
    This function returns list of proxies abd returns None
    in case of failure.
    """

    # url of site containing proxies
    url = "https://free-proxy-list.net/"

    try:
        # getting html content of site..
        page = requests.get(url)

    except:
        # returns None if unable to get source code of site
        print("\nFailed to get Proxy List :(")
        return None

    if page.status_code != 200:
        print("\nSomething Went Wrong while Getting Proxy List!\n")
        return None

    soup = bs(page.text, 'html.parser')  # creating soup object
    proxies = []  # final list of dictionaries each containing proxy info

    table = soup.find('table')
    tbody = None  # cpntains rows of IPs and Stuff

    if table:
        tbody = table.tbody
        
    if tbody:
        infos = tbody.find_all('tr')
        for info in infos:
            # each info is a tr from tbody of table
            # extracting info from table rows
            proxy_data_temp = [i.text for i in info]
            if len(proxy_data_temp) == 8:
                # after all attributes have been retrieved
                # from a row, it's time to format it properly.
                proxies.append(p_format(ip_address=proxy_data_temp[0],
                                        port=proxy_data_temp[1],
                                        code=proxy_data_temp[2],
                                        country=proxy_data_temp[3],
                                        anonymity=proxy_data_temp[4],
                                        google=proxy_data_temp[5],
                                        https=proxy_data_temp[6],
                                        last_checked=proxy_data_temp[7]))
    
        return {"list_of_proxies": proxies,
                "count": len(proxies)}


if __name__ == '__main__':
    result = Proxy_List()
    if result:
        print(result)

from bs4 import BeautifulSoup
import urllib
import ssl

# Ignore SSL certificate errors
# code obtained from py4e.com/html3/12-network
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Get site html
url = 'https://platform6.fi/members'
url_handle = urllib.request.urlopen(url, context = ctx)
site_html = BeautifulSoup(url_handle,'html.parser')

# Scrap content
startup_lists = site_html.find_all(attrs = {'class':'fp-title'})
for startup in startup_lists:
    name = startup.get_text().strip()
    print(name)

    # href = startup.a.get('href',None)
    # print(f'{name}: {href}')

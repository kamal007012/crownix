from urllib.request import urlopen, urlparse
from bs4 import BeautifulSoup
import lxml, os
from modules import helper
#import win_unicode_console , colorama


try:
    pages = set()
    url = input("\t\t\tExample :- mvec.com (or) http://mvec.com/\n\n\n[*] Enter the URL >> ")
    #print('%s_'%(W) * width)

    def getLinks(pageUrl):
        global pages
        clean = helper.clean(url)
        domain = helper.get_domain(clean)
        html = urlopen(clean)
        bsObj = BeautifulSoup(html, "lxml")
        for link in bsObj.findAll("a"):
            if 'href' in link.attrs:
                if link.attrs['href'] not in pages:
                #We have encountered a new page
                    newPage = link.attrs['href']
                    if helper.valid(newPage, domain):
                        pages.add(newPage)
                        print(">> ", newPage)


                        getLinks(newPage)

    getLinks("")

except Exception as e:
    print("[-] Something gonna wrong! Please Restart the application.")

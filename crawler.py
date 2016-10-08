# import the urlopen function from the urllib2 module
from urllib2 import urlopen
from urlparse import urljoin
# import the BeautifulSoup function from the bs4 module
from bs4 import BeautifulSoup
# import pprint to print things out in a pretty way
import pprint
# choose the url to crawl

url = 'http://www.codingdojo.com'
# get the result back with the BeautifulSoup crawler

 # print soup to see the result!!
# your code here to find all the links from the result
# and complete the challenges below




def link_list(list):
    soup = BeautifulSoup(urlopen(url),'html.parser')
    uniq_links=[]
    for link in soup.find_all('a'):
        link_match=link.get('href')
        if (link_match[0]=='#' or link_match=='javascript:void(0);'):
            continue
        elif link_match[0]=='/':
            abs_url=urljoin(url,link_match)
            uniq_links.append(str(abs_url))
    # pprint.pprint(uniq_links)
        else:
            uniq_links.append(str(link_match))
    # pprint.pprint(uniq_links)
    # print type(uniq_links)
    return uniq_links
    # print len(uniq_links)
# print link_list(url)

#
#
def link_occurrences(link_list):
    link_dict={}
    for i in range(len(link_list)):
        if link_list[i] not in link_dict:
            link_dict[link_list[i]]=1
        else:
            link_dict[link_list[i]]+=1
    return link_dict

pprint.pprint(link_occurrences(link_list(url)))

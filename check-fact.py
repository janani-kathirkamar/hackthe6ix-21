
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://www.y8.com/"

scam_counter = 0
def check_trustworthy(url):
    shortened_url = url.replace("https://","")
    shortened_url = shortened_url.replace("/","")
    report_site = "https://transparencyreport.google.com/safe-browsing/search?hl=en"
    modified_report_site = "https://transparencyreport.google.com/safe-browsing/search?url=https:%2F%2F"+shortened_url+"%2F&hl=en"
    
    page = urlopen(modified_report_site)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    figure = soup.find_all(name = 'span')

check_trustworthy(url)  

def check_age(url):
    #paste url into WhoisLookup
    if age_site < 2:
        scam_counter += 1

def check_spelling(url):
    #parse url into three parts [subdomain, domain, domain extension]
    #check each part in a database of sketchiness
    if sketchiness == True:
        scam_counter += 1

#main function
def check_scam(url):
    check_trustworthy(url)
    check_age(url)
    check_spelling(url)

    return scam_counter 


'''

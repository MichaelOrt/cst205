# -*- coding: utf-8 -*-
import scrapy
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
import pandas as pd
import re
import os
from urllib.parse import urlparse
import logging

class MailSpider(scrapy.Spider):
    
    name = 'email'

    def __init__(self, *args, **kwargs):
        logging.getLogger('scrapy').setLevel(logging.INFO)
        super().__init__(*args, **kwargs)
    
    def parse(self, response):
        
        links = LxmlLinkExtractor(allow=(),deny=self.reject).extract_links(response)
        links = [str(link.url) for link in links]
        links.append(str(response.url))
        
        for link in links:
            yield scrapy.Request(url=link, callback=self.parse_link) 
            
    def parse_link(self, response):
        
        for word in self.reject:
            if word in str(response.url):
                return
            
        html_text = str(response.text)
        mail_list = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", html_text)
        parsed_uri = urlparse(response.url)
        domain = '{uri.netloc}'.format(uri=parsed_uri)
        domain = domain.replace("www.", "")

        dic = {
                'domain': domain, 
                'email': mail_list, 
                'link': str(response.url)
            }
        df = pd.DataFrame(dic)
        
        df.to_csv(self.savefile, mode='a', header=False)
        df.to_csv(self.savefile, mode='a', header=False)

def ask_user(question):
    response = input(question + ' y/n' + '\n')
    if response == 'y':
        return True
    else:
        return False

def create_file(savefile):
    response = False
    if os.path.exists(savefile):
        response = ask_user('File already exists, replace?')
        if response == False: return 
    
    with open(savefile, 'wb') as file: 
        file.close()

def get_info(urlfile, savefile, reject=[]):

    url_list = []
    if os.path.exists(urlfile):
        with open(urlfile) as file:
            url_list = file.read().splitlines()
    else:
        print('No url file '+ urlfile + 'found.')

    #print("Full list:\n",url_list)

    create_file(savefile)
    df = pd.DataFrame(columns=['domain', 'email', 'link'], index=[0])
    df.to_csv(savefile, mode='w', header=True)
    
    print('Searching for emails...')
    process = CrawlerProcess({'USER_AGENT': 'Mozilla/5.0'})
    process.crawl(MailSpider, start_urls=url_list, savefile=savefile, reject=reject)
    process.start()
    
    print('Cleaning emails...')
    df = pd.read_csv(savefile, index_col=0)
    df.columns = ['domains', 'email', 'link']
    df = df.drop_duplicates(subset='email')
    df = df.reset_index(drop=True)
    df.to_csv(savefile, mode='w', header=True, index=False)
    
    return df

bad_words = ['facebook', 'instagram', 'youtube', 'twitter', 'wiki']
df = get_info('urllist.txt', 'mailcrawl.csv', reject=bad_words)
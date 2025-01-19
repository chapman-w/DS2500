#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 13:37:48 2024

@author: wesleychapman
Lab 5
"""

import requests
from bs4 import BeautifulSoup
from textblob import TextBlob


def construct_links(url):
    
    info = requests.get(url)
    soup = BeautifulSoup(info.text, 'html.parser')
    
    url_info = []
    for tag in soup.find_all('a', href=True):
        link = tag['href']
        label = tag.get_text(strip=True)
        url_info.append((link, label))
    return url_info


def count_missing_alt(url):
     
    info = requests.get(url)
    soup = BeautifulSoup(info.text, 'html.parser')
    
    images = soup.find_all('img')
    total_images = len(images)
    
    missing_alt_count = sum(1 for img in images if 'alt' not in img.attrs)
    
    return missing_alt_count/total_images
    

def paragraph_polarity(url, div_class):
    
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    target_div = soup.find('div', class_=div_class)
    if target_div:
           paragraph = target_div.find('p')
           if paragraph:
               post_text = paragraph.get_text(strip=True)
               
               # Calculate polarity
               polarity_score = TextBlob(post_text).sentiment.polarity
               return polarity_score
    
    
    
    

def main():

   url = "http://example.com"
   links = construct_links(url)
   print(links)
   
   new_url = "https://jonathanchapman.com/photography/"
   print(count_missing_alt(new_url))
   
   url = "https://www.reddit.com/r/NEU/comments/15q56w7/transferring_to_neu_computer_science_without/"
   div_class = "mb-sm mb-xs px-md xs:px-0"
   print(paragraph_polarity(url, div_class))
    
    
    
if __name__ == "__main__":
    main()    
    
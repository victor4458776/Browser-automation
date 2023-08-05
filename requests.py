from pathlib import Path

import scrapy
#import scrapy
#import spider

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")

#[s] Available Scrapy objects:
#[s]   scrapy     scrapy module (contains scrapy.Request, scrapy.Selector, etc)
#[s]   crawler    <scrapy.crawler.Crawler object at 0x7d8b1d728190>
#[s]   item       {}
#[s]   request    <GET https://quotes.toscrape.com/page/1/>
#[s]   response   <200 https://quotes.toscrape.com/page/1/>
#[s]   settings   <scrapy.settings.Settings object at 0x7d8b1d728670>
#[s]   spider     <DefaultSpider 'default' at 0x7d8b1d1caa60>
#[s] Useful shortcuts:
#[s]   fetch(url[, redirect=True]) Fetch URL and update local objects (by default, redirects are followed)
#[s]   fetch(req)                  Fetch a scrapy.Request and update local objects 
#[s]   shelp()           Shell help (print this help)
#[s]   view(response)    View response in a browser
#>>> response.css("title")
#[<Selector query='descendant-or-self::title' data='<title>Quotes to Scrape</title>'>]
#>>> response.css("title::text").getall()
#['Quotes to Scrape']
#>>> response.xpath("//title/text()").get()
#'Quotes to Scrape'
#********************************************************* 

import requests

if __name__ == "__main__":
    response = requests.get("http://www.google.com")
    for header in response.headers.keys():
        print (header  + ":" + response.headers[header])

# -*- encoding: utf-8 -*-

import requests, json

print ("Requests Library tests.")
responseGet = requests.get("http://www.google.es")

print (responseGet.text.encode('utf-8'))

print (responseGet.json)

print (responseGet.encoding)

print (responseGet.content)

print ("Status code: "+str(responseGet.status_code))

print ("Headers response: ")
for header, value in responseGet.headers.items():
  print(header, '-->', value)
#RESULTS
#>>> import requests
>>> if __name__ == "__main__":
...     response = requests.get("http://www.google.com")
...     for header in response.headers.keys():
...         print (header  + ":" + response.headers[header])
... 
#Date:Sat, 05 Aug 2023 22:08:20 GMT
#Expires:-1
#Cache-Control:private, max-age=0
#Content-Type:text/html; charset=ISO-8859-1
#Content-Security-Policy-Report-Only:object-src 'none';base-uri 'self';script-src 'nonce-TWoPy0YNsrXY9JSw_0KULg' 'strict-dynamic' 'report-sample' 'unsafe-eval' 'unsafe-inline' https: http:;report-uri https://csp.withgoogle.com/csp/gws/other-hp
#Content-Encoding:gzip
#Server:gws
#Content-Length:8404
#X-XSS-Protection:0
#X-Frame-Options:SAMEORIGIN
#Set-Cookie:AEC=Ad49MVHVkiKB_AWlUfQTh71FC_RVYiFv5ALiyyiMv3hDQk1UzqJyIr5r9Jg; expires=Thu, 01-Feb-2024 22:08:20 GMT; path=/; domain=.google.com; Secure; HttpOnly; SameSite=lax

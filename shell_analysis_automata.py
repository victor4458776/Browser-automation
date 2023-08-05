2023-08-06 00:01:10 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2023-08-06 00:01:10 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2023-08-06 00:01:10 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2023-08-06 00:01:10 [scrapy.core.engine] INFO: Spider opened
2023-08-06 00:01:11 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://robocorp.com/portal/robot/robocorp/template-python-workitems> (referer: None)
[s] Available Scrapy objects:
[s]   scrapy     scrapy module (contains scrapy.Request, scrapy.Selector, etc)
[s]   crawler    <scrapy.crawler.Crawler object at 0x7ae8058f8250>
[s]   item       {}
[s]   request    <GET https://robocorp.com/portal/robot/robocorp/template-python-workitems>
[s]   response   <200 https://robocorp.com/portal/robot/robocorp/template-python-workitems>
[s]   settings   <scrapy.settings.Settings object at 0x7ae8058f8820>
[s]   spider     <DefaultSpider 'default' at 0x7ae805399820>
[s] Useful shortcuts:
[s]   fetch(url[, redirect=True]) Fetch URL and update local objects (by default, redirects are followed)
[s]   fetch(req)                  Fetch a scrapy.Request and update local objects 
[s]   shelp()           Shell help (print this help)
[s]   view(response)    View response in a browser
>>> scrapy
<module 'scrapy' from '/home/victoralonsogarcia8/.local/lib/python3.9/site-packages/scrapy/__init__.py'>
>>> request
<GET https://robocorp.com/portal/robot/robocorp/template-python-workitems>
>>> spider
<DefaultSpider 'default' at 0x7ae805399820>
>>> view(response)
True
>>> for quote in response.css("div.quote"):
...     text = quote.css("span.text::text").get()
...     author = quote.css("small.author::text").get()
...     tags = quote.css("div.tags a.tag::text").getall()
...     print(dict(text=text, author=author, tags=tags))
... 
>>> print(quote)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'quote' is not defined
>>> print(response)
<200 https://robocorp.com/portal/robot/robocorp/template-python-workitems>
>>> 

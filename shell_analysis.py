# Automate function-extraction methods
>>> import re
>>> import mechanize
>>> browser = mechanize.Browser()
>>> print(browser)
<Browser (not visiting a URL)>
>>> browser.open("https://docs.scrapy.org/en/latest/intro/tutorial.html")
# THE FUNCTION IS ALIVE? Y/N, then the browser responses as an byte-object          
<response_seek_wrapper at 0x79e4fe83d790 whose wrapped object = <closeable_response at 0x79e4fe59f610 whose fp = <_io.BufferedReader name=3>>>
response = browser.follow_link(text_regex=r"cheese\s*shop", nr=1)
# LINKS  self._factory.links(), text, text_regex, name, name_regex, url
print(response1.info())  # headers
print(response1.read())  # body

>>> response1 = browser.submit
>>> response1 = browser.submit()
# request = self.form.click(*args, **kwds) 
# AttributeError: 'NoneType' object has no attribute 'click'
>>> print(browser.form)
None
>>> browser = mechanize.Browser()
>>> print(browser)
<Browser (not visiting a URL)>
# Add HTTP Basic/Digest auth username and password for HTTP proxy access.
# (equivalent to using "joe:password@..." form above)
>>> browser.set_proxies({"http": "joe:password@myproxy.example.com:3128",
...                 "ftp": "proxy.example.com",
...                 })
>>> print(browser)
<Browser (not visiting a URL)>
>>> browser.add_proxy_password("joe", "pass123")
>>> browser.finalize_request_headers = lambda request, headers: headers.__setitem__(
...   'My-Custom-Header', 'Something')
>>> # Don't handle HTTP-EQUIV headers (HTTP headers embedded in HTML).   
          

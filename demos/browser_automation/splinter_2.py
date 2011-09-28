#!/usr/bin/env python

"""
splinter

http://splinter.cobrateam.info
"""

from time import sleep
from splinter.browser import Browser


#url = 'http://simile.mit.edu/crowbar/test.html'
#url = 'http://dl.dropbox.com/u/144888/hello_js.html'
#url = 'http://www.ncbi.nlm.nih.gov/nuccore/CP002059.1'
#url = 'http://translate.google.com/#en|fr|game'
url = 'https://dl.dropbox.com/u/144888/email_js.html'

def main():
    #browser = Browser('zope.testbrowser')
    #browser = Browser('webdriver.chrome')
    browser = Browser()
    browser.process(url)
    
    #browser.execute_script("var win = window.open(); win.document.write('<html><head><title>Generated HTML of  ' + location.href + '</title></head><pre>' + document.documentElement.innerHTML.replace(/&/g, '&amp;').replace(/</g, '&lt;') + '</pre></html>'); win.document.close(); void 0;")
    
    #sleep(20)
    
    f = open("source.html", "w")
    print >>f, browser.html
    f.close()
    
    browser.quit()

#############################################################################

if __name__ == "__main__":
    main()
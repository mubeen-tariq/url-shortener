# Simple URL Shortener
# Used Python's library "pyshorteners"


import pyshorteners

print("---URL Shortener---")
url = input('Enter the url: ')


def shortenurl(url):
    s = pyshorteners.Shortener()
    print('Shortened URL is: ', s.tinyurl.short(url))


shortenurl(url)

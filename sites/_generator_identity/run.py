# -*- coding: utf-8 -*-

"""GetEnvFromURL.
Install requirements: pip3 install beautifulsoup4 docopt
Usage:
  run.py    (--url=<URL>)
            (--out-file=<FILE>)
"""


from docopt import docopt
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

USER_AGENT = ('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')


arguments = docopt(__doc__, version='GetEnvFromURL')

URL = arguments['--url'] or 'http://pascalandy.com/blog/landingpage_data_v2/'
FILE_NAME = arguments['--out-file'] or 'env'

def get_html(url):
    q = Request(url)
    q.add_header(*USER_AGENT)
    return urlopen(q).read()


def quote_val(a):
    return a[0], "'%s'" % a[1].translate(str.maketrans({"'":  r"\'"})).encode("ascii", "xmlcharrefreplace").decode()


soup = BeautifulSoup(get_html(URL))

try:
    code = soup.find("section", class_="post-content").code.string
except AttributeError as e:
    pass
else:
    with open(FILE_NAME, 'w') as fn:
        for line in code.rstrip('\n ').split('\n'):
            print('='.join(quote_val(line.strip().split('=', maxsplit=1))), file=fn)


#!/usr/bin/env python

import progressbar
import requests
import urlparse
from bs4 import BeautifulSoup
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('sites.ini')
requests.packages.urllib3.disable_warnings()

for site in parser.sections():
    print "Checking %s..." % site
    url = parser.get(site, 'url')
    user = parser.get(site, 'user')
    password = parser.get(site, 'pass')

    # Get all packages from /simple and
    # 'get' them to force update check
    r = requests.get(url, auth=(user, password), verify=False)
    soup = BeautifulSoup(r.text)
    pkg_urls = []
    for link in soup.find_all('a', href=True):
        pkg_urls.append(urlparse.urljoin(url, link['href']))

    num_packages = len(pkg_urls)

    bar = progressbar.ProgressBar(maxval=num_packages, \
            widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])

    print "Found %d packages, updating now..." % len(pkg_urls)
    count = 0
    for pkg in pkg_urls:
        pkg_request = requests.get(pkg, auth=(user, password), verify=False)
        count += 1
        bar.update(count)

    bar.finish()
    print

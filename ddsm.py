#!/usr/bin/env python2
# coding: utf-8

import re
import os
import urllib
import urllib2

def get_html(url):
    print 'Downloading: %s' % url
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    html = response.read()
    return html

def get_image(url, filename):
    print 'Downloading images: %s' % url
    urllib.urlretrieve(url, './images/%s' % filename)

def get_url():
    surl = 'http://marathon.csee.usf.edu/Mammography/Database.html'
    html = get_html(surl)
    for i in re.compile('([^"]+)">thumbnails</a>').findall(html):
        if '/normals/normal_' in i:
            continue
        ihtml = get_html(i) if i else ''
        m = re.compile(r'^(.+/)[^/]+$').search(i)
        src1 = m.groups()[0]
        for j in re.compile('<A\sHREF="(case[^"]+)').findall(ihtml):
            jhtml = get_html(src1 +j)
            m = re.compile(r'^(.+/)[^/]+$').search(src1 +j)
            src2 = m.groups()[0]
            for k in re.compile('IMG\sSRC="([^"]+)"', re.IGNORECASE).findall(jhtml):
                if k:
                    image_url = src2 + k
                    filename = image_url.replace('http://marathon.csee.usf.edu/Mammography/DDSM/thumbnails/', '')
                    f_dir = re.compile('^(.+)/([^/]+)').search(filename)
                    if not os.path.exists('./images/%s' %f_dir.groups()[0]):
                        os.makedirs('./images/%s' % f_dir.groups()[0])
                    if not os.path.exists('./images/%s' % filename):
                        get_image(image_url, filename)

if __name__ == '__main__':
    if not os.path.exists('images'):
        os.mkdir('images')
    get_url()

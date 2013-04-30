#!/usr/bin/env python2
# coding: utf-8
# xdPay.py

import os
import sys
import time
import urllib
import urllib2
import requests
import sqlite3 as lite
from lxml import html
from optparse import OptionParser

BASE_URL = "http://ssqzfw.xidian.edu.cn"
MAIN_URL = "http://ssqzfw.xidian.edu.cn/modules/swyh/login.jsp"

FORM_URL = "/modules/swyh/servlet/login"
PAY_INFO_URL = "/modules/swyh/byll.jsp"

TMP_DIR = os.path.expanduser("/tmp/")
IMG_PATH = os.path.join(TMP_DIR, "img.jpg")


def make_data_and_cookies():
    """make the post data(including vcode) and get cookies"""

    vcode = ''
    while len(vcode) is not 4:
        r = requests.get(MAIN_URL)
        doc = html.document_fromstring(r.text)
        vcode_link = doc.cssselect('form img')[0].get('src')
        #print vcode_link
        vcv = doc.cssselect('input[name="vcv"]')[0].get('value')
        img_url = BASE_URL + vcode_link
        #print vcv
        img = requests.get(img_url)

        # write to the image file
        with open(IMG_PATH, 'w') as f:
            f.write(img.content)
        fh = open(IMG_PATH, 'rb')
        imgstring = fh.read()
        fh.close()
        data = {
              "picstring" : imgstring
            }
        re = requests.post("http://202.117.120.235/server.php", data=data)
        vcode = re.text

    data = {
            "account": USERNAME,
            "password": PASSWORD,
            "vcode": vcode,
            "vcv": vcv
            }
    return data, r.cookies


def submit_form(data, cookies):
    """submit the login form so you're logined in"""
    form_action_url = BASE_URL + FORM_URL
    r = requests.post(form_action_url, data=data, cookies=cookies)

def get_info(cookies):
    """retrieve the data using the cookies"""
    info_url = BASE_URL + PAY_INFO_URL
    r = requests.get(info_url, cookies=cookies)
    doc = html.document_fromstring(r.text)
    used  = doc.cssselect('tr td')
    used_gb = float(used[4].text) / 1024
    rest_gb = float(used[6].text) / 1024
    return used_gb, rest_gb

if __name__ == '__main__':
    if not os.path.exists(TMP_DIR):
        os.mkdir(TMP_DIR)

    parser = OptionParser('%prog [-u <username>] [-p <password>] [-b]')
    parser.add_option('-u', '--username', dest='username', help='Name of account.')
    parser.add_option('-p', '--password', dest='password', help='Password of account.')
    parser.add_option('-b', '--batch', action='store_true', dest='batch', default=False, help='Whether batch or not, default false, NEED ACCOUT LIST FILE "account.list".')
    (options, args) = parser.parse_args()

    names = []
    passwds = []
    if options.batch:
        for i in open('account.list'):
            m = i.strip().split(' ')
            names.append(m[0])
            passwds.append(m[1])
    else:
        names.append(options.username)
        passwds.append(options.password)

    errTime = 0
    result = ''
    for indx in range(len(names)):
        USERNAME = names[indx]
        PASSWORD = passwds[indx]
        while errTime<4 :
            data, cookies = make_data_and_cookies()
            submit_form(data, cookies)
            time.sleep(1)
            try:
                result = get_info(cookies)
                break
            except:
                errTime += 1
                time.sleep(3)
        if result:
            print "\n账号：%s 流量使用情况：已使用 %.2fGB, 剩余 %.2f GB\n" % (USERNAME, result[0], result[1])
        else:
            print '\n查询出错：请检查您的账号和密码\n'

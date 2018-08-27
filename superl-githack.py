# -*- coding: utf-8 -*-
# Project = https://github.com/super-l/superl-githack.git
'''
    superl-githack
    Created by superl.                Nepenthes Security Team(忘忧草安全团队)
                                                                      00000
                                                                      00000
                                                                      00000
      00000000    00000  00000  00000000000     00000000    000000000 00000
     00000000000  00000  00000  000000000000   00000000000  000000000 00000
     00000  000   00000  00000  000000 00000  000000 00000  00000000  00000
     000000000    00000  00000  00000   0000  0000000000000 000000    00000
      0000000000  00000  00000  00000   00000 0000000000000 00000     00000
         0000000  00000  00000  00000   00000 00000         00000     00000
     00000  0000  000000000000  000000000000  000000000000  00000     00000
     00000000000  000000000000  000000000000   00000000000  00000     00000
      000000000   0000000000    00000000000     00000000    00000     00000
                                00000
                                00000                   Blog:www.superl.org
                                00000
'''
from __future__ import print_function
import sys
import re
import os
import urllib


try:
    import urllib2
except ImportError:
    import urllib.request


def getHtmlContent(target_url):
    send_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Connection': 'keep-alive'
    }

    if sys.version > '3':
        req = urllib.request.Request(target_url, headers=send_headers)
        response = urllib.request.urlopen(req, timeout=10)
    else:
        req = urllib2.Request(target_url, headers=send_headers)
        response = urllib2.urlopen(req, timeout=30)
    return response.read()


def getUrlList(htmlcontent):
    regex = r'<tr><td valign="top"><img src=".*?" alt="(?P<url>.*?)"></td><td><a href="(?P<dataurl>.*?)">(?P<title>.*?)</a>'
    content = re.compile(regex, re.S)
    find_result = content.findall(htmlcontent)
    return find_result


def save(url, savePath="git/"):
    content = getHtmlContent(url)
    find_result = getUrlList(content)
    # print(find_result)

    for i in range(len(find_result)):
        href_type = str(find_result[i][0])
        # print(href_type)

        if href_type == "[PARENTDIR]":
            continue
        elif href_type == "[DIR]":
            dir_link = str(find_result[i][1])
            dir_name = str(find_result[i][2])
            dir_href = url + dir_link

            print("发现目录：" + dir_href + "，遍历目录文件...")

            savePath = savePath + dir_name

            if not os.path.exists(savePath):
                os.mkdir(savePath)

            save(dir_href, savePath)

            savePath = savePath.replace(dir_name, "")

        else:
            file_href = url + str(find_result[i][1])
            file_name = str(find_result[i][2])
            print("发现文件，直接下载保存" + " 文件地址：" + file_href)

            savefile = savePath + find_result[i][1];

            if os.path.exists(savefile):
                print("该文件已经下载了！");
            else:
                urllib.urlretrieve(file_href, savefile);


if __name__ == "__main__":
    saveDir = "git"
    if not os.path.exists(saveDir):
        os.mkdir(saveDir)
    base_url = "http://www.superl.org/.git/"
    save(base_url)

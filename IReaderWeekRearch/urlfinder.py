# -*- coding: utf-8 -*-
import requests
import re


def parse(url, baseurl, type):
    r = requests.get(url)
    r.encoding = 'utf-8'
    #     print(r.encoding)
    content = r.text
    infoPattern = ''

    obtainbaiduyun(content, baseurl, type)

    nextPageRe = "[\s\S]+\<a\s*href=\"([.\w\/]+)\"\>下一页[\s\S]+"
    nextPageUrl = re.match(nextPageRe, content)
    if nextPageUrl:
        nextPage = nextPageUrl.group(1)
        parse(baseurl + nextPage, baseurl, type)
    else:
        print("last page")


def obtainbaiduyun(content, baseurl, type):
    start = content.find("<ul class=\"hanghang-list\">")
    end = content.find("<ol class=\"hanghang-page\">")
    newcontent = content[start:end]
    hrefPattern = "\<a href=\'([\w.\/]+)\'\>"
    m_tr = re.findall(hrefPattern, newcontent)
    with open(type + r"name.txt", 'a') as nameContent:
        with open("D:\pyc\ireadweek\error.txt", 'a') as errorContent:
            with open(type + r"map.txt", 'a') as mapContent:
                with open(type + r"url.txt", 'a') as urlContent:
                    for line in m_tr:
                        try:
                            bookurl = baseurl + line
                            r = requests.get(bookurl)
                            r.encoding = 'utf-8'
                            #     print(r.encoding)
                            bookcontent = r.text

                            # 过滤书名<title>故事思维 by 安妮特·西蒙斯
                            # mobi,epub,pdf,txt格式,Kindle电子书下载,mobi电子书下载-周读</title>
                            titleRe = "[\s\S]+<title>([\s\S]+?)by[\s\S]+<\/title>[\s\S]+"
                            titleMatch = re.match(titleRe, bookcontent)
                            if titleMatch:
                                title = titleMatch.group(1)
                                nameContent.write(title + "\n")

                            # 过滤百度云链接
                            start = bookcontent.find(
                                "<div class=\"hanghang-shu-content-btn\">")
                            end = bookcontent.find(
                                "<div class=\"hanghang-za-content\">")
                            booknewcontent = bookcontent[start:end]
                            baiduyun = "[\s\S]+\s+<a href=\"([\w:\/.]+)\"[\s\S]+"
                            baiduyunre = re.match(baiduyun, booknewcontent)
                            if baiduyunre:
                                url = baiduyunre.group(1)
                                urlContent.write(url + "\n")
                                mapContent.write(title + "    " + url + "\n")
                            else:
                                errorContent.write(title)
                        except Exception as ex:
                            print(line)


# 管理创业


#
# url = r"http://www.ireadweek.com/index.php/bookList/67.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\logic"
#
# url = r"http://www.ireadweek.com/index.php/bookList/66.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Finance"

###################
# url = r"http://www.ireadweek.com/index.php/bookList/65.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\fashion"

# url = r"http://www.ireadweek.com/index.php/bookList/64.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Joke"
#
# url = r"http://www.ireadweek.com/index.php/bookList/63.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Music"
#
# url = r"http://www.ireadweek.com/index.php/bookList/62.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Jade"
#
# url = r"http://www.ireadweek.com/index.php/bookList/61.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\tea"
#
# url = r"http://www.ireadweek.com/index.php/bookList/60.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\LearnEnglish"
#
##################
# url = r"http://www.ireadweek.com/index.php/bookList/59.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Jewellery"

##################
# url = r"http://www.ireadweek.com/index.php/bookList/58.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Medicine"

##################
# url = r"http://www.ireadweek.com/index.php/bookList/57.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Opera"

# url = r"http://www.ireadweek.com/index.php/bookList/55.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Law"

# url = r"http://www.ireadweek.com/index.php/bookList/54.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Photography"
#
##################
# url = r"http://www.ireadweek.com/index.php/bookList/53.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Bodybuilding"

##################
# url = r"http://www.ireadweek.com/index.php/bookList/52.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Food"

# url = r"http://www.ireadweek.com/index.php/bookList/51.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\SelfManagement"
#
# url = r"http://www.ireadweek.com/index.php/bookList/50.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Design"
#
##################
# url = r"http://www.ireadweek.com/index.php/bookList/49.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Family"

# url = r"http://www.ireadweek.com/index.php/bookList/48.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Literatureprize"

# url = r"http://www.ireadweek.com/index.php/bookList/47.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Read"

#
# url = r"http://www.ireadweek.com/index.php/bookList/46.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\speech"

##################
# url = r"http://www.ireadweek.com/index.php/bookList/45.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Youth"


# url = r"http://www.ireadweek.com/index.php/bookList/41.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Science"

##################
# url = r"http://www.ireadweek.com/index.php/bookList/42.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Film"

# url = r"http://www.ireadweek.com/index.php/bookList/43.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Tools"

# url = r"http://www.ireadweek.com/index.php/bookList/44.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Religion"

# url = r"http://www.ireadweek.com/index.php/bookList/37.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Poetry"

# url = r"http://www.ireadweek.com/index.php/bookList/39.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Classical"

# url = r"http://www.ireadweek.com/index.php/bookList/38.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\War"

# url = r"http://www.ireadweek.com/index.php/bookList/36.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Art"

# url = r"http://www.ireadweek.com/index.php/bookList/35.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\English"

# url = r"http://www.ireadweek.com/index.php/bookList/34.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Psychology2"

##################
# url = r"http://www.ireadweek.com/index.php/bookList/33.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\cartoon"

##################
# url = r"http://www.ireadweek.com/index.php/bookList/32.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Love"

# url = r"http://www.ireadweek.com/index.php/bookList/31.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\EconomicInvestment"

##################
# url = r"http://www.ireadweek.com/index.php/bookList/30.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Sale"

# url = r"http://www.ireadweek.com/index.php/bookList/29.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\SocialHuman"

##################
# url = r"http://www.ireadweek.com/index.php/bookList/28.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\life"

##################
# url = r"http://www.ireadweek.com/index.php/bookList/27.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\child"

# url = r"http://www.ireadweek.com/index.php/bookList/26.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Nobelprize"

# url = r"http://www.ireadweek.com/index.php/bookList/25.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\ForeignLiterature"

##################
# url = r"http://www.ireadweek.com/index.php/bookList/24.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\sport"

# url = r"http://www.ireadweek.com/index.php/bookList/23.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\ScienceTechnology"

##################
# url = r"http://www.ireadweek.com/index.php/bookList/22.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\workplace"

##################
# url = r"http://www.ireadweek.com/index.php/bookList/21.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Health"

# url = r"http://www.ireadweek.com/index.php/bookList/19.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Novel"

##################
# url = r"http://www.ireadweek.com/index.php/bookList/18.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\terror"

# url = r"http://www.ireadweek.com/index.php/bookList/17.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\autobiography"

##################
# url = r"http://www.ireadweek.com/index.php/bookList/16.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Sciencefiction"

# url = r"http://www.ireadweek.com/index.php/bookList/15.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Prose"

# url = r"http://www.ireadweek.com/index.php/bookList/14.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\history"

# url = r"http://www.ireadweek.com/index.php/bookList/13.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\ForeignNovels"

# url = r"http://www.ireadweek.com/index.php/bookList/12.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Psycholog"

# url = r"http://www.ireadweek.com/index.php/bookList/11.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\EntrepreneurshipManagement"

# url = r"http://www.ireadweek.com/index.php/bookList/10.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Philosophylife"

##################
# url = r"http://www.ireadweek.com/index.php/bookList/9.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\travels"

# url = r"http://www.ireadweek.com/index.php/bookList/6.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\literature"

# url = r"http://www.ireadweek.com/index.php/bookList/7.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Biography"

# url = r"http://www.ireadweek.com/index.php/bookList/8.html"
# baseurl = r"http://www.ireadweek.com"
# type = r"D:\pyc\ireadweek\Worldfamousbook"

##################
url = r"http://www.ireadweek.com/index.php/bookList/2.html"
baseurl = r"http://www.ireadweek.com"
type = r"D:\pyc\ireadweek\other"

parse(url, baseurl, type)

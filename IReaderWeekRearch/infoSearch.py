import requests
import sys
import io
import re
import json


def baiduyun(url):
    headers = {"Accept": r"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
               "Accept-Encoding": r"gzip, deflate, br",
               "Accept-Language": r"zh-CN,zh;q=0.9",
               "Connection": r"keep-alive",
               "Cache-Control": r"max-age=0",
               "Cookie": r"locale=zh; BAIDUID=DE4136E6678EFA9155CCC37D294A3072:FG=1; FP_UID=bfafc2a4ded214e2bbec403d33d6a562; PANWEB=1; BDUSS=k4wc3RyWjFnQXdQVkRiaVF3RFZIZmtySVp1S1hyTm5OTmFhdGhkSTF1T2FVWDFhQVFBQUFBJCQAAAAAAAAAAAEAAAA8yS8QvMXEr9DQ1d8zAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJrEVVqaxFVae; STOKEN=68ccad0c93d595ca63bf78369e5cfb73a06f3cfaf63c92cb5cecc2473c9722f7; SCRC=b314012c9d037125887c544f8a2938d9; BIDUPSID=DE4136E6678EFA9155CCC37D294A3072; PSTM=1515721702; cflag=15%3A3; BDCLND=v1Bz9hD%2FbRyyIGPB6M2CV1zvLyxJ0B8yrs8K2LR3ugE%3D; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1516099865,1516100011,1516100505,1516100738; Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0=1516100812; PANPSC=11268223909292048002%3Au4Z6slSSmflWwQE%2FPltX8On90oj%2BY%2FIs2NEnrqrLiyntefKbXAuoFe9mfuNV6kI1fmTzsKPDskPfpGYxbK7zcYwCNo%2BKa%2FTBpLrdV4FQ%2Fz%2BUjS3d4fIW%2BkNQsOYbdMWf3jGzPWbmHccDzLGxCF9yjchTKu%2BdwTb%2FOmicZ2coeUp%2BSJWX9%2F9F%2FBGwxPh3rTyLfX3EwneuEBOdmW%2Fext%2FoEg%3D%3D",
               "Host": r"pan.baidu.com",
               "Upgrade-Insecure-Requests": r"1",
               "User-Agent": r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
               }
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
#     print(r.encoding)
    content = r.text
#     print(content)
    infoPattern = '[\s\S]+\"app_id\"\:\"(\d+)\"[\s\S]+\"oper_id\"\:\"(\d+)\"[\s\S]+\"bdstoken\"\:\"(\w+)\"[\s\S]+\"shareid\"\:(\d+),[\s\S]+yunData.PATH\s+=\s+\"(\S+)\"[\s\S]+'
    matchObject = re.match(infoPattern, content)
    if matchObject:
        app_id = matchObject.group(1).strip()
        fromd = matchObject.group(2).strip()
        bdstoken = matchObject.group(3).strip()
        shareid = matchObject.group(4).strip()
        path = matchObject.group(5).strip()
        transfer(app_id, fromd, "fb4bfe204356a945e16783731632b930", shareid,
                 "MTUxNjE2MDY2NzY4MTAuMDU4MTE3MzE3mTk0MzQ2Mzo=", path)
    else:
        print("url")


def transfer(app_id, fromd, bdstoken, shareid, logid, path):
    url = r"https://pan.baidu.com/share/transfer?shareid=" + str(shareid) + "&from=" + str(fromd) + "&ondup=newcopy&async=1&bdstoken=" + str(
        bdstoken) + "&channel=chunlei&clienttype=0&web=1&app_id=" + str(app_id) + "&logid=" + str(logid)
    requestheaders = {"Accept": r"application/json, text/javascript, */*; q=0.01",
                      "Accept-Encoding": r"gzip, deflate, br",
                      "Accept-Language": r"zh-CN,zh;q=0.9",
                      "Connection": r"keep-alive",
                      "Content-Length": r"325",
                      "Content-Type": r"application/x-www-form-urlencoded; charset=UTF-8",
                      "Cache-Control": r"max-age=0",
                      "Cookie": r"BAIDUID=F12BC1EB2C8F5775B2844C017B0AC5AB:FG=1; PANWEB=1; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1516162062; cflag=15%3A3; FP_UID=32c676d60c11fc0dbdae7381d3068097; BDUSS=jlya2xoOWpLOUhINXBrMnZLeWNuSllDb2dJZWRMUnY0WWV1MWVvYWVwb1hXWVphQVFBQUFBJCQAAAAAAAAAAAEAAAA8yS8QvMXEr9DQ1d8zAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABfMXloXzF5ac; STOKEN=f4a72bc5787e76205b08c056412dcf4fe385312f2db40f056880e0eae8d6b1a6; SCRC=127becae833a968f0ae8f34051056ef9; Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0=1516162080",
                      "Host": r"pan.baidu.com",
                      "Origin": r"https://pan.baidu.com",
                      "Referer": r"https://pan.baidu.com/s/1nwYEOPV?errno=0&errmsg=Auth%20Login%20Sucess&&bduss=&ssnerror=0&traceid=",
                      "X-Requested-With": r"XMLHttpRequest",
                      "User-Agent": r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
                      }
    pathList = []
    pathList.append(path.replace("\\", ""))
    payload = {'filelist': pathList, 'path': "/ebook", }
    try:
        print(url)
        print(requestheaders)
        print(payload)
        r = requests.post(url, headers=requestheaders, data=payload)
        print(r.text)
    except Exception as e:
        print(e)


# http://blog.csdn.net/jim7424994/article/details/22675759
# sys.stdout = io.TextIOWrapper(
#     sys.stdout.buffer, encoding='utf8')
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
baiduyun(r"https://pan.baidu.com/s/1nwYEOPV")

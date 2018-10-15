import re

import requests

headers = {  # hdu用
    "Cookie": "",  # 改cookie
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}


class code:
    data = {
        'check': 0,
        'problemid': 1028,
        'language': 0,  # 语言  g++为0
        'usercode': ''  # 代码片段
    }

    queryData = {
        'first': '',
        'pid': 1028,
        'user': '',  # 改为用户名
        'lang': 1,
        'status': 5
    }

    def __init__(self, problemid, language, usercode):
        self.data['problemid'] = problemid
        self.data['language'] = language
        self.data['usercode'] = usercode

        self.queryData['pid'] = problemid
        self.queryData['lang'] = language

    def submitCode(self):
        url = 'http://acm.hdu.edu.cn/submit.php?action=submit'
        try:
            r = requests.post(url=url, data=self.data, headers=headers, timeout=5)
            if r.status_code != 200:
                print('submit code {}'.format(r.status_code))
            print('submit code (hdu{})'.format(self.data['problemid']))
            # print(r.text
            # print(r.status_code)
        except:
            print("submit error!!! ")

    def isAccepted(self):
        url = 'http://acm.hdu.edu.cn/status.php?'
        try:
            r = requests.get(url=url, params=self.queryData, headers=headers, timeout=5)
            pattern = r'Accepted'
            flag = len(re.findall(pattern, r.text))
            if flag >= 2:
                return True
            else:
                return False
        except:
            return None




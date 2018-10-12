import re
import requests

headers = {  # hdu用
    "Cookie": "PHPSESSID=m3m7v772n1jtpc7offh4qr4em6",  # 改cookie
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
        'user': '714508719@qq.com',
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
            r = requests.post(url=url, data=self.data, headers=headers)
            print('submit code+1')
            # print(r.text)
            # print(r.status_code)
        except:
            print('submit error!!!')

    def isAccepted(self):
        url = 'http://acm.hdu.edu.cn/status.php?'
        r = requests.get(url=url, params=self.queryData, headers=headers)
        pattern = r'Accepted'
        flag = len(re.findall(pattern, r.text))
        if flag >= 2:
            return True
        else:
            return False


scode = """#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <numeric>
#include <cstring>
#include <climits>
#include <cassert>
#include <complex>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <list>
#include <set>
#include <map>
using namespace std;

#pragma comment(linker, "/STACK:102400000,102400000")

typedef long long LL;
typedef double DB;
typedef unsigned uint;
typedef unsigned long long uLL;

/** Constant List .. **/ //{

const int MOD = int(1e9)+7;
const int INF = 0x3f3f3f3f;
const LL INFF = 0x3f3f3f3f3f3f3f3fLL;
const DB EPS = 1e-9;
const DB OO = 1e20;
const DB PI = acos(-1.0); //M_PI;
const int maxn = 121;

int c1[maxn] , c2[maxn];

void init()
{
    for(int i = 0 ; i < maxn ; i ++)
    {
        c1[i] = 1;
        c2[i] = 0;
    }
}

void solve()
{
    init();
    for(int i = 2; i < maxn ; i ++)
    {
        for(int j = 0 ; j < maxn ; j ++)
        {
            for(int k = 0 ; k + j < maxn ; k += i)
            {
                c2[j + k] += c1[j];
            }
        }
        for(int j = 0 ; j < maxn ; j ++)
        {
            c1[j] = c2[j];
            c2[j] = 0;
        }
    }
}

int main()
{
    #ifdef DoubleQ
    freopen("in.txt","r",stdin);
    #endif
    solve();
    int n;
    while(~scanf("%d",&amp;n))
    {
        printf("%d\n",c1[n]);
    }
}"""

if __name__ == '__main__':
    x = code(1001, 0, scode)
    # x.submitCode()
    # print(1)
    if x.isAccepted() == 'AC':
        print(1)
    else:
        print(0)



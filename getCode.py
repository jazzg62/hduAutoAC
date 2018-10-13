import re
import requests

headers = {  # csdn用
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}


def getCode(pid):  # 给出一个题目的id，获取其中的代码
    url = "https://so.csdn.net/so/search/s.do?q=hdu"
    code = ''
    list = getPageLink(url + str(pid))
    # print(list)
    for i in list:
        code = parserCodePage(i)
        yield code


def getPageLink(url):  # 输入一个搜索结果url，返回结果前10文章的url 列表
    # print(url)
    try:
        r = requests.get(url=url, headers=headers)
        pattern = r'<dd class="search-link"><a href="([\s\S]*?)"'
        return re.findall(pattern, r.text)
    except:
        getPageLink(url)


def parserCodePage(url):  # 给出一个博客文章的地址，返回该地址中的cpp代码段
    try:
        r = requests.get(url, headers=headers)
        pattern = r'<code class="language-cpp">([\s\S]*?)</code>'


        buf = re.findall(pattern, r.text)[-1]
        buf = buf.replace('&lt;', '<')
        buf = buf.replace('&gt;', '>')
        buf = buf.replace('&amp;', '&')
        if buf:
            return buf
    except:
        pass




def main():
    x = getCode(1028)
    print(type(x))
    for i in x:
        print(i)


if __name__ == '__main__':
    main()

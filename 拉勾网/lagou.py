import requests
from lxml import etree


def request_list_page():
    url = {
        'https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false&isSchoolJob=0'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/62.0.3202.94 Safari/537.36',
        'Referer': 'https://www.lagou.com/zhaopin/Python/?labelWords=label'
    }
    data = {
        'first': 'false',
        'pn': 2,
        'kd': 'python'
    }
    response = requests.post(url, headers=headers, data=data)

    print(response.json())


def main():
    request_list_page()


if __name__ == '__main__':
    main()




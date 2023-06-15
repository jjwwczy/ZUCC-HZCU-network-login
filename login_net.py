import requests
import time
import rc4
import json

def login():
    user="xxxxxx" #用户名
    pswd="xxxxxx" #密码
    url = "http://1.1.1.3/ac_portal/login.php"
    data={
    "opr": "pwdLogin",
    "userName": "",
    "pwd": "",
    "auth_tag": "",
    "rememberPwd": "1"
    }
    headers={
        # 'Accept':'*/*',
        # 'Accept-Encoding': 'gzip, deflate',
        # 'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'Connection': 'keep-alive',
        # 'Content-Length':'82',
        # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Host':'1.1.1.3',
        # 'Origin':'http://1.1.1.3',
        # 'Referer': 'http://1.1.1.3/ac_portal/20230318032256/pc.html?template=20230318032256&tabs=pwd-sms&vlanid=0&_ID_=0&switch_url=&url=http://1.1.1.3/homepage/index.html&controller_type=&mac=3c-54-47-89-e6-06',
        # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        # 'X-Requested-With': 'XMLHttpRequest',
            }
    now_date = str(int(round(time.time()*1000)))
    password=rc4.encrypt(now_date,pswd)
    data['userName']=user
    data['pwd']=password
    data['auth_tag']=now_date
    r=requests.post(url, data,headers=headers)
    r.encoding=r.apparent_encoding
    print(r.text)
    text_dict=json.loads(r.text)
    return text_dict['success']
if __name__ == '__main__':
    status=login()


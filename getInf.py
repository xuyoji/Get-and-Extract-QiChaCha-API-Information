#!/usr/bin/python
# pip install requests
import requests
import time
import hashlib
import json
 

def getInf(appkey, seckey, reqInterNme, company, linker):
    #  请求参数
    encode = 'utf-8'

    # Http请求头设置
    timespan = str(int(time.time()))
    token = appkey + timespan + seckey;
    hl = hashlib.md5()
    hl.update(token.encode(encoding=encode))
    token = hl.hexdigest().upper();
    #print('MD5加密后为 ：' + token)

    #设置请求Url-请自行设置Url
    #reqInterNme = "http://api.qichacha.com/ECIV4/Search"
    paramStr = linker+'='+ company
    url = reqInterNme + "?key=" + appkey + "&" + paramStr;
    headers={'Token': token,'Timespan':timespan}
    response = requests.get(url, headers=headers)

    resultJson = json.dumps(str(response.content, encoding = encode))
    # convert unicode to chinese
    resultJson = resultJson.encode(encode).decode("unicode-escape")
    return (response.status_code, resultJson)
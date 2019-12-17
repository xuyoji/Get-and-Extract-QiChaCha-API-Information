#copyright @ xuyj@shanghaitech.edu.cn
#2019.12.15
#python3 program

import requests
import time
import hashlib
import json
 

def getInf(appkey, seckey, reqInterNme, company, linker):
    encode = 'utf-8'

    timespan = str(int(time.time()))
    token = appkey + timespan + seckey
    hl = hashlib.md5()
    hl.update(token.encode(encoding=encode))
    token = hl.hexdigest().upper()

    paramStr = linker+'='+ company
    url = reqInterNme + "?key=" + appkey + "&" + paramStr
    headers={'Token': token,'Timespan':timespan}
    response = requests.get(url, headers=headers)

    return (response.status_code, str(response.content, encoding = encode))
#copyright @ xuyj@shanghaitech.edu.cn
#2019.12.14
#python3 program

import json, os
from getInf import *
from key import *

#EDIT YOUR API INFORMATION HERE
#Format in (URL, information name, keyword name)
#Add it to toGetList
gs = ('http://api.qichacha.com/ECIV4/GetDetailsByName', 'gs', 'keyword')
rz = ('http://api.qichacha.com/BusinessStateV4/SearchCompanyFinancings', 'rz', 'searchKey')
toGetList = (gs, rz)

for toGet in toGetList:
    if not os.path.exists(toGet[1]):
        os.makedirs(toGet[1])
    with open('companyList.csv', 'r') as f:
        companyList = [_.strip() for _ in f.readlines()]
    for company in companyList:
        flag, Inf = getInf(appkey, seckey, toGet[0], company, toGet[2])
        #print(Inf)
        with open('.//%s//'%toGet[1] + company + '.txt', 'w') as ff:
            ff.write(Inf)
        if int(flag) != 200:
            print(toGet[1], company, 'failed')
        else:
            print(toGet[1], company, 'succeed')
        time.sleep(0.1)

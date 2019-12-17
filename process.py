#copyright @ xuyj@shanghaitech.edu.cn
#2019.12.15
#python3 program

'''企业工商信息gs
成立日期：StartDate
所属地区（这里显示的是省份）: Area 下面的 Province 和 City
注册资本：RegistCapi
所属行业: Industry 下面的 Industry, IndustryCode, SubIndustry, SubIndustryCode
经营状态：Status (注意是不是查询成功与否的Status）
人数规模：PersonScope
登记机关（以确定行政上的所属地)：BelongOrg
企业地址（以确定经营商的所属地): Address'''
gsToDraw = ('Result', ('StartDate', ('Area', ('Province', 'City')), 'RegistCapi',
  ('Industry', ('Industry', 'IndustryCode', 'SubIndustry', 'SubIndustryCode')),
  'Status', 'PersonScope', 'BelongOrg', 'Address'), ('Company','StartDate', 'Province', 'City', 'RegistCapi',
  'Industry', 'IndustryCode', 'SubIndustry', 'SubIndustryCode',
  'Status', 'PersonScope', 'BelongOrg', 'Address'),'gs')

'''融资信息rz
产品名称：ProductName
融资事件发生的日期（融资日期）：Date
融资轮次：Round
融资金额：Amount （即使显示“金额未知”，也同样需要）
投资方：Investment'''
rzToDraw = ('Result', ('ProductName', 'Date', 'Round', 'Amount', 'Investment'), 
('Company', 'ProductName', 'Date', 'Round', 'Amount', 'Investment'),'rz')
toDrawList = (gsToDraw, rzToDraw)
#WRITE YOUR FORMAT HERE
#(result tag, (content to extract, nested tuple may be used to describe structure), (tag tuple), information name-should same with crawl.py) 

import json, csv, codecs
with open('companyList.csv', 'r') as f:
    companyList = [_.strip() for _ in f.readlines()]

for toDraw in toDrawList:
    with codecs.open('%s_result_test.csv'%toDraw[-1], 'w', 'utf_8_sig') as f:
        writer = csv.writer(f)
        tab = toDraw[-2]
        writer.writerow(tab)
        for company in companyList:
                with open('.//%s//'%toDraw[-1] + company + '.txt', 'r') as ff:
                    content = ff.readlines()
                    #content = (''.join(content)).strip('\"')
                    content = ''.join(content)
                    Inf = json.loads(content)
                    rst = toDraw[0]
                    infToDraw = [company]
                    if Inf["Status"] != '200':
                        writer.writerow(infToDraw)
                        continue
                    if toDraw[-1] == 'gs':
                        for item in toDraw[1]:
                            if type(item) == str:
                                if item not in Inf[rst]:
                                    Inf[rst][item] = '-'
                                infToDraw.append(Inf[rst][item])
                            elif type(item) == tuple:
                                if item[0] not in Inf[rst] or not(Inf[rst][item[0]]):
                                    Inf[rst][item[0]] = {}
                                for _ in item[1]:
                                    if _ not in Inf[rst][item[0]]:
                                        Inf[rst][item[0]][_] = '-'
                                    infToDraw.append(Inf[rst][item[0]][_])
                        writer.writerow(infToDraw)
                    elif toDraw[-1] == 'rz':
                        for _ in Inf[rst]:
                            infToDraw = [company]
                            for item in toDraw[1]:
                                if item not in _:
                                    _[item] = '-'
                                infToDraw.append(_[item])
                            writer.writerow(infToDraw)
                    #elif toDraw[-1] == WHAT YOU WANT
                        #Modify the former code to adapt to your own one HERE

print('Done!')





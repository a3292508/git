#!/usr/bin/python
#-*- coding:utf-8 -*-
#@Author：zhuxiujie

import requests

client_dict = {"李好":"17874512047",
               "李和":"17874512048",
               "李条":"17874512049",
               "李日":"17874512050",
               "李且":"17874512051",
               "李时":"17874512052",
               "李奖":"17874512053",
               "李将":"17874512054",
               "李啦":"17874512055",
               "李票":"17874512056",
               "李哦":"17874512057",
               "李不":"17874512058"
               }

url = 'http://sit3.haowu.com/partner-mobile-app/fill/filingfrom.do'
header = {"User-Agent":"Mozilla/5.0 (Linux; Android 9; MI 8 Build/PKQ1.180729.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3626.121 Mobile Safari/537.36 MicroMessenger/7.0.8.1540(0x27000834) Process/appbrand0 NetType/WIFI Language/zh_CN ABI/arm64",
          "Accept-Encoding":"gzip",
          "content-type":"application/x-www-form-urlencoded",
          "charset":"utf-8",
          "referer":"https://servicewechat.com/wx5faa076777cc0f7d/0/page-frame.html"}
for key in client_dict:
    data = {"clientIds[0].clientInfoId":"",
            "clientIds[0].isHidden":1,
            "clientIds[0].filingClientModuleList[0].moduleId":154,
            "clientIds[0].filingClientModuleList[0].moduleCode":"kehuxingming",
            "clientIds[0].filingClientModuleList[0].moduleContent":key,
            "clientIds[0].filingClientModuleList[1].moduleId":155,
            "clientIds[0].filingClientModuleList[1].moduleCode":"kehushouji",
            "clientIds[0].filingClientModuleList[1].moduleContent":client_dict[key],
            "key":"331145C61C8DB8763112A9F3AE461184",
            "os":"smallRoutine",
            "source":1,
            "appVersion":1,
            "houseIds":"111102427602819",       #111102427602818,111102427602819
            "longitude":"121.435818",
            "latitude":"31.345827"}
    res = requests.get(url,params=data,headers=header)
    try:
        print(res.json())
    except Exception as e:
        print("有数据错误！")
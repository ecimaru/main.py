import requests
import json

url ='http://apis.data.go.kr/1360000/WthrWrnInfoService/getWthrWrnMsg'
params ={'serviceKey' : 'DIK1aCltCAzi3FrQeQZunsWG/w+jQkCZRwGHm/IU9TbM8DKL9/zozuMSQh0mrOpT/QV59wQNqvwl24CJVF0eRw==',
         'pageNo' : '1', 'numOfRows' : '30',
         'dataType' : 'JSON', 'stnId' : '108', 'fromTmFc' : '20221201', 'toTmFc' : '20221205' }


response = requests.get(url, params=params)
result = response.json()




temp = result['response']['body']['items']['item']
tm_wthr = {}

for num in range(len(temp)):
    title = temp[num]['t1']
    time = temp[num]['t5']
    content = temp[num]['t4']
    sContent = temp[num]['t6']
    tsContent = temp[num]['t7']
    tm_wthr[temp[num]['tmFc']] = {'제목': title, '발효시각': time, '내용': content, '특보발효현황내용': sContent, '예비특보': tsContent}

with open('test.json','w') as f:
    json.dump(tm_wthr,f,ensure_ascii=False,indent=2)

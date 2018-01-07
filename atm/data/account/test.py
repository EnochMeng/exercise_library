import json
f=open('mlc.json','w')
data={
    'account_id':'mlc',
    'password':'123456',
    'enroll_time':'2018-01-06',
    'expire_time':'2020-01-06',
    'balance':150000
    }
data=json.dumps(data)
f.write(data)
f.close()

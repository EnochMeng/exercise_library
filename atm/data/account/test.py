import json
f=open('mlc.json','w')
data={'user_name':'mlc','user_password':'123456'}
data=json.dumps(data)
f.write(data)
f.close()

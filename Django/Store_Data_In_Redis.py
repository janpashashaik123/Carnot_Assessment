import pandas as pd
import redis
import json
    # redis connection
r = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

# open the first worksheed
df  = pd.read_csv('C:/Users/Janpasha/Downloads/raw_data (1).csv') 
df=df.sort_values('sts')
print(df)

# a   = df.set_index('device_fk_id').T.to_dict('dict')
a=df.set_index('device_fk_id').groupby('device_fk_id').apply(lambda x : x.to_numpy().tolist()).to_dict()
print("this is a, your excel list")
# print(a)
for key,value in a.items():
    # for value in list:
    # print(a[key]['latitude'])
    r.set(key,json.dumps(value))
    # r.rpush('myexceldata', str(value))
for key,val in a.items():
    b=json.loads(r.get(key))
    print(key)
    print(b)
# read all back to python
b = r.lrange('myexceldata', '0', '-1')

print("A1 becomes 0, B1 becomes 3 ...")
print(b[3])
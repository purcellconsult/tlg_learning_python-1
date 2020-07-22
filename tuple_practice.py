import time
#tuple_record  = ('etho', 'AA:BB:CC:DD:11:22', '192.168.0.1', '5060', 'UDP')

#print(tuple_record)
#rint(tuple_record * 2)

local_time = time.localtime(time.time())
print(local_time)
print(type(local_time))
print(local_time[0])
print(local_time[1])

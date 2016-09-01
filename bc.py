import bandicoot as bc
import pprint
u= bc.read_csv("sanjay", "C:\\Users\\Sahil\\Desktop")

rec = u.records
#other features that can be included - call duration... the people who are being called -- the number of times they have been called in total
t = []
c=0
#print(rec[1].datetime.timestamp())
for i in rec:
	#format i.datetime
	t.append(i.datetime.timestamp())
	c+=1

def grouper(iterable):
    prev = None
    group = []
    for item in iterable:
        if not prev or item - prev <= 1000:
            group.append(item)
        else:
            yield group
            group = [item]
        prev = item
    if group:
        yield group
		
di = dict(enumerate(grouper(t), 1))
	
newdi = [v for v in di.values() if len(v)>6]

print(newdi)
print()
import time
cluStart=[]
# convert newdi from epoch back to date and time
for i in newdi:
	cluStart.append(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i[0])))

print(cluStart)

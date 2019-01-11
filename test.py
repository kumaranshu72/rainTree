import os
import time
from operator import itemgetter

def convert2ephoc(tm):
    pattern = '%d.%m.%Y %H:%M:%S'
    epoch = int(time.mktime(time.strptime(tm, pattern)))
    return epoch

files = os.listdir("logs")

disconnects = {}
for f in files:
    f_in = open("logs/"+f, "r")
    for x in f_in:
      year = f[:4]
      result = [y.strip() for y in x.split('|')]
      #print(result)
      ind = result[0].find("ComputerName")

      if ind!=-1 and result[2]=='Client is disconnected from agent.':
          date = result[1][4:6]+'.'+result[1][1:3]+'.'+year+" 0:0:0"
          if disconnects.get(convert2ephoc(date)):
              disconnects[convert2ephoc(date)].append(result[0][ind+13:result[0].find(" ",ind+13)])
          else:
              disconnects[convert2ephoc(date)]=[]
              disconnects[convert2ephoc(date)].append(result[0][ind+13:result[0].find(" ",ind+13)])
    f_in.close()

#for x in sorted_disconnects:
#    print(sorted_disconnects[x])

date = raw_input("Date:")
from_date = date[0:2]+"."+date[3:5]+"."+date[6:10]+" 00:00:00"
from_ts = convert2ephoc(from_date)
to_date = date[14:16]+"."+date[17:19]+"."+date[20:24]+" 00:00:00"
to_ts = convert2ephoc(to_date)

system = {}
for x in disconnects:
    if x >= from_ts and x <= to_ts:
        for y in disconnects[x]:
            if system.get(y):
                system[y]+=1
            else:
                system[y] = 1

output = sorted(system.items(), key=itemgetter(1),reverse=True)

print("\nComputer Name Number of Disconnects\n")
for x in output:
    print(x[0]+" "+str(x[1]))

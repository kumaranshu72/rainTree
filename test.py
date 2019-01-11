import os
import time

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

for key in disconnects:
    print(key)

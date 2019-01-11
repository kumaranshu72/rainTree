import os

files = os.listdir("logs")

for f in files:
    f_in = open("logs/"+f, "r")
    for x in f_in:
      result = [y.strip() for y in x.split('|')]
      #print(result)
      ind = result[0].find("ComputerName")

      if ind!=-1 and result[2]=='Client is disconnected from agent.':
          print(result[0][ind+13:result[0].find(" ",ind+13)],result[1],result[2])
    f_in.close()

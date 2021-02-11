def filterByMonth(data, month):
 result = []
 for i in data:
  m = i['issued'][5:7]
  if int(i['issued'][5:7])==month:
    result.append(i)
    return result

    print(filterByMonth(data, 10))

import csv
def writeDataToCSVFile(file,data,keysoflist,boolean):
    with open(file, 'w') as f:
     if boolean:
       f.write(",".join(keysoflist)+"\n")
       for i in data:
         result=[]
         for key in keysoflist:
           result.append(i[key])
           f.write(",".join(result)+"\n")
     


#def filterByMont(data,month):
  #result=[]
  #for i in data:
    #if month>=10:
     # if i['issued'][5]==month//10 and i['issued'][6]==month%10:
      #  result.append(i)
  #return result


 #def filterByMonth(data,month):
  # result = []
   #for i in data:
    # for k,v in i.items():
      # for i['issued'] in data:
       #  value = s[4:6]
       #  if month== i[issued]:
       #    result.append(i)
       #    return result


import csv
def writeDataToCSVFile(file,data,keysoflist,boolean):
    with open(file, 'w') as f:
     if boolean:
       f.write(",".join(keysoflist)+"\n")
       for i in data:
         result=[]
         for key in keysoflist:
           result.append(i[key])
           f.write(",".join(result)+"\n")
     

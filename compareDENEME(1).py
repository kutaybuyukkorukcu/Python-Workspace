"""
import csv

with open('C:/Users/kutay/Desktop/book1.csv','rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter= ' ', quotechar = '|')
    for row in spamreader:
        print(', '.join(row))

t1 = open("book1.csv",'r')

fileone = t1.readlines()
print(t1)
t1.close()

outFile =


import csv

with open('C:/Users/kutay/Desktop/Book1.csv') as csvfile:
    readCSV = csv.reader(csvfile, limiter = ',')
    for row in readCSV:
        print (row)



import csv


with open('C:/Users/kutay/Desktop/Book1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    dates = []
    colors = []
    for row in readCSV:
        color = row[3]
        date = row[0]

        colors.append(color)
        dates.append(date)
        # colors.append(color)

    print(dates)
    print(colors)

    whatColor = input('What color do you witsh to know the date of? :')
    coldex = colors.index(whatColor)
    theDate = dates[coldex]
    print('The date of',whatColor,'is',theDate)

"""
"""
import pandas as pd

with open('C:/Users/kutay/Desktop/request.csv', 'r') as t1, open('C:/Users/kutay/Desktop/request1.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()
//dizi olarak dosyadaki veriyi al
with open('C:/Users/kutay/Desktop/solvedRequest.csv', 'w') as outFile:
    for line in filetwo:
        if line not in fileone:
            outFile.write(line)

"""

"""
import pandas as pd
import datetime

class generalCompare:

    table = pd.read_csv(data1)
    table2 = pd.read_csv(data2)
    csv_columnname = ["TIME", "PQ", "CPU", "MEMORY"]
    table.columns = csv_columnname
    row_count = sum(1 for row in table) + 1



class firstCompare(generalCompare):

    def printFirst(self):
        table = pd.read_csv(data1)
        csv_columnname = ["TIME","PQ","CPU","MEMORY"]
        table.columns = csv_columnname

        print(generalCompare.printTime())
        print(generalCompare.printPQ())
        print(generalCompare.printCPU())
        print(generalCompare.printMEMORY())

data1 = input("Select the first csv file you want to compare :")
data2 = input("Select the second csv file you want to compare :")
firstCompare.printFirst()
"""
"""
def tab():
    table = pd.read_csv(data)
    csv_sutun_isimleri = ["TIME","PQ","CPU","MEMORY"]
    table.columns = csv_sutun_isimleri

    datetimeFormat = "%H:%M"
    date1 = max(table["TIME"])
    date2 = min(table["TIME"])
    diff = datetime.datetime.strptime(date1,datetimeFormat) - datetime.datetime.strptime(date2, datetimeFormat)
    print(diff)

    row_count = sum(1 for row in table) + 1
    print(sum(table["PQ"]))

    print(sum(table["CPU"]) / row_count)
    print(sum(table["MEMORY"]) / row_count)
"""

"""
import pandas as pd
import datetime

class printProperties():     

    csvCount = int(input("Kac tane csv dosyasi karsilastiracaksiniz?"))
    for i in csvCount:
        data[i] = input("i. csv dosyasinin pathini giriniz : ")
    table = ['table1','table2','table3','table4']
    data = ['data1','data2','data3','data4']
    for i in range(0,csvCount):
        table[i] = pd.read_csv(data[i])
    csv_sutun_isimleri = ["TIME","PQ","CPU","MEMORY"]
    table.columns = csv_sutun_isimleri
    row_count = sum(1 for row in table) + 1

    def properties(self):

        self.datetimeFormat= "%H:%M"
        maxT = max(table["TIME"])
        minT = min(table["TIME"])
        diff = datetime.datetime.strptime(maxT, datetimeFormat) - datetime.datetime.strptime(minT, datetimeFormat)
        print(diff)
        print(sum(table["PQ"]))
        print(sum(table["CPU"]) / row_count)
        print(sum(table["MEMORY"]) / row_count)

"""

"""
import pandas as pd
import matplotlib

def tab():
    table = pd.read_csv(data)
    datetimeFormat = "%H:%M"
    date1 = max(table["TIME"])
    date2 = min(table["TIME"])
    diff = datetime.datetime.strptime(date1,datetimeFormat) - datetime.datetime.strptime(date2, datetimeFormat)
    print(diff)
    c = max(table['PQ'])
    print(c)
    print("veri 1-->işlenen veri :", c, "--------------------------->geçen süre :", diff)
    table[['TIME', 'PQ']].plot(figsize=(10, 10))
def tab2():
    table2 = pd.read_csv(data2)
    datetimeFormat = "%H:%M"
    date3 = max(table["TIME"])
    date4 = min(table["TIME"])
    diff2 = datetime.datetime.strptime(date3,datetimeFormat) - datetime.datetime.strptime(date4, datetimeFormat)
    print(diff2)
    y=max(table2['PQ'])
    print("veri 2--------------------------------------->işlenen veri :", y, "--------------------------->geçen süre :", diff2)
    table2[['TIME', 'PQ']].plot(figsize=(10, 10))
data = input('okunması istediğiniz csv dosyasını secin: ')
data2 = input('okunması istediğiniz csv dosyasını secin: ')
table2 = pd.read_csv(data2)
table = pd.read_csv(data)
table2[['TIME', 'PQ']].plot(figsize=(10, 10))
table[['TIME', 'PQ']].plot(figsize=(10, 10))
tab()
tab2()

"""

"""
print ("Reading the entire file into a list")
text_file = open("C:/Users/kutay/Desktop/request1.csv", "r")
lines = text_file.readlines()
print(lines)
print(len(lines))
for line in lines:
    print(line)
text_file.close()
//////////////////////////////////////////////////////////////
with open("C:/Users/kutay/Desktop/request1.csv") as f:
    myList = list(f)
    print(myList)
"""

"""
import pandas as pd
import matplotlib.pyplot as plt
class comPare:
    def __init__(self, tables, data):
        self.tables = tables
        self.tables = pd.read_csv(data)
        self.data = ['request.cvs', 'request.cvs', 'request.cvs']
    def tab(self,tables,data):
        for i in self.tables:
            if self.data in self.tables:
                pass
                else:
                self.tables.append(data)
                for i in self.tables['TIME'] :
                    a = max(tables['TIME'][i])
                    b = min(tables['TIME'][i])
                    d = a - b
                    print(d)
                    c = max(tables['PQ'])
                    print(c)
                    print("veridata :",i, "--------------------------------------->işlenen veri :", tables['TIME'][i], "--------------------------->geçen süre :",c[i])
                    #table[['TIME', 'PQ']].plot(figsize=(10, 10))
                    #  """
                    # def tab2():         table2 = pd.read_csv(data2)
                    # o= max(table2['TIME'])         p= min(table2['TIME'])
                    # op= o-p
                    # y=max(table2['PQ'])
                    # print("veri 2--------------------------------------->işlenen veri :", y, "--------------------------->geçen süre :", op)
                    # table2[['TIME', 'PQ']].plot(figsize=(10, 10))              """   #data = input('okunması istediğiniz csv dosyasını secin: ')
                    #  data2 = input('okunması istediğiniz csv dosyasını secin: ')
                    # tab()
                    #  tab2()
"""
def printProp(x):
    row_count = sum(1 for row in x) + 1
    datetimeFormat = "%H:%M"
    maxT= max(x["TIME"])
    minT = min(x["TIME"])
    diff = datetime.datetime.strptime(maxT, datetimeFormat) - datetime.datetime.strptime(minT, datetimeFormat)
    print(diff)
    print(sum(x["PQ"]))
    print(sum(x["CPU"]) / row_count)
    print(sum(x["MEMORY"]) / row_count)
"""

"""
import pandas as pd
import datetime

class dataStruct:
    def rowCount(self,x):
        row_count = sum(1 for row in x) + 1
        return(row_count)
    def timeDiff(self,x):
        datetimeFormat = "%H:%M"
        maxT = max(x["TIME"])
        minT = min(x["TIME"])
        diff = datetime.datetime.strptime(maxT, datetimeFormat) - datetime.datetime.strptime(minT, datetimeFormat)
        return diff
    def returnPQ(self,x):
        pqV = sum(x["PQ"])
        return pqV
    def returnCPU(self,x):
        cpuV = sum(x["CPU"]) / dataStruct.row_count(self,x)
        return cpuV
    def returnMEMORY(self,x):
        memoryV = sum(x["MEMORY"]) / dataStruct.row_count(self,x)
        return memoryV
    def printCPU(self,x):
        print(dataStruct.returnCPU(self,x))

    data1 = input("Select the first csv file you want to compare :")
    table1 = pd.read_csv(data1)
    csv_columnname = ["TIME", "PQ", "CPU", "MEMORY"]
    table1.columns = csv_columnname
    printCPU(self,table1)
"""

import webbrowser
import pandas as pd
import datetime

def printFunc():
    csvCount = int(input("Kac tane csv dosyasi karsilastiracaksiniz?"))
    data = []
    table = []
    rowSayisi = []
    csvFile = []
#usecols ile istenen sutunlari okutabiliriz
    for i in range(0,csvCount): #csv dosyalarinin pathlerini data listesine yaz
        plsWork = input("i. csv dosyasinin pathini giriniz : ")
        data.append(plsWork)

    for i in range(0,csvCount): #data pathlerini oku ve table listesine yaz
        plsWork2 = pd.read_csv(data[i])
        table.append(plsWork2)
    csv_sutun_isimleri = ["ID","TIME","PQ","CPU","MEMORY"]
    for i in range(0,csvCount): #Her table icin sutun ata
        table[i].columns = csv_sutun_isimleri

    for i in range(0,csvCount):  #Her table icin farkli bir row sayisi olmali
        plsWork3 = sum(1 for row in table[i])
        rowSayisi.append(plsWork3)

    for i in range(0,csvCount): #alter table islemi
        datetimeFormat = "%H:%M"
        maxT = max(table[i]["TIME"])
        minT = min(table[i]["TIME"])
        diff = datetime.datetime.strptime(maxT, datetimeFormat) - datetime.datetime.strptime(minT, datetimeFormat)
        table[i].drop("TIME",axis=1,inplace=False)
        table[i]["TIME"] = diff
        pqV = sum(table[i]["PQ"])
        table[i].drop("PQ",axis=1,inplace=False)
        table[i]["PQ"] = pqV
        cpuV = sum(table[i]["CPU"]) / rowSayisi[i]
        table[i].drop("CPU",axis=1,inplace=False)
        table[i]["CPU"] = cpuV
        memoryV = sum(table[i]["MEMORY"]) / rowSayisi[i]
        table[i].drop("MEMORY",axis=1,inplace=False)
        table[i]["MEMORY"] = memoryV
        plsWork4 = table[i][:1]
        csvFile.append(plsWork4)

    for n in range(0,len(csvFile)-1):
        e = csvFile[n]
        for m in range(1,len(csvFile)):
            if n == m or n == m+1 :
                continue
            z = csvFile[m]
            print(e)
            print(z)
            print("----------------")


""" 
with open("c:/users/kutay/desktop/a.txt") as f:
    f.write(csvFile[0])
    f.close()
"""


"""                     
n = 0
m = 1
while(n<10)
    if n == 0:
        n += 1
    print(n)
    n += 1
"""

"""
    e = csvFile[n]
    m = n+1
    for m in csvFile[1:]:
        z = csvFile[m]
        print(e + z)
"""

"""

with open('C:/Users/kutay/Desktop/a.txt', 'r') as t1:
    #fileone = t1.readlines()
    t1.read().replace()

"""
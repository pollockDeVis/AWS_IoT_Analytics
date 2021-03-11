# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 23:20:28 2020

@author: Pollock
"""

# def func1():
#     print("I am a function")
    
# def func2(arg1, arg2):
#     print(arg1, " ", arg2)
    
# def cube(x):
#     return x*x*x


# # func1()
# # print(func1())
# # print(func1)

# # func2(10, 20)
# # print(func2(10, 20))
# # print(func2)


# def power(num, x=1):
#     result = 1
#     for i in range (x):
#         result = result* num
#     return result

# def multi_add(*args): #varibale arguments always has to be the last one
#     result = 0
#     for x in args:
#         result = result + x
#     return result
# # print(cube(3))

# print(power(2))
# print(power(2,3))
# print(power(x=3, num=2)) #order doesnt matter if names of arg is explicitly declared
# print(multi_add(10,2,4,5,6))



# def main():
#     x, y = 10, 1000
# # No switch case in python
    
#     if(x<y):
#         st = "x is less than y"
#     elif(x == y):
#         st = "x is the same as y  "
#     else:
#         st = "x is greater than y"
#     print(st)
    
# #Conditional statement
#     st = "x is less than y" if (x<y) else "x is greater than or same as y"
#     print(st)

# if __name__ == "__main__":
#     main()


    # while (x < 5):
    #     print(x)
    #     x = x+1
        
    # for x in range(5, 10): #inclusive first but not last
    #     print(x)

    # days = ["Mon", "Tue", "wed", "thur", "fri", "sat", "sun"]
    
    # for i in days:
    #     print (i)
    
    # for x in range (5, 10):
    #     #if (x==7): break
    #     if(x%2 == 0): continue
    #     print(x)
    
    # days = ["Mon", "Tue", "wed", "thur", "fri", "sat", "sun"]
    
    # for i, d in enumerate(days): # gives the index along with the content
    #     print (i, d)


# class myClass():
#    def method1(self): #first argument to a method is class is usually self | Method is for class. Function
#    #is on its own
#        print("myClass method1")
       
#    def method2(self, someString):
#        print("myClass method2 " + someString)


# class anotherClass(myClass):
#    def method1(self): 
#        myClass.method1(self) #inheriting from Super Class/Base Class
#        print("anotherClass method1")
       
#    def method2(self, someString): #This will override the method2 in SuperClass
#        print("anotherClass method2 ")
       
       
# def main():
#     c = myClass()
    
#     c.method1()
#     c.method2("Hello World")
    
#     c2 = anotherClass()
#     c2.method1()
#     c2.method2("this is a string")
        
# if __name__ == "__main__":
#     main()
        
        
# import math

# print("the square root of 16 is", math.sqrt(16))     

# print("Pi is: ", math.pi)   
# print("The v")
 
# today = date.today()
# print("today's date is ", today)    
    
    
# print("Date components: ", today.day, today.month, today.year)

# print("Today's weekday # is: ", today.weekday())
# days = ["mon", "Tue", "wed", "Thu", "fri", "sat","sun"]
# print("Today's day is ", days[today.weekday()])

# today = datetime.now()
# print("The current date and time is ", today)      

# t = datetime.time(datetime.now())

# today= datetime.now()
# print(today)
# t = datetime.time(datetime.now())
# print(t)


# print(now.strftime("%a, %d, %B, %y"))   #   Sun, 01, November, 20
# print(now.strftime("Locale date & time: %c")) # Locale setting Sun Nov  1 17:41:11 2020
# print(now.strftime("Locale date: %x")) #11/01/20
# print(now.strftime("Locale time: %X")) #17:41:11
# print(now.strftime("Current time: %I: %M: %S %p ")) #Current time: 05: 49: 58 PM 
# print(now.strftime("Current time: %H: %M"))         #Current time: 17: 49
# now = datetime.now()
           
        
# from datetime import date   
# from datetime import time
# from datetime import datetime
# from datetime import timedelta
 
      
        
# def main():

#     # print(timedelta(days=365, hours=5, minutes=1)) #365 days, 5:01:00
#     # now = datetime.now()
#     # print("Today is " +  str(now)) #Today is 2020-11-01 17:59:53.652267
#     # print("one year from  today will be " + str(now + timedelta(days= 365))) #one year from  today will be 2021-11-01 17:59:53.652267
#     # print("In two days and 3 weeks it will be " + str(now + timedelta(days=2, weeks= 3))) #In two days and 3 weeks it will be 2020-11-24 17:59:53.652267
    
#     # t = datetime.now() - timedelta(weeks = 1)
    
#     # s = t.strftime("%A %B %d, %Y")
#     # print("One week ago it was " + s) #One week ago it wasSunday October 25, 2020
    
#     today = date.today()
#     print(today)
#     afd = date(today.year, 4, 1)
    
#     if afd < today:
#         print("April fool's day went by %d days ago" % ((today-afd).days)) #April fool's day went by 214 days ago
#         afd = afd.replace(year = today.year+1)
        
#     time_to_afd = afd-today
#     print("It's just ", time_to_afd.days, "days until april fool's day") #It's just  151 days until april fool's day
# if __name__ == "__main__":
#     main()
        
        




#import calendar

#Prints out calendar in plain text
#c = calendar.TextCalendar(calendar.SUNDAY)
# st = c.formatmonth(2021, 1, 0, 0)
# print(st)
        
#Prints out calender in HTML
# hc = calendar.HTMLCalendar(calendar.SUNDAY)
# st = hc.formatmonth(2020, 1)     
# print(st)

#Iterates through all the days in the month        
# for i in c.itermonthdays(2020, 5):    
#     print(i)   

# for name in calendar.month_name:
#     print(name)    
    
# for day in calendar.day_name:
#     print(day)
        

# print("Tean meetings will be on: ")
# for m in range(1,13):
#        cal = calendar.monthcalendar(2018, m)
#        #print(cal)
#        weekone = cal[0]
  
#        weektwo = cal[1]

#        if weekone[calendar.FRIDAY] !=0:
#            meetday = weekone[calendar.FRIDAY]
#        else:
#            meetday = weektwo[calendar.FRIDAY]
       
#        print("%10s %1d" % (calendar.month_name[m], meetday)) #10 and 4 are white spaces
        
    # f = open("textfile.txt","r") #+ is create file if doesnt exist
    # #f = open("py_exercise/textfile.txt", "a")
    # # for i in range(10):
    # #     f.write("This is line " + str(i)+"\r\n")
    
    # # f.close()        
        
    # if f.mode == 'r':
    #     #contents = f.read()
    #     fl = f.readlines()

    #     for x in fl:
    #         print(x)
    #     #print(contents)
# import datetime
# from datetime import date, time, timedelta
# import time      

    # td = datetime.datetime.now()- datetime.datetime.fromtimestamp(
        
    #         path.getmtime("textfile.txt")
    #     )
    # print("it has been "+ str(td)+ "since the file was modified") #it has been 5:21:57.969402since the file was modified
    # print("or, "+ str(td.total_seconds())+ "seconds") #19317.969402seconds
     # print(os.name)
    # print("Item Exists: " + str(path.exists("textfile.txt")))
    # print("Item is a file: " + str(path.isfile("textfile.txt")))
    # print("Item is a directory: "+ str(path.isdir("textfile.txt"))) 
    
    # print("Item path: " + str(path.realpath("textfile.txt"))) #Item path: C:\Users\Pollock\Desktop\textfile.txt
    # print("Item real path & name: " + str(path.split(path.realpath("textfile.txt")))) # returns a tuple: Item real path & name: ('C:\\Users\\Pollock\\Desktop', 'textfile.txt')
     
    # t= time.ctime(path.getmtime("textfile.txt")) #Sun Nov  1 19:57:43 2020
    # print(t)
    # print(datetime.datetime.fromtimestamp(path.getatime("textfile.txt"))) #2020-11-01 19:57:43.068970
          
    # if path.exists("textfile.txt"):
    #     src  = path.realpath("textfile.txt")
        
    # dst = src + ".bak" #adds this extension to the end of the file 
    
    # # shutil.copy(src, dst) #copies from source to dest
    # # shutil.copystat(src, dst) #copies metadata
    
    # # os.rename("textfile.txt", "newfile.txt")
  
    # # root_dir, tail = path.split(src)
    # # shutil.make_archive("archive", "zip", root_dir) #copies everything in the directory in the zip file
    # with ZipFile("testzip.zip", "w") as newzip: #with keyword creates local scopes for objects
    #     newzip.write("textfile.txt")
    #     newzip.write("textfile.txt.bak")
  
# import os
# from os import path
# import shutil  
# from shutil import make_archive     
# from zipfile import ZipFile 
 
    # webUrl = urllib.request.urlopen("http://www.google.com")
    # print("result code: " + str(webUrl.getcode()))
    # data = webUrl.read() #return HTML data
    # print(data)

    # urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson"
    
    # webUrl = urllib.request.urlopen(urlData)
    # print("result code: " + str(webUrl.getcode()))
    # if(webUrl.getcode() == 200):
    #     data = webUrl.read()
    #     printResults(data)
    # else:
    #     print("received error, cannot parse results")





# import  urllib.request
# import json

  
# def printResults(data):
#     theJSON = json.loads(data) #converts JSON to python object
    
#     if "title" in theJSON["metadata"]:
#         print(theJSON["metadata"]["title"])
        
#     count = theJSON["metadata"]["count"]
#     print(str(count)+ " events recorded")
    
#     for i in theJSON["features"]:
#         print(i["properties"]["place"])
#     print("------------------\n")
    
    
#     for i in theJSON["features"]:
#         if i["properties"]["mag"] >= 4.0:
#             print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
#     print("------------------\n")
    
#     print("Events that were felt: ")
#     for i in theJSON["features"]:
#         feltReports = i["properties"]["felt"]
#         if feltReports != None:
#             if feltReports > 0:
#                 print("%2.1f" % i["properties"]["mag"], i["properties"]["place"], " reported " + str(feltReports) + "time(s)")
                
     
# from html.parser import HTMLParser     

# metacount = 0

# class MyHTMLParser(HTMLParser):
#     def handle_comment(self, data):
#         print("Encountered comment: ", data)
#         pos = self.getpos()
#         print("\t At line: ", pos[0], " position ", pos[1]) #second position is the number of whitespace
        
#     def handle_startendtag(self, tag, attrs):
#         global metacount
#         if tag == 'meta':
#             metacount += 1
#         print("Encountered tag: ", tag)
#         pos = self.getpos()
#         print("\t At line: ", pos[0], " position ", pos[1]) #second position is the number of whitespace
        
#         if attrs.__len__() > 0:
#             print("\tAttributes")
#             for a in attrs:
#                 print("\t", a[0], "=", a)
        
#     def handle_endtag(self, tag):
#         print("Encountered tag: ", tag)
#         pos = self.getpos()
#         print("\t At line: ", pos[0], " position ", pos[1]) #second position is the number of whitespace
        
        
#     def  handle_data(self, data):
#         if data.isspace():
#             return
#         print("Encountered data: ", data)
#         pos = self.getpos()
#         print("\tAt line: ", pos[0], " position ", pos[1]) #second position is the number of whitespace
        
    # parser = MyHTMLParser()
    # f = open("samplehtml.html")
    # if f.mode =='r':
    #     contents = f.read()
    #     parser.feed(contents)
    # print("Meta tags found: " + str(metacount))    

    # doc = xml.dom.minidom.parse("samplexml.xml")
    
    # print(doc.nodeName)
    # print(doc.firstChild.tagName)
    # skills = doc.getElementsByTagName("skill")
    # print("%d skills: " % skills.length)
    # for skill in skills:
    #     print(skill.getAttribute("name"))
        
        
    # newSkill = doc.createElement("skill")
    # newSkill.setAttribute("name", "Embedded C")
    # doc.firstChild.appendChild(newSkill)
    
    # skills = doc.getElementsByTagName("skill")
    # print("%d skills: " % skills.length)
    # for skill in skills:
    #     print(skill.getAttribute("name"))
    

# import xml.dom.minidom
    
def main():
    

    
if __name__ == "__main__":
    main()
        























        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
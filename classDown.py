#!/usr/bin/env python3

import requests
import os
import subprocess
import getpass
import shutil
from bs4 import BeautifulSoup

baseurl : str
login : str
password : str
file  : str

def mkChDir(nameDir):
   currentPath = os.getcwd()
   newDirPath =  currentPath + "/" + nameDir

   try:
      os.chdir(nameDir)
   except OSError:
      print ("Couldn't find directory named " + nameDir + " trying to create one")
      try:
         os.mkdir(nameDir)
      except OSError:
         print("Couldn't create directory. Do you have permission?")
         print ("Exiting")
         exit()
      else:
         os.chdir(nameDir)
         print ("Succesfully created directory " + nameDir)
   else:
      print(nameDir + " Directory found")

def menu():
   global baseurl
   global login
   global password
   print ("Select the website option: \n1. Qualidade de Software\n2. Tecnologia de Hardware\n3. Enter custom URL\n4. Exit")
   choice = input()
   if choice == "1":
      baseurl = "http://disciplinas.mafra.eti.br/qualidade-software/videos/"
      print ("Enter login")
      login = input()
      password = getpass.getpass("Enter password\n")
      mkChDir("Qualidade-Software")
   elif choice == "2":
      baseurl = "http://disciplinas.mafra.eti.br/THW/videos/"
      print ("Enter login")
      login = input()
      password = getpass.getpass("Enter password\n")
      mkChDir("Tecnologia-de-Hardware")
   elif choice == "3":
      print ("Please note that the page has to be in the same format as the others, and require a authentication")
      print ("EnterCustom URL with the /videos/ in the end: ")
      baseurl = input()
      print ("Enter login")
      login = input()
      password = getpass.getpass("Enter password\n")
      print ("The videos Downloaded here will be put in the /CustomURL folder")
      mkChDir("CustomURL")
   elif choice == "4":
      exit()
   else:
      print("Invalid choice, try again")
      menu()
def m3u8ToMp4(baseurl, file, login, password, outputVideoName):
   mkChDir("tmpFiles")
   url = baseurl + file
   response = requests.get(url, auth=(login, password))
   htmlText = response.text
   urlTsList = htmlText.split("\n")
   keyBaseStr = urlTsList[4];

   keyIdStart = keyBaseStr.find("videos/") + 7
   keyIdEnd = keyBaseStr.find("\",IV")
   keyId = keyBaseStr[keyIdStart:keyIdEnd]
   keyPathStart = keyBaseStr.find("URI=\"") + 5
   oldKeyPath = keyBaseStr[keyPathStart:keyIdEnd]
   newKeyPath = keyBaseStr.replace(oldKeyPath, keyId)

   newM3u8File = open(file, "w+")

   for k in range(len(urlTsList) - 1):
      if k == 4:
         newM3u8File.write(newKeyPath + "\n")
      elif k == len(urlTsList) - 1:
         newM3u8File.write(urlTsList[k])
      else:
         newM3u8File.write(urlTsList[k] + "\n")
   newM3u8File.close()

   print("Downloading key")
   keyUrl = baseurl + keyId
   r = requests.get(keyUrl, allow_redirects=True, auth=(login, password))
   open(keyId, 'wb').write(r.content)


   for i in range(6, len(urlTsList) - 1, 2):
      print("Downloading " + urlTsList[i])
      tsUrl = baseurl + urlTsList[i]
      r = requests.get(tsUrl, allow_redirects=True, auth=(login, password))
      open(urlTsList[i], 'wb').write(r.content)

   os.system("ffmpeg -allowed_extensions ALL -i " + file +  " -acodec copy -vcodec copy " +  "\"../" + outputVideoName + "\"")
   os.chdir("../")
   try:
      shutil.rmtree("tmpFiles")
   except OSError as e:
      print ("Error: " + e.sterror)


def downloadFile(baseurl, file, login, password):
   url = baseurl + file
   print ("Downloading " + file)
   r = requests.get(url, allow_redirects=True, auth=(login, password))
   open(file, 'wb').write(r.content)
   print ("Done")

menu()

response = requests.get(baseurl, auth=(login, password))
if response.ok:
   print ("Succesfully logged in!")
else:
   print (response)
   print ("Couldn't get in :(")
   print ("Exiting script")
   exit()

htmlText = response.text
soup = BeautifulSoup(response.content, 'html.parser')
ulTag = list(soup.children)[4]

videosUrl = []
for li in ulTag.findAll('li'):
   for a in li.findAll('a'):
       videosUrl.append(a.get('href'))

videos = []
for li in ulTag.findAll('li'):
   for b in li.findAll('b'):
       videos.append(b.text)

print ("Choose the video to Download")
videoName = "video.mp4"
for index in range(len(videos)):
   print (str(index + 1) + ". " + videos[index])
print (str(len(videos) + 1) + ". " + "Download all")
while True:
   videoInput = input()
   if int(videoInput) == len(videos) + 1:
      for iterator in range(len(videos)):
         print ("Downloading " + videos[iterator])
         file = videosUrl[iterator]
         videoName = videos[iterator] + ".mp4"
         fileExtension = file.split(".")[1]
         if fileExtension == "m3u8":
            m3u8ToMp4(baseurl, file, login, password, videoName)
         else:
            downloadFile(baseurl, file, login, password)
      exit()
   try:
      if int(videoInput) <= len(videos) and int(videoInput) > 0:
         file = videosUrl[int(videoInput) - 1]
         videoName = videos[int(videoInput) - 1] + ".mp4"
         break
      else:
         print ("Enter a valid number")
   except ValueError:
      print ("Enter a valid number")
fileExtension = file.split(".")[1]
if fileExtension == "m3u8":
   m3u8ToMp4(baseurl, file, login, password, videoName)
else:
   downloadFile(baseurl, file, login, password)

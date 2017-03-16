#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import mutagen
import shutil

argu=input("Drag your folder with songs form osu and press enter: ")
arg = argu.replace("\"","")


try:
    os.makedirs("output/")
except OSError:
    print("exist")

for root, dirs, files in os.walk(arg):
    print (root)

    for bla in (x for x in files if ".mp3" in x):
         #root+"\\"+bla
         try:
             audio = MP3(root + "\\" + bla)
             lenght = audio.info.length
         except mutagen.mp3.HeaderNotFoundError:
             str = (root.replace(arg, ""))
             name = (str.split(" ", 1)[1])
             author = (name.split(" - ", 1)[0])
             title = (name.split(" - ", 1)[1])
             namefile = author + " - " + title + ".mp3"
             shutil.copy(root + "\\" + bla, "output/" + namefile)
             print("&" * 20)
             print("&" * 20)
             print("&" * 20)
             lenght=0

         print (lenght)


         if (lenght>30):

            str = (root.replace(arg,""))
            name = (str.split(" ",1)[1])
            author = (name.split(" - ",1)[0])
            title = (name.split(" - ",1)[1])
            namefile = author+" - "+title+".mp3"
            print (namefile)
            shutil.copy(root + "\\" + bla, "output/"+namefile)

            try:
                audioID = EasyID3("output/"+namefile)
                audioID.delete()
            except mutagen.id3._util.ID3NoHeaderError:
                audioID = mutagen.File("output/"+namefile, easy=True)
                audioID.add_tags()

            audioID["title"] = title.lstrip(' ')
            audioID["artist"] = author.lstrip(' ')
            audioID.save(v2_version=3)

    print("*" * 20)

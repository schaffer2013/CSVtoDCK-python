import scrython
import csv
import time
import shutil

from PIL import Image
import requests
import createDCK
from createDCK import CardFromCSV 
from io import BytesIO
#import pygame

deckName=input("Enter your deck name : ") 

arrCards=[]

with open('testDeck.csv', newline='') as csvfile:
        reader=csv.reader(csvfile, delimiter=',')
        header=next(reader) #Get past header

        for row in reader:
            arrCards.append(CardFromCSV(row[0],row[1],row[2],row[9]))
cmdrs=[]
for card in arrCards:
    if card.isCommander:
        cmdr=scrython.cards.Named(fuzzy=card.name)
        cmdrs.append(cmdr)
        print (cmdr.name())
        time.sleep(0.1)

##response = requests.get(cmdr.image_uris(image_type='large'))
##img = Image.open(BytesIO(response.content))
##img.show()
##img.close()

deckFile="decks\\"+deckName+".dck"

f=open(deckFile,"w+")
f.write("[metadata]\n")
f.write("Name="+deckName+"\n")
f.write("[Commander]\n")
for cmdr in cmdrs:
    f.write("1 "+str(cmdr.name())+"|"+(str(cmdr.set_code())).upper()+"\n")
f.write("[Main]\n")

for card in arrCards:
    if (not card.isCommander) and card.board=='main':
        c=scrython.cards.Named(fuzzy=card.name)
        name=c.name().split(" // ")[0]
        print(name)
        f.write(str(card.quantity)+" "+(name)+"|"+(c.set_code()).upper()+"\n")
        time.sleep(0.1)

f.close()

dest='C:\\Users\\phils\\AppData\\Roaming\\Forge\\decks\\commander'

shutil.copy2(deckFile,dest)



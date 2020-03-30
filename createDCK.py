import scrython
import csv
import time

from PIL import Image
import requests
from io import BytesIO
#import pygame

class CardFromCSV:
    def __init__(self,brd,qty,n,cmd):
        self.board=brd
        self.quantity=int(qty)
        self.name=n
        self.isCommander= (cmd=='True')




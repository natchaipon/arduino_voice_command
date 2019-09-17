# -*- coding: utf-8 -*-
import serial
from pythainlp.tokenize import word_tokenize
import speech_recognition as sr
import urllib.request
import time

ser = serial.Serial('COM4', 9600, timeout=0)

while True:
    onled = "H"
    offled = "L"
    readserial = "R"
    readserial1 = "G"
    #ser.write(serialcmd.encode())

    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        outputaudio = r.recognize_google(audio,language = "th-TH")
    except sr.RequestError as e: 
        print("Could not understand audio")
    except sr.UnknownValueError:
        outputaudio = ""
        print("ไม่เข้าใจคำสั่ง")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    cut = outputaudio
    cutlist = word_tokenize(cut)
    txt = (','.join(str(x) for x in cutlist))
    print(txt)

    if txt.find("สมบูรณ์")==0:
        subcutlist = txt[8:]
        print(subcutlist)
        print("........................................................")
        
        if subcutlist.find("เปิดไฟ")==0:
            print("ok")
            ser.write(onled.encode())

        if subcutlist.find("ปิดไฟ")==0:
            print("ok")
            ser.write(offled.encode())

        if subcutlist.find("ดู")==0 & subcutlist.find("ข้อมูล")==0:          
            print("ok")
            ser.write(readserial.encode())
            time.sleep(2)
            i = str(ser.readline()[:4])
            p = list(i)
            sub = p[2:5]
            tostring = ''.join(sub)
            print("สถานะเซ็นเซอร์แก๊ส "+tostring)
            time.sleep(1)

        if subcutlist.find("ฝนตก")==0 & subcutlist.find("ไหม")==0:
            print("ok")
            ser.write(readserial1.encode())
            time.sleep(4)
            i = str(ser.readline()[:4])
            p = list(i)
            sub = p[2:3]
            tostring = ''.join(sub)
            if tostring == "T":
                print("ตอนนี้ฝนตก")
            elif tostring == "F":
                print("ตอนนี้ฝนไม่ตก")
            time.sleep(3)
    outputaudio = ""
            

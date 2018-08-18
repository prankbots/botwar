# -*- coding: utf-8 -*-
from linepy import *
from akad.ttypes import *
from multiprocessing import Pool
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess,asyncio
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast
_session = requests.session()
translateen = []
line = LINE()
line.log("Auth Token : " + str(line.authToken))
channelToken = line.getChannelResult()
settingsOpen = codecs.open("prankBots.json","r","utf-8")
settings = json.load(settingsOpen)
oepoll = OEPoll(line)
lineProfile = line.getProfile()
lineSettings = line.getSettings()
lineMID = line.profile.mid
def backupData():
    try:
        backup = settings
        f = codecs.open('prankBots.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    time.sleep(5)
    python = sys.executable
    os.execl(python, python, *sys.argv)
def logError(text):
    line.log("[ ERROR ] " + str(text))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + " | " + inihari.strftime('%H:%M:%S')
    with open("prankBots.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            prankbot = pesan.replace(settings["keyCommand"],"")
        else:
            prankbot = "Undefined command"
    else:
        prankbot = text.lower()
    return prankbot
def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        if op.type == 5:
            line.findAndAddContactsByMid(op.param1)
            line.sendMessage(op.param1, "Thanks for add\nCreator Bots")
            line.sendContact(op.param1, 'u0ac948397fbc732bd3bc5ca273faa698')
        if op.type == 13:
            try:
                group = line.getGroup(op.param1)
                contact = line.getContact(op.param2)
                line.acceptGroupInvitation(op.param1)
            except Exception as error:
                logError(error)
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False:
                 setKey = ''
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != line.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        prankbot = command(text)
                        if 'Spongebob' in msg.text:
                            kontak = line.getContact(msg._from)
                            response = ("ada apa kau memanggilku ","ya aku disini ","apakah ada yang memesan krebipeti ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "keluar" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("ok gw keluar ya ","ok siap ","yaudah kalo gitu bye bye ","yasudahlah bye ","rese lu ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                            line.leaveGroup(msg.to)
                        if "makan" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("silahkan makan ","ok ","makan apa bos ","sepertinya aku tidak lapar ","oh tentu saja,sepertinya kau lapar ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "Siapa" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("kerang ajaib mungkin ","sepertinya beruang laut ","ohh.. aku tidak tau ","sepertinya para neftizen ","itu adalah kau ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "apa" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("oh aku tidak tau ","apa yang kau tanyakan ","ohh.. aku tidak tau ","apa itu kau ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "kemana" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("ke kuburan sana ","ke lubang buaya saja kalo begitu "," ","pergi bekerja keras mencari tikungan mu ","aku harus pulang ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "sayank" in text.lower() or "yank" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("beraninya kau panggil sayank ","apa kau para neftizen "," ","palalu peang ","iya sayank ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "mbuh" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("mbuh jare ","semprul kau "," ","tak colok ndasmu ","helehh knapa sih ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "kapan" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("kapan kapan aja dah ","emang mau ngapain "," ","ntah kapan gw gak tau ","kapan aja boleh ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "bot" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("paan lu manggil manggil ","oet hadir "," ","bot bot bot jembot ","jembot mana jmbot ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "knapa" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("gak tau ","gak knapa napa "," ","kepo lu ","knapa aja boleh ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "baper" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("puskun gih ","makan aja biar kenyang "," ","baper gw kick nih ","gak usah baper deh minum larutan dulu sana biar adem ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "asem" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("asem jare ","ketek lu asem "," ","asem opone ","lu asem ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "sue" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("lu sue gw mah kagak ","sabar.. "," ","bahhhh ","ndasmu ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "kamvret" in text.lower() or "kampret" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("astagfirullah jangan bilang gitu ","kasar banget lu njir "," ","paan lu mprett. ","biasa aja kalee ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "gw" in text.lower() or "aku" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("iya ","ada apa ","oh bgitu ","aku juga ","hooh ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "kuy" in text.lower() or "ayo" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("kuuyyyy ahh ","kmana ","gw gak di ajak njir ","ayolah kalo bgitu ","siaappp.! ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
                        if "kikil" in text.lower() or "kick" in text.lower():
                            kontak = line.getContact(msg._from)
                            response = ("dasar kikil ","bah kikil ","njirr ada kikil ","situ kikil . ","si kikil mana si kikil ")
                            respon = random.choice(response)
                            line.sendMessage(msg.to, respon + kontak.displayName)
    except Exception as error:
        logError(error)
        
        if op.type == 59:
            print (op)
        
#===========================PRANKBOTS SCRIPT===================#
while True:
    try:
      ops=oepoll.singleTrace(count=50)
      if ops != None:
        for op in ops: 
          bot(op)
          oepoll.setRevision(op.revision)
        
    except Exception as e:
        line.log("[SINGLE_TRACE] ERROR : " + str(e))
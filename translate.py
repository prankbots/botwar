# -*- coding: utf-8 -*-
from linepy import *
from akad.ttypes import *
from multiprocessing import Pool
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess,asyncio
from datetime import datetime, timedelta
from time import sleep
from googletrans import Translator
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
                        if 'Transla' in msg.text:
                              spl = msg.text.replace('Transla','')
                              if spl == 'te':
                                  if msg.to in translateen:
                                       msgs = "Auto Translate sudah aktif"
                                  else:
                                       translateen.append(msg.to)
                                       ginfo = line.getGroup(msg.to)
                                       msgs = "Auto Translate Diaktifkan\nDi Group : " +str(ginfo.name)
                                  line.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'te off':
                                    if msg.to in translateen:
                                         translateen.remove(msg.to)
                                         ginfo = line.getGroup(msg.to)
                                         msgs = "Auto Translate Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Auto Translate Sudah Tidak Aktif"
                                    line.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
        if op.type == 26:
               msg = op.message
               if msg.to in translateen:
                   try:
                       if msg.text is not None:
                           kata = msg.text
                           translator = Translator()
                           hasil = translator.translate(kata, dest='en')
                           A = hasil.text
                           line.sendMessage(msg.to, A)
                   except Exception as error:
                       pass
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
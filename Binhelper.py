
__author__ = 'Zing'
__version__ = '1.0.0'

from unicodedata import normalize
import wx
import os
import re
import time
import urllib
import string
import base64
import sqlite3
import hashlib
import binascii

"""
Form1 is the Page of Crack
"""

class Form1(wx.Panel):
    def __init__(self, *args, **kwargs):
        super(Form1, self).__init__(*args, **kwargs)
	self.colors = ['add','and', 'rol','sub',  'or','ror','mul','xor','shl','div','not','shr','divmod','neg','pow','abs','round','bswap']
	self.jinzhi=['10','16','2']
	self.createControls()
        self.bindEvents()
        self.doLayout()

    def createControls(self):
        self.loggerIn = wx.TextCtrl(self, style=wx.TE_MULTILINE)
	self.loggerOut = wx.TextCtrl(self, style=wx.TE_MULTILINE)
	self.but1 = wx.Button(self, label="Text->Dec")
	self.but2 = wx.Button(self, label="Dec->Text")
	self.but3 = wx.Button(self, label="Text->Hex")
	self.but4 = wx.Button(self, label="Hex->Text")
	self.but5 = wx.Button(self, label="Text->Oct")
	self.but6 = wx.Button(self, label="Oct->Text")
	self.but7 = wx.Button(self, label="Text->Bin")
	self.but8 = wx.Button(self, label="Bin->Text")

        self.but9 = wx.Button(self, label="result")
        self.txt1 = wx.TextCtrl(self, -1, "",
                size=(175, -1))
        self.txt2 = wx.TextCtrl(self, -1, "",
                size=(175, -1))
        self.txt3 = wx.TextCtrl(self, -1, "",
                size=(175, -1))
	self.colorRadioBox = wx.RadioBox(self,
            label="",
            choices=self.colors, majorDimension=3, style=wx.RA_SPECIFY_COLS)
        self.choseary = wx.RadioBox(self,
            label="",
            choices=self.jinzhi, majorDimension=3, style=wx.RA_SPECIFY_COLS)
        self.text1= wx.StaticText(self, -1, "operator1",
                (100, 10))
        self.text2= wx.StaticText(self, -1, "operator2",
                (100, 10))

    def bindEvents(self):
        for control, event, handler in \
            [(self.but1, wx.EVT_BUTTON, self.text2dec),
	     (self.but2, wx.EVT_BUTTON, self.dec2text),
	     (self.but3, wx.EVT_BUTTON, self.text2hex),
	     (self.but4, wx.EVT_BUTTON, self.hex2text),
	     (self.but5, wx.EVT_BUTTON, self.text2oct),
	     (self.but6, wx.EVT_BUTTON, self.oct2text),
	     (self.but7, wx.EVT_BUTTON, self.text2bin),
	     (self.but8, wx.EVT_BUTTON, self.bin2text),
            (self.but9, wx.EVT_BUTTON, self.caculate)

	     ]:
            control.Bind(event, handler)

    def text2dec(self,event):
        list1=list(self.loggerIn.GetValue())
        n=0
        while n< len(list1):
	        list1[n]=ord(list1[n])
	        n+=1
        m=0
        strd=''
        while m<len(list1):
	        strd+=str(list1[m])+' '
	        m+=1
        self.loggerOut.SetValue(strd)

    def dec2text(self,event):
        n=0
        s=''
        list1=self.loggerIn.GetValue().split(' ')
        while n<len(list1):
	        s+=chr(string.atoi(list1[n]))
	        n+=1
        self.loggerOut.SetValue(s)

    def text2hex(self,event):
        n=0
        strhex=''
        s=self.loggerIn.GetValue()
        list1=list(s)
        while n< len(list1):
            strhex+=hex(ord(list1[n]))+" "
            n+=1
        self.loggerOut.SetValue(strhex)

    def hex2text(self,event):
        n=0
        s=''
        list1=self.loggerIn.GetValue().split(' ')
        while n<len(list1):
	        s+=chr(string.atoi(list1[n],16))
	        n+=1
        self.loggerOut.SetValue(s)

    def text2oct(self,event):
        n=0
        stroct=''
        s=self.loggerIn.GetValue()
        list1=list(s)
        while n< len(list1):
            stroct+=oct(ord(list1[n]))+" "
            n+=1
        self.loggerOut.SetValue(stroct)

    def oct2text(self,event):
        n=0
        s=''
        list1=self.loggerIn.GetValue().split(' ')
        while n<len(list1):
	        s+=chr(string.atoi(list1[n],8))
	        n+=1
        self.loggerOut.SetValue(s)

    def text2bin(self,event):
        n=0
        strbin=''
        s=self.loggerIn.GetValue()
        list1=list(s)
        while n< len(list1):
            strbin+=bin(ord(list1[n]))+"  "
            n+=1
        self.loggerOut.SetValue(strbin)
    def bin2text(self,event):
        n=0
        s=''
        list1=self.loggerIn.GetValue().split(' ')
        while n<len(list1):
	        s+=chr(string.atoi(list1[n],2))
	        n+=1
        self.loggerOut.SetValue(s)

    def choseal(self,event):
        str=self.loggerIn.GetValue()

    def doLayout(self):
        raise NotImplementedError





    def caculate(self,event):
        operator1=self.txt1.GetValue()
        operator2=self.txt2.GetValue()
        cal=self.colorRadioBox.GetStringSelection()
        num=self.choseary.GetStringSelection()

        if cal=="xor" :
            if num=="2":
                result=str(int(operator1,2)^int(operator2,2))
                self.txt3.SetValue(result)
            elif num=="10":
                result=str(string.int(operator1)^string.int(operator2))
                self.txt3.SetValue(result)
            elif num=="16":
                result=str(int(operator1,16)^int(operator2,16))
                self.txt3.SetValue(result)

        if cal=="abs":
            if num=="2":
                result=str(abs(int(operator1,2)))
                self.txt3.SetValue(result)
            elif num=="10":
                result=str(abs(int(operator1)))
                self.txt3.SetValue(result)
            elif num=="16":
                result=str(abs(int(operator1,16)))
                self.txt3.SetValue(result)

        if cal=="divmod":
            if num=="2":
                result=str(divmod(int(operator1,2),int(operator2,2)))
                self.txt3.SetValue(result)
            elif num=="10":
                result=str(divmod(int(operator1),int(operator2)))
                self.txt3.SetValue(result)
            elif num=="16":
                result=str(divmod(int(operator1,16),int(operator2,16)))
                self.txt3.SetValue(result)

        if cal=="pow":
            if num=="2":
                result=str(pow(int(operator1,2),int(operator2,2)))
                self.txt3.SetValue(result)
            elif num=="10":
                result=str(pow(int(operator1),int(operator2)))
                self.txt3.SetValue(result)
            elif num=="16":
                result=str(pow(int(operator1,16),int(operator2,16)))
                self.txt3.SetValue(result)

        if cal=="round":
            if num=="2":
                result=str(round(int(operator1,2),int(operator2,2)))
                self.txt3.SetValue(result)
            elif num=="10":
                result=str(round(int(operator1),int(operator2)))
                self.txt3.SetValue(result)
            elif num=="16":
                result=str(round(int(operator1,16),int(operator2,16)))
                self.txt3.SetValue(result)

        if cal=="or":
            if num=="2":
                result=str(int(operator1,2)|int(operator2,2))
                self.txt3.SetValue(result)
            elif num=="10":
                result=str(string.atoi(operator1)|string.atoi(operator2))
                self.txt3.SetValue(result)
            elif num=="16":
                result=str(int(operator1,16)|int(operator2,16))
                self.txt3.SetValue(result)

        if cal=='rol':
            if num=="2":
                byte=int(operator1,2)
                count=string.atoi(operator2)
                result=str(byte << count | byte >> (32- count) & 0xFFFFFFFF)
                self.txt3.SetValue(result)
            if num=="10":
                byte=string.atoi(operator1)
                count=string.atoi(operator2)
                result=str(byte << count | byte >> (32- count) & 0xFFFFFFFF)
                self.txt3.SetValue(result)
            if num=="16":
                byte=int(operator1,16)
                count=string.atoi(operator2)
                result=str(byte << count | byte >> (32- count) & 0xFFFFFFFF)
                self.txt3.SetValue(result)

        if cal=='ror':
            if num=="2":
                byte=int(operator1,2)
                count=string.atoi(operator2)
                result=str(byte >> count | byte << (32- count) & 0xFFFFFFFF)
                self.txt3.SetValue(result)
            if num=="10":
                byte=string.atoi(operator1)
                count=string.atoi(operator2)
                result=str(byte >> count | byte << (32- count) & 0xFFFFFFFF)
                self.txt3.SetValue(result)
            if num=="16":
                byte=int(operator1,16)
                count=string.atoi(operator2)
                result=str(byte >> count | byte << (32- count) & 0xFFFFFFFF)
                self.txt3.SetValue(result)

        if cal=="and" :
            if num=="2":
                result=str(int(operator1,2) and int(operator2,2))
                self.txt3.SetValue(result)
            elif num=="10":
                result=str(string.atoi(operator1) and string.atoi(operator2))
                self.txt3.SetValue(result)
            elif num=="16":
                result=str(int(operator1,16) and int(operator2,16))
                self.txt3.SetValue(result)

        if cal=="add" :
            if num=="2":
                result=str(float(operator1,2)+float(operator2,2))
                self.txt3.SetValue(result)
            elif num=="10":
                result=str(float(operator1)+float(operator2))
                self.txt3.SetValue(result)
            elif num=="16":
                result=str(float(operator1,16)+float(operator2,16))
                self.txt3.SetValue(result)

        if cal=="sub" :
            if num=="2":
                result=str(float(operator1,2)-float(operator2,2))
                self.txt3.SetValue(result)
            elif num=="10":
                result=str(float(operator1)-float(operator2))
                self.txt3.SetValue(result)
            elif num=="16":
                result=str(float(operator1,16)-float(operator2,16))
                self.txt3.SetValue(result)

        if cal=="mul":
            if num=="2":
                result=str(float(operator1,2)*float(operator2,2))
                self.txt3.SetValue(result)
            elif num=="10":
                result=str(float(operator1)*float(operator2))
                self.txt3.SetValue(result)
            elif num=="16":
                result=str(float(operator1,16)*float(operator2,16))
                self.txt3.SetValue(result)

        if cal=="div":
            if num=="2":
                result=str(float(operator1,2)/float(operator2,2))
                self.txt3.SetValue(result)
            elif num=="10":
                result=str(float(operator1)/float(operator2))
                self.txt3.SetValue(result)
            elif num=="16":
                result=str(float(operator1,16)/float(operator2,16))
                self.txt3.SetValue(result)

        if cal=='bswap':
            if num=='2':
                a=int(operator1,2)
                b=(a * 0x0202020202 & 0x010884422010) % 1023
                result=str(bin(b)[2:].zfill(8))
                self.txt3.SetValue(result)
            if num=='10':
                a=int(operator1)
                b=(a * 0x0202020202 & 0x010884422010) % 1023
                result=str(bin(b)[2:].zfill(8))
                self.txt3.SetValue(result)
            if num=='16':
                a=int(operator1,16)
                b=(a * 0x0202020202 & 0x010884422010) % 1023
                result=str(bin(b)[2:].zfill(8))
                self.txt3.SetValue(result)

        if cal=='not':
            if num=='2':
                result=str(~int(operator1,2))
                self.txt3.SetValue(result)
            if num=='10':
                result=str(~int(operator1))
                self.txt3.SetValue(result)
            if num=='16':
                result=str(~int(operator1,16))
                self.txt3.SetValue(result)

        if cal=='shl':
            if num=='2':
                result=str(2*int(operator1,2)*int(operator2,2))
                self.txt3.SetValue(result)
            if num=='10':
                result=str(2*string.atoi(operator1)*string.atoi(operator2))
                self.txt3.SetValue(result)
            if num=='16':
                result=str(2*int(operator1,16)*int(operator2,16))
                self.txt3.SetValue(result)

        if cal=='shr':
            if num=='2':
                result=str(int(operator1,2)/(2*int(operator2,2)))
                self.txt3.SetValue(result)
            if num=='10':
                result=str(string.atoi(operator1)/(2*string.atoi(operator2)))
                self.txt3.SetValue(result)
            if num=='16':
                result=str(int(operator1,16)/(2*int(operator2,16)))
                self.txt3.SetValue(result)

        if cal=='neg':
            if num=='2':
                result=str(~int(operator1,2)+1)
                self.txt3.SetValue(result)
            if num=='10':
                result=str(~string.atoi(operator1)+1)
                self.txt3.SetValue(result)
            if num=='16':
                result=str(~int(operator1,16)+1)
                self.txt3.SetValue(result)

class FormPage1(Form1):
    def doLayout(self):
        for control, x, y, width, height in \
                [(self.loggerIn, 260, 20,400, 225),
		 (self.loggerOut, 260, 270, 400, 230),
                 (self.but1, 5, 30, 85, 25),
		 (self.but2, 140, 30, 85, 25),
		 (self.but3, 5, 70, 85, 25),
		 (self.but4, 140, 70, 85, 25),
		 (self.but5, 5, 110, 85, 25),
		 (self.but6, 140, 110, 85, 25),
		 (self.but7, 5, 150, 85, 25),
		 (self.but8, 140, 150, 85, 25),
		 (self.colorRadioBox, 2, 190, -1, -1),
         (self.choseary,5,340,240,-1),
         (self.txt1,140,390,-1,-1),
         (self.txt2,140,430,-1,-1),
         (self.txt3,140,470,-1,-1),
         (self.text1,10,390,-1,-1),
         (self.text2,10,430,-1,-1),
                    (self.but9,5,470,-1,-1)]:
            control.SetDimensions(x=x, y=y, width=width, height=height)


"""
Form2 is the Page of Crypto
"""

class Form2(wx.Panel):
    def __init__(self, *args, **kwargs):
        super(Form2, self).__init__(*args, **kwargs)
        self.createControls()
        self.doLayout()
        self.bindEvents()

    def createControls(self):
        sampleList = ['Base64','MD5',  'SHA1', 'SHA256', 'SHA512','CRC32',
                      'URL', 'Bacon',  'Morse','CaeSar','ROT']
        self.but1 = wx.Button(self, label="enc")
        self.but2 = wx.Button(self, label="dec")
        self.but3 = wx.Button(self, label="UpperALL")
        self.but4 = wx.Button(self, label="LowerAll")
        self.but5 = wx.Button(self, label="Upp<=>Low")
        self.but6 = wx.Button(self, label="String Reverse")
        self.but7 = wx.Button(self, label="Replace")
        self.loggerIn = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.loggerOut = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.listBox = wx.ListBox(self, -1, (20, 20), (80, 120), sampleList,
                wx.LB_SINGLE)
        self.listBox.SetSelection(3)
        self.r = wx.SpinCtrl(self, -1, "", (30, 20), (80, -1))
        self.r.SetValue(5)
        self.textshift= wx.StaticText(self, -1, "shift",
                (100, 10))
        self.text2= wx.StaticText(self, -1, "To",
                (100, 10))
        self.rep = wx.TextCtrl(self, -1, "",
                size=(175, -1))
        self.to = wx.TextCtrl(self, -1, "",
                size=(175, -1))

    def bindEvents(self):
        for control, event, handler in \
            [(self.but1,wx.EVT_BUTTON,self.enc),
                (self.but2,wx.EVT_BUTTON,self.dec),
                     (self.but3,wx.EVT_BUTTON,self.UpperAll),
                (self.but4,wx.EVT_BUTTON,self.LowerAll),
                (self.but5,wx.EVT_BUTTON,self.UppLow),
                (self.but6,wx.EVT_BUTTON,self.StrReverse),
                (self.but7,wx.EVT_BUTTON,self.Replace),]:
            control.Bind(event, handler)

    def Replace(self,event):
        str1=self.rep.GetValue()
        str2=self.to.GetValue()
        text=self.loggerIn.GetValue()
        self.loggerOut.SetValue(str(re.subn(str1, str2,text)[0]))

    def dec(self,event):
        if self.listBox.GetStringSelection()=='CaeSar':
            key = int(self.r.GetValue())
            e = self.loggerIn.GetValue()
            def convert(c, key, start = 'a', n = 26):
                a = ord(start)
                offset = ((ord(c) - a + key)%n)
                return chr(a + offset)
            def caesarEncode(s, key):
                o = ""
                for c in s:
                    if c.islower():
                        o+= convert(c, key, 'a')
                    elif c.isupper():
                        o+= convert(c, key, 'A')
                    else:
                        o+= c
                return o
            def caesarDecode(s, key):
                return caesarEncode(s, -key)
            d = caesarDecode(e, key)
            self.loggerOut.SetValue(d)

        if self.listBox.GetStringSelection()=='ROT':
            s=self.loggerIn.GetValue()
            OffSet=int(self.r.GetValue())
            def encodeCh(ch):
                f=lambda x: chr((ord(ch)-x+OffSet) % 26 + x)
                return f(97) if ch.islower() else (f(65) if ch.isupper() else ch)
            self.loggerOut.SetValue(''.join(encodeCh(c) for c in s))

        if self.listBox.GetStringSelection()=='Url':
            s=self.loggerIn.GetValue()
            list1=s.split('%')
            m=''
            for i in range(len(list1)-1):
                i += 1
                m+=chr(int(list1[i],16))

            self.loggerOut.SetValue(m)

        if self.listBox.GetStringSelection()=='Base64':
            self.loggerOut.SetValue(base64.decodestring(self.loggerIn.GetValue()))

        if self.listBox.GetStringSelection()=='Morse':
            __morse_code__ = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
            'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
            'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
            'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',

            '1': ['.----', '.-'], '2': ['..---', '..-'], '3': ['...--', '...-'], '4': ['....-', '....-'], '5': ['.....', '.'],
            '6': ['-....', '-....'], '7': ['--...', '-...'], '8': ['---..', '-..'], '9': ['----.', '-.'], '0': ['-----', '-'],

            '.': '.-.-.-', ':': '---...', ',': '--..--', ';': '-.-.-.', '?': '..--..', '=': '-...-', "'": '.---.',
            '/': '-..-.', '!': '-.-.--', '-': '-....-', '_': '..--.-', '"': '.-..-.', '(': '-.--.', ')': '-.--.-',
            '$': '...-..-', '&': '.-...', '@': '.--.-.'
            }
            __de_morse_code__ = {}

            for c in __morse_code__:
                if type(__morse_code__[c]) == list:
                    for _c in __morse_code__[c]:
                        __de_morse_code__[_c] = c
                    continue
                __de_morse_code__[__morse_code__[c]] = c

            def morse_decode(data):
                codes = data.split("/")
                result = []
                for code in codes:
                    if code:
                        result.append(__de_morse_code__[code])
                return "".join(result)
            result = morse_decode(self.loggerIn.GetValue())
            self.loggerOut.SetValue(result)

        if self.listBox.GetStringSelection()=='Bacon':
            def bacon2text(bacon):
                bacondict = {}
                plaintext = ""
                bacon = bacon.lower()
                bacon = re.sub("[\W\d]", "", bacon.strip())
                for i in xrange(0,26):
                    tmp = bin(i)[2:].zfill(5)
                    tmp = tmp.replace('0', 'a')
                    tmp = tmp.replace('1', 'b')
                    bacondict[tmp] = chr(65+i)

                for i in xrange(0, len(bacon)/5):
                    plaintext = plaintext + bacondict.get(bacon[i*5:i*5+5], ' ')
                return plaintext
            self.loggerOut.SetValue(bacon2text(self.loggerIn.GetValue()))

    def enc(self,event):
        if self.listBox.GetStringSelection()=='MD5':
            self.loggerOut.SetValue(hashlib.new("md5", self.loggerIn.GetValue().encode()).hexdigest())

        if self.listBox.GetStringSelection()=='CRC32':
            self.loggerOut.SetValue(str(binascii.crc32(self.loggerIn.GetValue().encode()) & 0xffffffff))

        if self.listBox.GetStringSelection()=='SHA1':
            self.loggerOut.SetValue(hashlib.new("sha1", self.loggerIn.GetValue().encode()).hexdigest())

        if self.listBox.GetStringSelection()=='SHA256':
            self.loggerOut.SetValue(hashlib.new("sha256", self.loggerIn.GetValue().encode()).hexdigest())

        if self.listBox.GetStringSelection()=='SHA512':
            self.loggerOut.SetValue(hashlib.new("sha512", self.loggerIn.GetValue().encode()).hexdigest())

        if self.listBox.GetStringSelection()=='Base64':
            self.loggerOut.SetValue(base64.encodestring(self.loggerIn.GetValue()))

        if self.listBox.GetStringSelection()=='URL':
            n=0
            strhex=''
            str1=self.loggerIn.GetValue()
            list1=list(str1)
            while n< len(list1):
                strhex+="%"+hex(ord(list1[n])).replace("0x",'')
                n+=1
            self.loggerOut.SetValue(strhex)

        if self.listBox.GetStringSelection()=='Morse':
            __morse_code__ = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
            'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
            'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
            'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',

            '1': ['.----', '.-'], '2': ['..---', '..-'], '3': ['...--', '...-'], '4': ['....-', '....-'], '5': ['.....', '.'],
            '6': ['-....', '-....'], '7': ['--...', '-...'], '8': ['---..', '-..'], '9': ['----.', '-.'], '0': ['-----', '-'],

            '.': '.-.-.-', ':': '---...', ',': '--..--', ';': '-.-.-.', '?': '..--..', '=': '-...-', "'": '.---.',
            '/': '-..-.', '!': '-.-.--', '-': '-....-', '_': '..--.-', '"': '.-..-.', '(': '-.--.', ')': '-.--.-',
            '$': '...-..-', '&': '.-...', '@': '.--.-.'
            }

            __de_morse_code__ = {}

            for c in __morse_code__:
                if type(__morse_code__[c]) == list:
                    for _c in __morse_code__[c]:
                        __de_morse_code__[_c] = c
                    continue
                __de_morse_code__[__morse_code__[c]] = c

            def morse_encode(data):
                data = data.upper()
                encoded = []
                for c in data:
                    if type(__morse_code__[c]) == list:
                        encoded.append(__morse_code__[c][0])
                    else:
                        encoded.append(__morse_code__[c])
                return "/".join(encoded)

            result = morse_encode(self.loggerIn.GetValue())
            self.loggerOut.SetValue(result)

        if self.listBox.GetStringSelection()=='CaeSar':
            key = int(self.r.GetValue())
            s = self.loggerIn.GetValue()
            def convert(c, key, start = 'a', n = 26):
                a = ord(start)
                offset = ((ord(c) - a + key)%n)
                return chr(a + offset)
            def caesarEncode(s, key):
                o = ""
                for c in s:
                    if c.islower():
                        o+= convert(c, key, 'a')
                    elif c.isupper():
                        o+= convert(c, key, 'A')
                    else:
                        o+= c
                return o
            e = caesarEncode(s, key)
            self.loggerOut.SetValue(e)

        if self.listBox.GetStringSelection()=='ROT':
            s=self.loggerIn.GetValue()
            OffSet=int(self.r.GetValue())
            def encodeCh(ch):
                f=lambda x: chr((ord(ch)-x+OffSet) % 26 + x)
                return f(97) if ch.islower() else (f(65) if ch.isupper() else ch)
            self.loggerOut.SetValue(''.join(encodeCh(c) for c in s))

        if self.listBox.GetStringSelection()=='Bacon':
            def generate_dict():
                bacon_dict = {}
                for i in xrange(0, 26):
                    tmp = bin(i)[2:].zfill(5)
                    tmp = tmp.replace('0', 'a')
                    tmp = tmp.replace('1', 'b')
                    bacon_dict[tmp] = chr(65 + i)
                return bacon_dict
            def encode(words, bacon_dict):
                cipher = ''
                bacon_dict = {v: k for k, v in bacon_dict.items()}
                words = normalize('NFKD', words).encode('ascii', 'ignore')
                words = words.upper()
                words = re.sub(r'[^A-Z]+', '', words)

                for i in words:
                        cipher += bacon_dict.get(i).upper()+' '
                return cipher
            bacon_dict = generate_dict()
            self.loggerOut.SetValue(encode(self.loggerIn.GetValue(), bacon_dict))

    def str2md5(self,event):
        str1=self.listBox.GetSelection()
        str=self.loggerIn.GetValue()
        md5_result=hashlib.md5(str)
        self.loggerOut.SetValue(md5_result)

    def UpperAll(self,event):
        self.loggerOut.SetValue(str.upper(self.loggerIn.GetValue().encode()))

    def LowerAll(self,event):
        self.loggerOut.SetValue(str.lower(self.loggerIn.GetValue().encode()))

    def UppLow(self,event):
        s=''
        low='abcdefghijklmnopqrstuvwxyz'
        up='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for c in self.loggerIn.GetValue().encode():
            if c in low:
                s+=c.upper()
            elif c in up:
                s+=c.lower()
            else:
                s+=c
        self.loggerOut.SetValue(s)

    def StrReverse(self,event):
        self.loggerOut.SetValue(self.loggerIn.GetValue().encode()[::-1])

    def doLayout(self):
        raise NotImplementedError

class FormPage2(Form2):
    def doLayout(self):
        for control, x, y, width, height in \
                [(self.loggerIn, 260, 20, 400, 225),
		 (self.loggerOut, 260, 270, 400, 230),
		 (self.but1, 5, 240, -1, -1),
		 (self.but2, 120, 240, -1, -1),
         (self.but7,5,290,-1,-1),
         (self.listBox,5,20,200,-1),
         (self.r,85,200,-1,-1),
         (self.textshift,15,200,60,-1),
         (self.rep,5,330,200,25),
         (self.text2,5,360,-1,-1),
         (self.to,5,390,200,25),
                    (self.but3, 5, 435, 98, -1),
                    (self.but4, 110, 435, 98, -1),
                    (self.but5, 5, 475, 98, -1),
                    (self.but6, 110, 475, 98, -1),
                    ]:
            control.SetDimensions(x=x, y=y, width=width, height=height)


"""
Form3 is the Page of Instruction
"""

class Form3(wx.Panel):
    def __init__(self, *args, **kwargs):
        super(Form3, self).__init__(*args, **kwargs)
        self.createControls()
        self.doLayout()
        self.bindEvents()

    def createControls(self):
        platlist=['x86','arm','mips','powerpc']
        self.platlist = wx.ListBox(self, -1, (20, 20), (80, 120), platlist,
                wx.LB_SINGLE)
        self.platlist.SetSelection(2)
        self.instruction = wx.TextCtrl(self, -1, "",
                size=(175, -1))
        self.result = wx.TextCtrl(self, -1, "",
                size=(175, -1))
        self.but1 = wx.Button(self, label="Search")

    def doLayout(self):
        raise NotImplementedError

    def SearchInstruction(self,event):
        ins=self.instruction.GetValue()
        plat=self.platlist.GetStringSelection()
        cx = sqlite3.connect("instruction.sqlite")
        cu = cx.cursor()
        cu.execute("select function from " + plat + " where instruction = '" + ins + "'")
        a=cu.fetchall()
        str = a[0][0]
        self.result.SetValue(str)

    def bindEvents(self):
        for control, event, handler in \
            [(self.but1,wx.EVT_BUTTON,self.SearchInstruction)
            ]:
            control.Bind(event, handler)

class FormPage3(Form3):
    def doLayout(self):
        for control, x, y, width, height in \
            [(self.platlist,5,20,-1,90),
                (self.instruction,5,130,130,-1),
                (self.but1,5,170,-1,-1),
                (self.result,160,20,480,470)]:
            control.SetDimensions(x=x, y=y, width=width, height=height)



"""
Form4 is the Page of Note
"""

class Form4(wx.Panel):
    def __init__(self, *args, **kwargs):
        super(Form4, self).__init__(*args, **kwargs)
        self.createControls()
        self.doLayout()
        self.bindevents()

    def createControls(self):
        self.tnote = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.but1 = wx.Button(self, label="SaveToText")
        self.but2 = wx.Button(self, label="ClearAll")

    def doLayout(self):
        raise NotImplementedError

    def savetext(self,event):
        str1=self.tnote.GetValue()
        x=time.localtime(time.time())
        a=str(time.strftime('%Y-%m-%d %H:%M:%S',x))
        f=open(a,'w')
        f.write(str1+'\n')
        f.close()

    def cleartext(self,event):
        self.tnote.Clear()

    def bindevents(self):
        for control, event, handler in \
            [(self.but1, wx.EVT_BUTTON, self.savetext),
                (self.but2, wx.EVT_BUTTON, self.cleartext)
            ]:
                    control.Bind(event, handler)

class FormPage4(Form4):
    def doLayout(self):
        for control, x, y, width, height in \
            [(self.tnote,20,20,630,430),
                (self.but1,430,490,-1,-1),
                (self.but2,560,490,-1,-1)]:
            control.SetDimensions(x=x, y=y, width=width, height=height)



"""
Main Frame
"""


class FrameWithForms(wx.Frame):
    def __init__(self, *args, **kwargs):
        #super(FrameWithForms, self).__init__(*args, **kwargs)
	#self.SetClientSize(notebook.GetBestSize())	

	wx.Frame.__init__(self, None, -1, 'BinHelper 1.0.0 by Zing',size=(690, 590))

	notebook = wx.Notebook(self)
        form1 = FormPage1(notebook)
        form2 = FormPage2(notebook)
	form3 = FormPage3(notebook)
	form4 = FormPage4(notebook)
        #form5 = Form1Page5(notebook)

	notebook.AddPage(form1, 'Crack',True)
        notebook.AddPage(form2, 'Crypto',True)
	notebook.AddPage(form3, 'Instructions',True)
       	notebook.AddPage(form4, 'TmpNote',True)
	#notebook.AddPage(form5, 'about',True)

        


if __name__ == '__main__':
    app = wx.App(0)
    frame = FrameWithForms(None, title='BinHelper 1.0 by Zing')
    frame.Show()
    app.MainLoop()


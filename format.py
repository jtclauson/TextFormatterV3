import logging
import re
from dragonmapper import transcriptions
from dragonmapper import hanzi

class Formatted:
    def __init__(self, filename, text):
        self.filename = filename
        self.text = text

def Format(input):
    lines = input.text.split("\n")
    filename = "formatted/"+input.filename+".txt"
    origin = input.origin

    formattedLines = []
    
    if origin == "imiwa":
        formattedLines = forImiwa(lines)
    elif origin == "pleco":
        formattedLines = forPleco(lines, filename)
    elif origin == "misc-chinese":
        formattedLines = forMiscChinese(lines, filename)
    
    f = Formatted(filename, formattedLines)
    # logging.debug('f -- '+f)
    # logging.debug('filename -- '+filename)
    # logging.debug('formattedLines -- '+formattedLines)
    print('f -- '+f)
    print('filename -- '+filename)
    print('formattedLines -- '+formattedLines)
    return f


def formatEnglish(rawString):
    chunks = re.split('[0-9]',rawString)
    newEntry = ""
    for i, chunk in enumerate(chunks):
        if chunk:
            if i==len(chunks)-1:
                newEntry=newEntry+"・"+chunk
            else:
                newEntry=newEntry+"・"+chunk+"<br>"
    return newEntry
   
def forImiwa(lines):
    # newFile = open(filename, "w", encoding="utf8")
    formattedText = []

    for i in range (len(lines)):
        entry = lines[i]
        kanji = ""
        yomi = ""
        meaning = ""
        if i%2==0:
            if "[" not in entry:
                kanji = entry[:-1]
                yomi = "No Kanji"
                meaning = lines[i+1]#[:-1]
                # newFile.write("\""+meaning+"\"" + "; " +kanji+ "; "+yomi+"\n")
                formattedText.append("\""+meaning+"\"" + "; " +kanji+ "; "+yomi+"\n")
            else:
                spl = entry.split("[")
                kanji = spl[0][:-1]
                yomi = spl[1][:-1]
                meaning = lines[i+1]#[:-1]
                # newFile.write("\""+meaning+"\"" + "; " +kanji+ "; "+yomi+"\n")
                formattedText.append("\""+meaning+"\"" + "; " +kanji+ "; "+yomi+"\n")
               
    # newFile.close()    
    return formattedText
   
def forPleco(lines, filename):
    newFile = open(filename, "w", encoding="utf8")

    for i in range (len(lines)):
        if i%2==0:
            entry = lines[i].split("\t")
            kanji = entry[0]
            pinyin = entry[1]
            dufa = transcriptions.to_zhuyin(pinyin)
            rawString = entry[2]#[:-1]
            meaning=formatEnglish(rawString)
            newFile.write("\""+meaning+"\"" + "; " +kanji+ "; "+dufa+"\n")
               
    newFile.close()

def forTextScanner(lines, filename):
    newFile = open(filename, "w", encoding="utf8")

    for i in range (len(lines)):
        if i%2==0:
            entry = lines[i].split("\t")
            kanji = entry[0]
            dufa = hanzi.to_zhuyin(kanji)
            meaning=entry[1]
            newFile.write("\""+meaning+"\"" + "; " +kanji+ "; "+dufa+"\n")
               
    newFile.close()
    
def forMiscChinese(lines, filename):
    newFile = open(filename, "w", encoding="utf8")

    for i in range (len(lines)):
        if i%2==0:
            line = lines[i].strip()
            nextLine = lines[i+1].strip()
        
            kanji = line
            imi = nextLine
            yomi = hanzi.to_zhuyin(kanji)
            newFile.write("\""+imi+"\"" + "; " +kanji+ "; "+yomi+"\n")
               
    newFile.close()
import re
from dragonmapper import transcriptions
from dragonmapper import hanzi
import datetime

def Format(text, filename, origin):
    try:
        lines = text.split("\n")
        inputFileName = ""
        if not filename:
            inputFileName = datetime.datetime.now().strftime("%Y-%m-%d")+"_"+origin
        else:
            inputFileName = filename
        filename = inputFileName+".txt"

        formattedLines = []
        
        if origin == "Imiwa":
            formattedLines = forImiwa(lines)
        elif origin == "Pleco":
            formattedLines = forPleco(lines)
        elif origin == "Misc-Chinese":
            formattedLines = forMiscChinese(lines)
    except:
        finalFormatted = {"error": "Error in converting input text"}
        return finalFormatted
    
    finalFormatted = {
        "error": "",
        "filename": filename,
        "origin": origin,
        "text": formattedLines

    }
    return finalFormatted


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
                meaning = lines[i+1]
                formattedText.append("\""+meaning+"\"" + "; " +kanji+ "; "+yomi+"\n")
            else:
                spl = entry.split("[")
                kanji = spl[0][:-1]
                yomi = spl[1][:-2]
                meaning = lines[i+1].strip()
                formattedText.append("\""+meaning+"\"" + "; " +kanji+ "; "+yomi+"\n")
    return formattedText
   
def forPleco(lines):
    formattedText = []

    for i in range (len(lines)):
        if i%2==0:
            entry = lines[i].split("\t")
            kanji = entry[0]
            pinyin = entry[1]
            dufa = transcriptions.to_zhuyin(pinyin)
            rawString = entry[2]
            meaning=formatEnglish(rawString).strip()
            formattedText.append("\""+meaning+"\"" + "; " +kanji+ "; "+dufa+"\n")
    return formattedText

def forMiscChinese(lines):
    formattedText = []

    for i in range (len(lines)):
        if i%2==0:
            line = lines[i].strip()
            nextLine = lines[i+1].strip()
        
            kanji = line
            imi = nextLine
            yomi = hanzi.to_zhuyin(kanji)
            formattedText.append("\""+imi+"\"" + "; " +kanji+ "; "+yomi+"\n")
    return formattedText
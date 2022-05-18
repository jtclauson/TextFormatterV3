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
        filename = "app/formatted/"+inputFileName+".txt"

        formattedLines = []
        
        if origin == "Imiwa":
            formattedLines = forImiwa(lines, filename)
        elif origin == "Pleco":
            formattedLines = forPleco(lines, filename)
        elif origin == "Misc-Chinese":
            formattedLines = forMiscChinese(lines, filename)
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
   
def forImiwa(lines, filename):
    newFile = open(filename, "w", encoding="utf8")
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
                newFile.write("\""+meaning+"\"" + "; " +kanji+ "; "+yomi+"\n")
                formattedText.append("\""+meaning+"\"" + "; " +kanji+ "; "+yomi+"\n")
            else:
                spl = entry.split("[")
                kanji = spl[0][:-1]
                yomi = spl[1][:-2]
                meaning = lines[i+1].strip()
                newFile.write("\""+meaning+"\"" + "; " +kanji+ "; "+yomi+"\n")
                formattedText.append("\""+meaning+"\"" + "; " +kanji+ "; "+yomi+"\n")
               
    newFile.close()    
    return formattedText
   
def forPleco(lines, filename):
    newFile = open(filename, "w", encoding="utf8")
    formattedText = []

    for i in range (len(lines)):
        if i%2==0:
            entry = lines[i].split("\t")
            kanji = entry[0]
            pinyin = entry[1]
            dufa = transcriptions.to_zhuyin(pinyin)
            rawString = entry[2]
            meaning=formatEnglish(rawString).strip()
            newFile.write("\""+meaning+"\"" + "; " +kanji+ "; "+dufa+"\n")
            formattedText.append("\""+meaning+"\"" + "; " +kanji+ "; "+dufa+"\n")
               
    newFile.close()
    return formattedText

def forMiscChinese(lines, filename):
    newFile = open(filename, "w", encoding="utf8")
    formattedText = []

    for i in range (len(lines)):
        if i%2==0:
            line = lines[i].strip()
            nextLine = lines[i+1].strip()
        
            kanji = line
            imi = nextLine
            yomi = hanzi.to_zhuyin(kanji)
            newFile.write("\""+imi+"\"" + "; " +kanji+ "; "+yomi+"\n")
            formattedText.append("\""+imi+"\"" + "; " +kanji+ "; "+yomi+"\n")
               
    newFile.close()
    return formattedText
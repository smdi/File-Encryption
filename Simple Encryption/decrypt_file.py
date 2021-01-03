




from library import  getEncodedData, decodeDictionary
import  re




def decodeWord(dataEncoded):
    msg = ""
    i = 0

    dictData = decodeDictionary()
    dictKeys = list(dictData.keys())
    dictValues = list(dictData.values())
    while i < len(dataEncoded):
        string = dataEncoded[i:i + 16]
        i += 16
        j = 0
        for _ in dictValues:
            match = re.fullmatch(dictValues[j], string)
            if match != None:
                msg = msg + chr(dictKeys[j])
            j += 1
    return msg


def decoding(filename):
    msg = ""
    print("started encoding " + filename)
    i = 0

    dataEncoded = getEncodedData(filename)
    dictData = decodeDictionary()
    dictKeys = list(dictData.keys())
    dictValues = list(dictData.values())
    while i < len(dataEncoded):
        string = dataEncoded[i:i + 16]
        i += 16
        j = 0
        for _ in dictValues:
            match = re.fullmatch(dictValues[j], string)
            if match != None:
                msg = msg + chr(dictKeys[j])
            j += 1
    with open(filename + "_decodedFile.txt", 'w') as decodeMsgWritter:
        decodeMsgWritter.write(str(msg))
    print("completed encoding " + filename)





# decoding("input.txt")

# print(decodeWord(""))












from library import  getEncodedData, decodeDictionary, getSumOfValueOfKey
import  re




def decodeWord(dataEncoded):
    msg = ""
    i = 0
    sum = getSumOfValueOfKey()
    dictData = decodeDictionary()
    dictKeys = list(dictData.keys())
    dictValues = list(dictData.values())
    while i < len(dataEncoded):
        string = dataEncoded[i:i + 16]
        string = int(string) - int(sum)
        string = str(string)

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
    sum = getSumOfValueOfKey()
    dataEncoded = getEncodedData(filename)
    dictData = decodeDictionary()
    dictKeys = list(dictData.keys())
    dictValues = list(dictData.values())
    while i < len(dataEncoded):
        string = dataEncoded[i:i + 16]
        string = int(string) - int(sum)
        string = str(string)

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

print(decodeWord("90011174332450199000218333245009900021834324500990001172832568099000118283425009"))







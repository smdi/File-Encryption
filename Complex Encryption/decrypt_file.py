




from library import  getEncodedData, decodeDictionary, getSumOfValueOfKey, rotateString
import  re




def decodeWord(dataEncoded):
    msg = ""
    sum = getSumOfValueOfKey()
    dictData = decodeDictionary()
    dictKeys = list(dictData.keys())
    dictValues = list(dictData.values())
    try:
        for x in range(16, len(dataEncoded) + 16, 16):
            string = dataEncoded[x-16:x]
            string = int(string) - int(sum)
            string = rotateString(string)
            string = str(string)
            j = 0
            for _ in dictValues:
                match = re.fullmatch(dictValues[j], string)
                if match != None:
                    msg = msg + chr(dictKeys[j])
                j += 1
    except Exception as e:
        print(e)


    return msg


def decoding(filename):
    msg = ""
    print("started encoding " + filename)
    sum = getSumOfValueOfKey()
    dataEncoded = getEncodedData(filename)
    dictData = decodeDictionary()
    dictKeys = list(dictData.keys())
    dictValues = list(dictData.values())
    try:
        for x in range(16, len(dataEncoded) + 16, 16):
            string = dataEncoded[x - 16:x]
            string = int(string) - int(sum)
            string = rotateString(string)
            string = str(string)
            j = 0
            for _ in dictValues:
                match = re.fullmatch(dictValues[j], string)
                if match != None:
                    msg = msg + chr(dictKeys[j])
                j += 1
    except Exception as e:
        print(e)

    with open(filename + "_decodedFile.txt", 'w') as decodeMsgWritter:
        decodeMsgWritter.write(str(msg))
    print("completed encoding " + filename)





# decoding("input.txt")

print(decodeWord("91001177932460099000117984255009900011808425500990412172832450099000527284245009"))







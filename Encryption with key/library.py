import ast



def getPatternDictionary():
    with open('patterns_of_characters.py', 'r') as patternData:
        patterns = ast.literal_eval(patternData.read())
    return patterns


def getZeroCodesDictionary():
    with open('repeated_count.py', 'r') as codeData:
        codes_dict = ast.literal_eval(codeData.read())
    return codes_dict


def setZeroCodesDictionary(codes_dict):
    with open('repeated_count.py', 'w') as codeData:
        codeData.write(str(codes_dict))


def get3DigitCodes():
    with open('3DigitCodes.txt', 'r') as digitCodeReader:
        digitCodeData = digitCodeReader.readlines()
    return digitCodeData


def setDatatoEncodedFile(encoded_single_char, filename):
    with open(filename+'_encodedFile.txt', 'a') as encodingFile:
        encodingFile.write(encoded_single_char)


def getEncodedData(filename):
    with open(filename+'_encodedFile.txt', 'r') as encodedCodeReader:
        encodedData = encodedCodeReader.read()
    return encodedData


def decodeDictionary():
    with open('decoding_patterns.py', 'r') as decodeDictionaryReaader:
        decodingData = decodeDictionaryReaader.read()
        decodingDictionaryData = ast.literal_eval(decodingData)
    return decodingDictionaryData


def getSecretKeyEncodedData():
    with open('secret.txt_encodedFile.txt', 'r') as secret:
        data = secret.read()
    return data


def getSumOfValueOfKey():
    res = 0
    key = getSecretKeyEncodedData()
    for x in range(16, len(key)+16, 16):
        data = key[x-16:x]
        res = res + int(data)
    return res


def rotateMatrix(c):
    import numpy as np
    c = str(c)
    a = [ [c[0], c[1], c[2], c[3]], [c[4], c[5], c[6], c[7]], [c[8], c[9], c[10], c[11]], [c[12], c[13], c[14], c[15]]]
    res = np.rot90(a, 2)
    return res


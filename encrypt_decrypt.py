import ast
import re


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


def getEncodedCharacter(singleChar, codes_of_chars, patternCodes, digit3codes):
    encoded_single_char = ""

    dict_key_usage = codes_of_chars[ord(singleChar)]

    if dict_key_usage == 8:
        dict_key_usage = 0
        codes_of_chars[ord(singleChar)] = dict_key_usage


    dict_pattern = patternCodes[ord(singleChar)]


    codes_of_chars[ord(singleChar)] = codes_of_chars[ord(singleChar)] + 1
    digit3code_singleChar = digit3codes[dict_key_usage]
    if singleChar.isupper():
        encoded_single_char = dict_pattern.format(digit3code_singleChar[0], digit3code_singleChar[1],
                                                  digit3code_singleChar[2], '1')
    else:
        encoded_single_char = dict_pattern.format(digit3code_singleChar[0], digit3code_singleChar[1],
                                                  digit3code_singleChar[2], '0')

    return encoded_single_char


def encodeFile(filename):

    print("started encoding " + filename)
    with open(filename, 'r') as inputfile:
        singleLine = inputfile.readline()
        patternCodes = getPatternDictionary()
        codes_of_chars = getZeroCodesDictionary()
        digit3codes = get3DigitCodes()
        while singleLine:
            enocoded_data = ""
            for singleChar in singleLine:
                if ord(singleChar) in patternCodes:
                    enocoded_data = enocoded_data + getEncodedCharacter(singleChar, codes_of_chars, patternCodes, digit3codes)

                else:
                    print("char doesnot exist in patterncodes" + ord(singleChar))

            print(enocoded_data)
            setDatatoEncodedFile(enocoded_data, filename)
            singleLine = inputfile.readline()

    setZeroCodesDictionary(codes_of_chars)
    print("completed encoding " + filename)


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
    with open(filename + "_decodedFile.txt", 'a') as decodeMsgWritter:
        decodeMsgWritter.write(str(msg))
    print("completed encoding " + filename)




enc = 0

if enc == 1:
    encodeFile('input.txt')
else :
    decoding('input.txt')










from  library import getPatternDictionary, getZeroCodesDictionary, get3DigitCodes,\
    setDatatoEncodedFile, setZeroCodesDictionary, getSecretKeyEncodedData, getSumOfValueOfKey, rotateMatrix



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


def enocdeWord(word):
    enocoded_data = ""
    sum = getSumOfValueOfKey()
    patternCodes = getPatternDictionary()
    codes_of_chars = getZeroCodesDictionary()
    digit3codes = get3DigitCodes()
    for singleChar in word:
        if ord(singleChar) in patternCodes:
            encSC = getEncodedCharacter(singleChar, codes_of_chars, patternCodes, digit3codes)

            encSC = int(encSC) + int(sum)
            enocoded_data = enocoded_data + str(encSC)
        else:
            print("char doesnot exist in patterncodes" + ord(singleChar))

    setZeroCodesDictionary(codes_of_chars)
    return enocoded_data


def encodeFile(filename):
    print("started encoding " + filename)
    with open(filename, 'r') as inputfile:
        sum = getSumOfValueOfKey()
        singleLine = inputfile.readline()
        patternCodes = getPatternDictionary()
        codes_of_chars = getZeroCodesDictionary()
        digit3codes = get3DigitCodes()
        while singleLine:
            enocoded_data = ""
            for singleChar in singleLine:
                if ord(singleChar) in patternCodes:
                    encSC = getEncodedCharacter(singleChar, codes_of_chars, patternCodes, digit3codes)
                    encSC = int(encSC) + int(sum)
                    enocoded_data = enocoded_data + str(encSC)

                else:
                    print("char doesnot exist in patterncodes" + ord(singleChar))

            print(enocoded_data)
            setDatatoEncodedFile(enocoded_data, filename)
            singleLine = inputfile.readline()

    setZeroCodesDictionary(codes_of_chars)
    print("completed encoding " + filename)







# encodeFile('input.txt')
# encodeFile('secret.txt')
#
# print(enocdeWord("Apple"))
print(enocdeWord("Apple"))





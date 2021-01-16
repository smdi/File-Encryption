







small = [1260, 2250, 3240, 4230, 5220, 6210, 7200, 8190, 9180, 4170, 6160, 8150, 9140, 2130, 5120, 4110, 3100, 1890, 1980, 2070, 2160, 2230, 2340, 2430, 2520, 2610]
large = [1261, 2251, 3241, 4231, 5221, 6211, 7201, 8191, 9181, 4171, 6161, 8151, 9141, 2131, 5121, 4111, 3101, 1891, 1981, 2071, 2161, 2231, 2341, 2431, 2521, 2611]
number = [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999, 1100]




def enocdeWord(word):
    enocoded_data = ""
    for eachletter in word:
        if eachletter.isalpha() and eachletter.islower():
            enocoded_data += str( small[ord(eachletter) % 97] )
        if eachletter.isalpha() and eachletter.isupper():
            enocoded_data += str( large[ord(eachletter) % 65])
        if eachletter.isnumeric():
            enocoded_data += str( number[ord(eachletter) % 48]  )

    return enocoded_data






# print(enocdeWord("Apple"))





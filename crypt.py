import string
#JaAbDk1QlerxhNo8pLqS2Q==C52TB!9DC6! T6BTC!TDB2Tx T6B9TC!Tz!00D 6zxC2TC29202CAHTC!TC52T0x6
#TBCxC6! WTq52T 2GCT82HT6BTJSnij8GNMQUx06N++TLehaxw==
def countOccurrences(strn):
    print("Prova")
    charDict = {}
    for ch in string.printable:
        charDict[ch] = 0
    for ch in strn:
        charDict[ch] += 1
    return sorted(charDict, key=charDict.get, reverse=True)

decipherDict = {
    'T' : ' ',
    '2' : 'e', #ok
    'C' : 't', #ok
    '6' : 'i', #ok
    'D' : 'u', #ok
    '!' : 'o', #ok
    'B' : 's', #ok
    ' ' : 'n', #ok
    '0' : 'm', #ok
    'x' : 'a', #ok
    '5' : 'h', #ok
    'A' : 'r', #ok
    'z' : 'c', #ok
    'H' : 'y', #ok
    '9' : 'l', #ok
    'W' : ',', #ok
    'q' : 't', #ok 
    'G' : 'x', #ok
    '8' : 'k', #ok
    'J' : 'J', #a or A or 0 or 1
    'S' : 'S', #z or 
}

def mapString(strn):
    finalString = ""
    for ch in strn:
        if(ch in decipherDict):
            finalString += decipherDict[ch]
        else:
            finalString += ch
    return finalString
        
def countUnique(strn):
    uniques = set(strn)
    print("UNIQUE OCCURENCES: " + str(len(uniques)))

    
def decipher(strn, modn):
    finalString = ""
    for ch in strn: 
        finalString += (chr((65 + (ord(ch) + modn) % 26)))
    return finalString

def skipDecipher(strn, skipSize):
    finalString = ""
    counter = 0
    while len(finalString) < len(strn):
        finalString += strn[counter]
        counter = (counter + skipSize + 1) % len(strn)
    return finalString



def main():
    print("bruh")
    strn = "C52TB!9DC6! T6BTC!TDB2Tx T6B9TC!Tz!00D 6zxC2TC29202CAHTC!TC52T0x6 TBCxC6! WTq52T 2GCT82HT6BTJS"
    print(countOccurrences("C52TB!9DC6! T6BTC!TDB2Tx T6B9TC!Tz!00D 6zxC2TC29202CAHTC!TC52T0x6 TBCxC6! WTq52T 2GCT82HT6BTJS"))
    #print(decipher(strn, 15))
    print(mapString(strn))
    countUnique(strn)
    
    strn2 = "Ttoleenstidhyw sst. s1e nt  a k 2 ilhotiTep3psoefhnhya4r a  a e s5itdiNts As6oo ma hlEw7r aapciaSo8idlglops r"
    print(skipDecipher(strn2, 10))
    
if __name__ == '__main__':
    main()
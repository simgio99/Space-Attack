import string
import base64


def base64decode(str):
    return base64.decode(str)

# Function that computes the sorted dictionary of the most frequent characters in a string. We used it to execute the frequency analysis
def countOccurrences(strn):
    charDict = {}
    for ch in string.printable:
        charDict[ch] = 0
    for ch in strn:
        charDict[ch] += 1
    return sorted(charDict, key=charDict.get, reverse=True)


# Function that returns the string obtained as translation of the argument string with the specified decipher dictionary
# We created it while working for the level 3 of the challenge, in order to simplify its resolution
def mapString(strn, decipherDict):
    finalString = ""
    for ch in strn:
        if(ch in decipherDict):
            finalString += decipherDict[ch]
        else:
            finalString += ch
    return finalString

#Function that returns the count of the unique occurences of characters in the given string
def countUnique(strn):
    uniques = set(strn)
    print("UNIQUE OCCURENCES: " + str(len(uniques)))

#Function that implements a decipher method based on modulo arithmetic with the given string
# This was our first attempt for level 4
def modDecipher(strn, modn):
    finalString = ""
    for ch in strn: 
        finalString += (chr((65 + (ord(ch) + modn) % 26)))
    return finalString

#Function that implements the skip-n decryption algorithm with the given string and skip-size
# This function allowed us to decrypt level 4
def skipDecipher(strn, skipSize):
    finalString = ""
    counter = 0
    while len(finalString) < len(strn):
        finalString += strn[counter]
        counter = (counter + skipSize + 1) % len(strn)
    return finalString



def main():
    decipherDict = {
    'T' : ' ', #ok
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
    'J' : '1', #a or A or 0 or 1
    'S' : '0', #z or 
}
    
    # Test script we used to decrypt level 3
    strn = "C52TB!9DC6! T6BTC!TDB2Tx T6B9TC!Tz!00D 6zxC2TC29202CAHTC!TC52T0x6 TBCxC6! WTq52T 2GCT82HT6BTJS"
    print(countOccurrences("C52TB!9DC6! T6BTC!TDB2Tx T6B9TC!Tz!00D 6zxC2TC29202CAHTC!TC52T0x6 TBCxC6! WTq52T 2GCT82HT6BTJS"))
    print(mapString(strn, decipherDict))
    countUnique(strn)
    
    # Test script we used to decrypt level 4
    strn2 = "Ttoleenstidhyw sst. s1e nt  a k 2 ilhotiTep3psoefhnhya4r a  a e s5itdiNts As6oo ma hlEw7r aapciaSo8idlglops r"
    print(skipDecipher(strn2, 10))
    
if __name__ == '__main__':
    main()

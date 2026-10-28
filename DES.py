from DESFunction import *
import sys

def openFile(pFileName):
    try:
        with open(pFileName, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("Error: File not found.")
        return None

def blockPadding(pText):
    blockSize = 8 # 8 bytes or 64 bits for DES
    finalBlockLen = len(pText) % blockSize
    paddingLen = blockSize - finalBlockLen 

    if paddingLen == 0: 
        paddingLen = blockSize

    paddedText = pText + chr(paddingLen) * paddingLen
    return paddedText

def removePadding(pText):
    textLength = len(pText)
    paddingLength = ord(pText[textLength-1])
    paddingStartIndex = textLength - paddingLength

    expectedPadding = pText[paddingStartIndex:textLength]
    if expectedPadding != chr(paddingLength) * paddingLength:
        raise ValueError("Invalid padding detected")
    
    return pText[:paddingStartIndex]

def charsToBits(pBlock):
    bitBlock = ''
    for char in pBlock:
        bit = format(ord(char), '08b')

        bitBlock += bit
    return bitBlock
 
def bitsToHex(pBitBlock):
    hexList = ''
    for i in range(0, len(pBitBlock), 4):
        bitGroup = pBitBlock[i : i+4]
        hexChar = format(int(bitGroup, 2), 'x')
        hexList += hexChar

    return hexList

def hexToBits(pHexText):
    bitBlock = ''
    for hexChar in pHexText:
        bitBlock += format(int(hexChar, 16), '04b')

    return bitBlock

def bitsToChars(pBitBlock):
    charList = ''
    for i in range(0, len(pBitBlock), 8):
        bitGroup = pBitBlock[i : i+8]
        char = format(int(bitGroup, 2), 'c')
        charList += char

    return charList

def DES(pBitText, pBitKey, pMode):
    numberOfDES = len(pBitText) // 64
    resultText = ''

    for i in range(numberOfDES): # number of DESs to do
        block = pBitText[i*64 : (i+1)*64]
        roundKeyList = keysGenerator(pBitKey, pMode)
        permutedText = initialPermutation(block)
        left, right = splitBlock(permutedText) 

        for j in range(16): # number of rounds to do
            left, right = fiestelFunction(left, right, roundKeyList[j])
        
        finalRoundBlock = right + left
        resultBlock = finalPermutation(finalRoundBlock)
        resultText += resultBlock

    return resultText

def main(pFileName):
    text = openFile(pFileName)
    if text is None: return

    while True:
        key = input("Key >> ")
        if len(key) < 8:
            print("You need to input an 8-character key!\n")
        else:
            key = key[:8]  # Truncate if it's too long
            break

    choice = 'A'
    while choice not in ('E','D'):
        choice = input('(E)ncrypt or (D)ecrypt >> ').upper()
        if choice == 'E':
            paddedText = blockPadding(text) # add padding to the text
            bitText = charsToBits(paddedText)
            bitKey = charsToBits(key)
            cipherText = DES(bitText, bitKey, 'E') 
            hexCipherText = bitsToHex(cipherText)
            with open("DES-Cipher.txt", "w") as file:
                file.write(hexCipherText)
        elif choice == 'D':
            bitText = hexToBits(text)
            bitKey = charsToBits(key)
            plainText = DES(bitText, bitKey, 'D')
            charsPlainText = bitsToChars(plainText)
            charsPlainText = removePadding(charsPlainText)
            with open("DES-Plain.txt", "w") as file:
                file.write(charsPlainText) 
        else:
            print("Error: Invalid options, input E or D only")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python freqChart.py <filename>")
    else:
        main(sys.argv[1])


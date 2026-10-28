from DES import *
from DESFunction import *

def testBlockPadding():
    input_text = "12345678"  # 8 characters, 8 bytes (64 bits)
    padded_text = blockPadding(input_text)
    assert padded_text == "12345678\x08\x08\x08\x08\x08\x08\x08\x08", "Test failed: padding is incorrect"

    # Test case 2: Input length is less than block size
    input_text = "1234"  # 4 characters, 4 bytes (32 bits)
    padded_text = blockPadding(input_text)
    assert padded_text == "1234\x04\x04\x04\x04", "Test failed: padding is incorrect"

    # Test case 3: Input length is greater than block size but not a multiple of block size
    input_text = "123456"  # 6 characters, 6 bytes (48 bits)
    padded_text = blockPadding(input_text)
    assert padded_text == "123456\x02\x02", "Test failed: padding is incorrect"

def testCharsToBits():
    input_text = 'AB'
    bitText = charsToBits(input_text)
    assert bitText == '0100000101000010', "Test failed: conversion is incorrect"

def testBitsToHex():
    input_text = '0100000101000010'
    hexText = bitsToHex(input_text)
    assert hexText == '4142', "Test failed: conversion is incorrect"

def testHexToBits():
    input_text = '4142'
    bitText = hexToBits(input_text)
    assert bitText == '0100000101000010', "Test failed: conversion is incorrect"

def testBitsToChars():
    # Test 1: Basic test with 8 bits for 'A' and 'B' (should return 'AB')
    input_text = '0100000101000010'
    charText = bitsToChars(input_text)
    assert charText == 'AB', "Test failed: conversion is incorrect"

    # Test 2: Single character 'A' (8 bits for 'A', expected 'A')
    input_text = '01000001'
    charText = bitsToChars(input_text)
    assert charText == 'A', "Test failed: conversion is incorrect"

    # Test 3: Single character 'Z' (8 bits for 'Z', expected 'Z')
    input_text = '01011010'
    charText = bitsToChars(input_text)
    assert charText == 'Z', "Test failed: conversion is incorrect"

    # Test 4: Test multiple characters (8 bits for 'A', 'B', 'C', 'D', expected 'ABCD')
    input_text = '01000001010000100100001101000100'
    charText = bitsToChars(input_text)
    assert charText == 'ABCD', "Test failed: conversion is incorrect"

    # Test 5: Empty input (should return empty string)
    input_text = ''
    charText = bitsToChars(input_text)
    assert charText == '', "Test failed: conversion is incorrect"

    # Test 6: All zeros (should return a string of NUL characters)
    input_text = '0000000000000000'
    charText = bitsToChars(input_text)
    assert charText == '\x00\x00', "Test failed: conversion is incorrect"

    # Test 7: Test with different characters (input is 'HELLO')
    input_text = '0100100001000101010011000100110001001111'  # 'HELLO'
    charText = bitsToChars(input_text)
    assert charText == 'HELLO', "Test failed: conversion is incorrect"

def testSplitBlock():
    test_input = '0100000101000010'
    left, right = splitBlock(test_input)
    assert left == '01000001', "Test failed: split is incorrect"
    assert right == '01000010', "Test failed: split is incorrect"

    test_input = '0100100001000101010011000100110001001111'
    left, right = splitBlock(test_input)
    assert left == '01001000010001010100', "Test failed: split is incorrect"
    assert right == '11000100110001001111', "Test failed: split is incorrect"

def testEncryptionXOR():
    inputOne = '01001000010001010100'
    inputTwo = '11000100110001001111'
    outputXOR = encryptXOR(inputOne, inputTwo)
    assert outputXOR == '10001100100000011011', "Test failed: XOR is incorrect"

    inputOne = '11111111'
    inputTwo = '10101011'
    outputXOR = encryptXOR(inputOne, inputTwo)
    assert outputXOR == '01010100', "Test failed: XOR is incorrect"

def testIP():
    inputBits = "1100100010110010111111100010000100000010110001100000100000001110"
    expectedOutput = "0010010100000110101001000000100000100111000011101100010110110110"
    outputBits = initialPermutation(inputBits)
    assert outputBits == expectedOutput, "Test failed: Initial Permutation is incorrect"
    #1100100010110010111111100010000100000010110001100000100000001110
    #0010010100000110101001000000100000100111000011101100010110110110 

def testInvIP():
    inputBits = "0010010100000110101001000000100000100111000011101100010110110110"
    expectedOutput = "1100100010110010111111100010000100000010110001100000100000001110"
    outputBits = finalPermutation(inputBits)
    assert outputBits == expectedOutput, "Test failed: Initial Permutation is incorrect"
    #0010010100000110101001000000100000100111000011101100010110110110 
    #1100100010110010111111100010000100000010110001100000100000001110

def testExpansion():
    inputBits = "01101101011011110110110101101111"  # 32-bit input
    expectedOutput = "101101011010101101011110101101011010101101011110"  # 48-bit output
    outputBits = expansion(inputBits)
    assert outputBits == expectedOutput, "Test failed: Expansion is incorrect"
    #01101101011011110110110101101111
    #101101011010101101011110101101011010101101011110

def testPermutationBox():
    inputBits = "11001100000000001100110011111111"
    expectedOutput = "00011011100111101000110000111001"
    outputBits = permutationBox(inputBits)
    assert outputBits == expectedOutput, "Test failed: Permutation Box output is incorrect"
    #11001100000000001100110011111111
    #00011011100111101000110000111001

def testLeftShift():
    testBit = '10101101'
    testNumShift = 3
    outputBit = leftShift(testBit, testNumShift)
    assert outputBit == '01101101', "Test failed: Left Shift is incorrect"

def testRightShift():
    testBit = '10101101'
    testNumShift = 2
    outputBit = rightShift(testBit, testNumShift)
    assert outputBit == '01101011', "Test failed: Right Shift is incorrect"

def testPermutedChoiceOne():
    inputKey = "0001001100110100010101110111100110011011101111001101111111110001"
    expectedOutput = "11110000110011001010101011110101010101100110011110001111"
    outputKey = permutedChoiceOne(inputKey)
    assert outputKey == expectedOutput, "Test failed: Permuted Choice One is incorrect"

    #0001001100110100010101110111100110011011101111001101111111110001

def testPermutedChoiceTwo():
    inputKey = "11110000110011001010101011110101010101100110011110001111"
    expectedOutput = "110010110011110110001011000011100001011111110101"
    outputKey = permutedChoiceTwo(inputKey)
    assert outputKey == expectedOutput, "Test failed: Permuted Choice Two is incorrect"
    #11110000110011001010101011110101010101100110011110001111
    #110010110011110110001011000011100001011111110101

def testSubstitutionBox():
    inputBlock = "1111001010101110000011110101011100001100001111000011110000111110"
    expectedOutput = "01010100010100111111011110100101"  # Example expected output
    outputBlock = substitutionBox(inputBlock)
    assert outputBlock == expectedOutput, "Test failed: Substitution Box is incorrect."

def testEncryptionKeysGenerator():
    inputKey = '1010010111010101110100001001000010101010101001001010010101001000'
    outputList = keysGenerator(inputKey, 'E')

    expected = permutedChoiceOne(inputKey)
    left, right = splitBlock(expected)
    left = leftShift(left, 27)
    right = leftShift(right, 27)
    combine = left + right
    expectedOutput = permutedChoiceTwo(combine)
    assert outputList[14] == expectedOutput, "Test failed: Encryption Keys Generator is incorrect."

def testDecryptionKeysGenerator():
    inputKey = '1010010111010101110100001001000010101010101001001010010101001000'
    outputListOne = keysGenerator(inputKey, 'E')
    outputListTwo = keysGenerator(inputKey, 'D')

    assert outputListOne[0] == outputListTwo[15], "Test failed: Decryption Keys Generator is incorrect."
    assert outputListOne[1] == outputListTwo[14], "Test failed: Decryption Keys Generator is incorrect."
    assert outputListOne[2] == outputListTwo[13], "Test failed: Decryption Keys Generator is incorrect."
    assert outputListOne[3] == outputListTwo[12], "Test failed: Decryption Keys Generator is incorrect."
    assert outputListOne[4] == outputListTwo[11], "Test failed: Decryption Keys Generator is incorrect."
    assert outputListOne[5] == outputListTwo[10], "Test failed: Decryption Keys Generator is incorrect."
    assert outputListOne[6] == outputListTwo[9], "Test failed: Decryption Keys Generator is incorrect."
    assert outputListOne[7] == outputListTwo[8], "Test failed: Decryption Keys Generator is incorrect."
    assert outputListOne[8] == outputListTwo[7], "Test failed: Decryption Keys Generator is incorrect."
    assert outputListOne[9] == outputListTwo[6], "Test failed: Decryption Keys Generator is incorrect."
    assert outputListOne[10] == outputListTwo[5], "Test failed: Decryption Keys Generator is incorrect."
    assert outputListOne[11] == outputListTwo[4], "Test failed: Decryption Keys Generator is incorrect."
    assert outputListOne[12] == outputListTwo[3], "Test failed: Decryption Keys Generator is incorrect."
    assert outputListOne[13] == outputListTwo[2], "Test failed: Decryption Keys Generator is incorrect."
    assert outputListOne[14] == outputListTwo[1], "Test failed: Decryption Keys Generator is incorrect."
    assert outputListOne[15] == outputListTwo[0], "Test failed: Decryption Keys Generator is incorrect."

def testLeftRightXOR():
    left =  '1010010001111000'
    right = '0000011111000000'
    output = leftRightXOR(left, right)
    expectedOutput = '1010001110111000'
    assert output == expectedOutput, "Test failed: Left XOR Right is incorrect."

def testRemovePadding():
    assert removePadding("Hello\x03\x03\x03") == "Hello", "Test failed: Padding removal is incorrect"
    assert removePadding("DataBlock\x04\x04\x04\x04") == "DataBlock", "Test failed: Padding removal is incorrect"
    assert removePadding("Test\x01") == "Test", "Test failed: Padding removal is incorrect"
    assert removePadding("\x08\x08\x08\x08\x08\x08\x08\x08") == "","Test failed: Padding removal is incorrect"
    try:
        removePadding("Invalid\x05\x05\x05\x02")
        assert False, "Test failed: Did not raise error on invalid padding"
    except ValueError:
        pass 

def main():
    testBlockPadding()
    testCharsToBits()
    testBitsToHex()
    testHexToBits()
    testBitsToChars()
    testSplitBlock()
    testEncryptionXOR()
    testIP()
    testInvIP()
    testExpansion()
    testLeftShift()
    testRightShift()
    testPermutationBox()
    testPermutedChoiceOne()
    testPermutedChoiceTwo()
    testSubstitutionBox()
    testEncryptionKeysGenerator()
    testDecryptionKeysGenerator()
    testLeftRightXOR()
    testRemovePadding()
    print("All tests passed!")

if __name__ == "__main__":
    main()
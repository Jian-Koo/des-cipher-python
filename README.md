# DES Cipher Implementation in Python

An educational implementation of the **Data Encryption Standard (DES)** cryptographic algorithm in Python, developed to explore symmetric-key encryption, Feistel networks, bitwise operations, key scheduling, and block cipher design.

The application supports file encryption and decryption through a command-line interface, with the core DES algorithm implemented from scratch without external cryptographic libraries.

## Project Overview

DES is a symmetric-key block cipher that operates on 64-bit data blocks using a 16-round Feistel network.

This project implements the underlying DES operations, including:

- Initial and final permutations
- 64-bit block processing
- Expansion from 32 bits to 48 bits
- XOR operations
- Substitution using eight DES S-boxes
- Permutation operations
- 16-round Feistel network
- Round-key generation and scheduling
- Encryption and decryption
- Block padding and padding removal
- Binary, hexadecimal, and character conversions

The application processes text files, encrypts their contents into hexadecimal ciphertext, and supports decryption using the same key.

## Implementation

### DES Encryption

The encryption process follows the standard DES structure:

1. Read the plaintext from an input file.
2. Apply padding to align the plaintext with 64-bit blocks.
3. Convert the characters into binary.
4. Generate 16 round keys from the supplied key.
5. Apply the initial permutation.
6. Process each block through 16 Feistel rounds.
7. Apply the final permutation.
8. Convert the encrypted binary data into hexadecimal format.
9. Save the ciphertext to `DES-Cipher.txt`.

### DES Decryption

Decryption reverses the process:

1. Read the hexadecimal ciphertext.
2. Convert the ciphertext into binary.
3. Generate the DES round keys in reverse order.
4. Apply the DES Feistel network.
5. Convert the resulting binary data into characters.
6. Remove the block padding.
7. Save the recovered plaintext to `DES-Plain.txt`.

DES uses the same underlying Feistel structure for encryption and decryption, with the round keys applied in opposite orders.

### Key Scheduling

The implementation generates 16 round keys through:

- Permuted Choice 1 (PC-1)
- Splitting the key into two 28-bit halves
- Circular left or right shifts
- Permuted Choice 2 (PC-2)

Each round uses a 48-bit subkey derived from the original 64-bit key representation.

## Repository Structure

```text
des-cipher-python/
├── README.md
├── .gitignore
├── DES.py
├── DESFunction.py
├── DES_Testing.py
└── DES-test2025.txt
```

| File | Description |
|---|---|
| `DES.py` | Main application handling file input, encryption, decryption, padding, and output |
| `DESFunction.py` | Implementation of the DES permutations, Feistel function, substitution boxes, and key scheduling |
| `DES_Testing.py` | Unit tests covering individual DES operations and helper functions |
| `DES-test2025.txt` | Sample plaintext file for demonstrating encryption and decryption |

The application generates `DES-Cipher.txt` and `DES-Plain.txt` during execution.

## Requirements

- Python 3
- A terminal or command-line environment

The implementation relies exclusively on Python's standard library.

**No additional Python packages are required.**

## Usage

### 1. Encryption

Run the application with a plaintext file:

```bash
python3 DES.py DES-test2025.txt
```

Enter an eight-character key when prompted:

```text
Key >> MYKEY123
(E)ncrypt or (D)ecrypt >> E
```

The encrypted output is saved as:

```text
DES-Cipher.txt
```

The ciphertext is represented as hexadecimal text.

### 2. Decryption

Run the application using the encrypted file:

```bash
python3 DES.py DES-Cipher.txt
```

Enter the same key and select decryption:

```text
Key >> MYKEY123
(E)ncrypt or (D)ecrypt >> D
```

The decrypted plaintext is saved as:

```text
DES-Plain.txt
```

The original plaintext can then be compared against the decrypted output to verify successful recovery.

**Note:** The application expects an eight-character key. Longer inputs are truncated to eight characters. The text-processing implementation is intended for compatible eight-bit character input, such as ASCII text.

## Unit Testing

The project includes a dedicated test script:

```bash
python3 DES_Testing.py
```

The test suite covers:

- Block padding and padding removal
- Character-to-binary conversion
- Binary-to-hexadecimal conversion
- Hexadecimal-to-binary conversion
- Binary-to-character conversion
- Block splitting
- XOR operations
- Initial and final permutations
- Expansion permutation
- Permutation box
- Substitution boxes
- Circular key shifts
- Permuted Choice 1 and 2
- Encryption and decryption key schedules
- Feistel-related helper operations

Successful execution displays:

```text
All tests passed!
```

These tests help verify the individual components of the DES implementation.

## Design Considerations and Limitations

### Educational Implementation

The cipher operations are implemented directly in Python to demonstrate the internal workings of DES rather than relying on an existing cryptographic library.

This makes the project useful for examining the relationship between binary operations, permutation tables, substitution boxes, and Feistel rounds.

### Block Processing

The application processes 64-bit blocks independently without implementing a chaining mode or authenticated encryption.

Consequently, identical plaintext blocks encrypted with the same key can produce identical ciphertext blocks.

### Input Handling

The implementation is designed primarily for text files containing compatible eight-bit characters. It is not a general-purpose binary file encryption utility.

### Cryptographic Security

**DES is obsolete and should not be used to protect sensitive information.**

Its effective 56-bit key length is insufficient against modern brute-force attacks. This implementation also does not provide ciphertext authentication or integrity protection.

For modern applications, established and properly implemented authenticated encryption schemes, such as AES-GCM, should be used instead.

This project is intended strictly for educational purposes and cryptographic algorithm exploration.

## Project Background

This project was originally developed as part of undergraduate cryptography coursework and has been organised for portfolio presentation.

The main objective was to develop a deeper understanding of symmetric-key cryptography through direct implementation of DES, including its Feistel structure, permutation and substitution operations, and key scheduling.

The project emphasises algorithm implementation, binary data manipulation, modular programming, and unit testing.

## Copyright

Copyright © 2026 Jian Heng Koo. All rights reserved.

The original source code, documentation, and other original materials in this repository are the work of Jian Heng Koo.

No licence is granted to copy, modify, redistribute, publish, sublicense, or use these materials for commercial purposes without permission from the author.

The DES algorithm is a publicly documented cryptographic standard. Third-party references, tools, and other materials remain subject to their respective licences and copyright terms.

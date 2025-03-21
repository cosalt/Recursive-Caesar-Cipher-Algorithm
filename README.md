# Recursive Caesar Cipher Algorithm

This repository provides two Python implementations of the Caesar Cipher algorithm: one utilizing recursion and the other employing iteration. The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted by a fixed number of positions down or up the alphabet.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Encrypting a Message](#encrypting-a-message)
  - [Decrypting a Message](#decrypting-a-message)
- [Examples](#examples)
  - [recursive-implementation](https://github.com/cosalt/Recursive-Caesar-Cipher-Algorithm/blob/main/with%20recursion.py)
  - [iterative-implementation](https://github.com/cosalt/Recursive-Caesar-Cipher-Algorithm/blob/main/without%20recursion.py)
- [Contributing](#contributing)
- [License](#license)

## About

The Caesar Cipher is one of the simplest and most widely known encryption techniques. In this repository, both recursive and iterative methods are provided to demonstrate different approaches to implementing the cipher.

## Features

- **Recursive Implementation**: Encrypt and decrypt messages using a recursive approach.
- **Iterative Implementation**: Encrypt and decrypt messages using an iterative approach.
- **Encryption and Decryption**: Both encryption and decryption functionalities are provided.
- **Alphabet Wrapping**: Handles wrapping around the alphabet correctly during encryption and decryption.

## Installation

1. **Clone the repository**:

   ```
   git clone https://github.com/cosalt/Recursive-Caesar-Cipher-Algorithm.git
   ```
   This command clones the repository to your local machine.

2. **Navigate to the project directory**:

   ```
   cd Recursive-Caesar-Cipher-Algorithm
   ```
   Change into the project directory.

3. **Ensure you have Python 3 installed**. You can download it from [python.org](https://www.python.org/downloads/).

## Usage

Both implementations provide functions to encrypt and decrypt messages.

### Encrypting a Message

To encrypt a message, use the `encrypt` function, specifying the plaintext and the shift key.

```
from caesar_cipher import encrypt

plaintext = "Hello, World!"
shift_key = 3
ciphertext = encrypt(plaintext, shift_key)
print("Encrypted:", ciphertext)
```
This script imports the `encrypt` function, defines a plaintext message and a shift key, encrypts the message, and prints the ciphertext.

### Decrypting a Message

To decrypt a message, use the `decrypt` function, specifying the ciphertext and the shift key.

```
from caesar_cipher import decrypt

ciphertext = "Khoor, Zruog!"
shift_key = 3
plaintext = decrypt(ciphertext, shift_key)
print("Decrypted:", plaintext)
```
This script imports the `decrypt` function, defines a ciphertext message and a shift key, decrypts the message, and prints the plaintext.

## Examples

### Recursive Implementation

The `with_recursion.py` file contains a recursive implementation of the Caesar Cipher. To use it:

1. Open `with_recursion.py`.
2. Follow the instructions within the script to input your message and desired shift key.

### Iterative Implementation

The `without_recursion.py` file provides an iterative implementation of the Caesar Cipher. To use it:

1. Open `without_recursion.py`.
2. Follow the prompts to input your message and shift key.

## Contributing

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request with your proposed changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

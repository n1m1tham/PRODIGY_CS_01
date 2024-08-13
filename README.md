Cipher.py
This repository contains a Python program that implements the Caesar Cipher algorithm, which can be used to encrypt and decrypt text messages. The Caesar Cipher is a simple substitution cipher where each letter in the plaintext is shifted by a fixed number of positions down or up the alphabet.

Features
Encrypt text messages by shifting letters forward in the alphabet.
Decrypt text messages by shifting letters backward in the alphabet.
Handles both uppercase and lowercase letters.
Non-alphabetic characters (e.g., numbers, punctuation) remain unchanged.
How It Works
The Caesar Cipher works by shifting the letters in the input text by a specified number of positions (shift value). For example, with a shift value of 3:

'A' becomes 'D'
'B' becomes 'E'
'C' becomes 'F'
'X' becomes 'A'
'Y' becomes 'B'
'Z' becomes 'C'
The process can be reversed using the same shift value to decrypt the message.

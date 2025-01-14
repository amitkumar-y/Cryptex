"""
Author: @marvhus
Instructions:
    Rename the "Text" class to whatever cipher you are working on.
    Edit the encode and decode defs as required to encode or decode your cipher.
    make sure you add the following to __init__.py: from cipherfile import *
    Doing this will link the code to main.py 
"""
from cipher import Cipher

class R47(Cipher):

    name = 'Rot 47'
    type = 'cipher'

    def encode(args):
        text = args.text

        if not text:
            return {'text': "No input text", 'success': False}

        output = ''

        for character in text:
            encoded = ord(character)
            if encoded  >= 33 and encoded <= 126:
                output += chr(33 + ((encoded + 14) % 94))
            else:
                output += character

        return {'text': output, 'success': True}

    def decode(args):
        text = args.text

        if not text:
            return {'text': "No input text", 'success': False}

        output = ''

        for character in text:
            encoded = ord(character)
            if encoded >= 33 and encoded <= 126:
                output += chr(33 + ((encoded + 14) % 94))
            else:
                output += character

        return {'text': output, 'success': True}

    def print_options():
        print(''' 
        ### Modes
        -d / --decode ---- decode
        -e / --encode ---- encode

        ### Input
        -t / --text ------ input text

        ### Examples
        python main.py r47 -e -t 'hello'
        python main.py r47 -d -t 'hello'
        ''')

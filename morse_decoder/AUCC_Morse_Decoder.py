#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys

morseAlphabet ={
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",
    " " : "/"
    }

inverseMorseAlphabet=dict((v,k) for (k,v) in morseAlphabet.items())

def decodeMorse(morse_mesaj):
    text_mesaj = ""
    for item in morse_mesaj.split(' '):
        text_mesaj = text_mesaj + inverseMorseAlphabet[item]
    return text_mesaj

def kullanim_mesaji(name=None):
    usage = sys.argv[0] + " message [-h --help] [-v --version]\n" 
    description = "--------AUCC Python Morse Decoder--------\n"
    example1 = "Example: python " + sys.argv[0] + " \".-- . / .-.. --- ...- . / .- ..- -.-. -.-.\"\n" 
    return   usage +"\n"+ description +"\n"+ example1


def main():
    
    parser = argparse.ArgumentParser(description='--------AUCC Python Morse Encoder--------', usage=kullanim_mesaji())
    parser.add_argument("message", help="Please enter it in double quotes")
    parser.add_argument("-v", "--version", action='version', version='%(prog)s  0.4b')
    args = parser.parse_args()
    
    morse_mesaj = args.message
   
    text_mesaj = decodeMorse(morse_mesaj)
    print "Your message has been trasnlated.."
    print "The message :\n--> ",text_mesaj 
    

if __name__ == '__main__':
    main()


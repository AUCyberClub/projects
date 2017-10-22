#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import sys
import math
import struct
import tempfile
import argparse

import numpy as np
import wave

morse_tablosu = {
        'A': '.-',              'a': '.-',
        'B': '-...',            'b': '-...',
        'C': '-.-.',            'c': '-.-.',
        'D': '-..',             'd': '-..',
        'E': '.',               'e': '.',
        'F': '..-.',            'f': '..-.',
        'G': '--.',             'g': '--.',
        'H': '....',            'h': '....',
        'I': '..',              'i': '..',
        'J': '.---',            'j': '.---',
        'K': '-.-',             'k': '-.-',
        'L': '.-..',            'l': '.-..',
        'M': '--',              'm': '--',
        'N': '-.',              'n': '-.',
        'O': '---',             'o': '---',
        'P': '.--.',            'p': '.--.',
        'Q': '--.-',            'q': '--.-',
        'R': '.-.',             'r': '.-.',
        'S': '...',             's': '...',
        'T': '-',               't': '-',
        'U': '..-',             'u': '..-',
        'V': '...-',            'v': '...-',
        'W': '.--',             'w': '.--',
        'X': '-..-',            'x': '-..-',
        'Y': '-.--',            'y': '-.--',
        'Z': '--..',            'z': '--..',
        '0': '-----',           ',': '--..--',
        '1': '.----',           '.': '.-.-.-',
        '2': '..---',           '?': '..--..',
        '3': '...--',           ';': '-.-.-.',
        '4': '....-',           ':': '---...',
        '5': '.....',           "'": '.----.',
        '6': '-....',           '-': '-....-',
        '7': '--...',           '/': '-..-.',
        '8': '---..',           '(': '-.--.-',
        '9': '----.',           ')': '-.--.-',
        ' ': ' ',               '_': '..--.-',
}

def write_signal(wavef, duration, volume=0, rate=44100.0,frequency=1240.0):
    for i in range(int(duration * rate * duration)):

            value = int(volume*math.sin(frequency*math.pi*float(i)/float(rate)))
            data = struct.pack('<h', value)
            wavef.writeframesraw(data)
            
def morse_to_wav(text, uzunluk_carpani, bosluk_carpani, file_=None):
    if not file_:
        _, file_ = tempfile.mkstemp(".wav")

    wav = wave.open(file_, 'w')
    wav.setnchannels(1)
    wav.setsampwidth(2)
    rate = 44100.0
    wav.setframerate(rate)

    for char in text:
        if char == '.':
            write_signal(wav, 0.25*uzunluk_carpani, volume=32767.0)
        if char == '-':
            write_signal(wav, 0.5*uzunluk_carpani, volume=32767.0)
        if char == ' ':
            write_signal(wav, 0.2*bosluk_carpani, volume=0)
        write_signal(wav, 0.2*uzunluk_carpani, volume=0)

    wav.writeframes('')
    wav.close()

    return file_

def denetle(string):
    keys = morse_tablosu.keys()
    for char in string:
        if char.upper() not in keys and char != ' ':
            sys.exit('You cant encode ' + char + ' this character.')

def text_to_mors(text_mesaj):
    morse_mesaj = "" 
    for char in text_mesaj:
        if char == ' ':
            morse_mesaj = morse_mesaj + " "
        else:
            morse_mesaj = morse_mesaj + " " + morse_tablosu[char.upper()]
                
    return morse_mesaj

def kullanim_mesaji(name=None):
    usage = sys.argv[0] + " message [-h --help] [-d --directory] [-l --length] [-s --space] [-v --version]\n" 
    description = "--------AUCC Python2 Morse Encoder--------\n"
    example1 = "Example1: python2 " + sys.argv[0] + " \"SOS\"\n"
    example2 = "Example2: python2 " + sys.argv[0] + " \"SOS\" -d ~/Desktop/SOS.waw\n"
    example3 = "Example3: python2 " + sys.argv[0] + " \"SOS\" -d ~/Desktop/SOS.waw -l 2 -s 2" 
    return   usage +"\n"+ description +"\n"+ example1 + example2 + example3


def main():
    
    parser = argparse.ArgumentParser(description='--------AUCC Python2 Morse Encoder--------', usage=kullanim_mesaji())
    parser.add_argument("message", help="Please enter it in double quotes")
    parser.add_argument("-d", "--directory", help="save directory of sound file")
    parser.add_argument("-l", "--length", type=float, default=1, help="length multipler")
    parser.add_argument("-s", "--space", type=float, default=1, help="space character multipler")
    parser.add_argument("-v", "--version", action='version', version='%(prog)s  0.4b')
    args = parser.parse_args()
    
    text_mesaj = args.message
    denetle(text_mesaj)
    
    morse_mesaj = text_to_mors(text_mesaj)
    print "Your message has been trasnlated.."
    print "The message :\n--> ",morse_mesaj 
    
    kayit_yolu = args.directory
    uzunluk_carpani = args.length
    bosluk_carpani =args.space
    
    if kayit_yolu:
        f = morse_to_wav(morse_mesaj, uzunluk_carpani, bosluk_carpani, file_=kayit_yolu)
        print "Your message has been saved."

if __name__ == '__main__':
    main()

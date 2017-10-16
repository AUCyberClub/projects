#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
import socket
from multiprocessing import Pool
from time import time

ip = None
quiet_flag = None

def split_list_to_lists(alist, wanted_parts):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts) ]

def scanner(port):
    global ip, quiet_flag
    sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sck.connect_ex((socket.gethostbyname(ip), port))
    if result == 0: print ("%d ->\tOpen" % port)
    elif not quiet_flag: print ("%d ->\tClose" % port)
    sck.close()

def kullanim_mesaji():   
    usage = sys.argv[0] + " ip [-h --help] [-m --mprocessors] [-a | -k | -s] [-p --ports] [-q --quiet] [-v --version] \n" 
    description = "--------AUCC Port Scanner-------- \n"
    example1 = "Example1: python " + sys.argv[0] + " localhost -m 4 -k -q \n"
    example2 = "Example2: python " + sys.argv[0] + " localhost -s -p 22,80,8080\n"
    example3 = "Example3: python " + sys.argv[0] + " 192.168.1.1 -m 4 -a -q"
    return usage +"\n"+ description +"\n"+ example1 + example2 + example3

def main():
    global ip, quiet_flag
    parser = argparse.ArgumentParser(description='--------AUCC Port Scanner--------', usage=kullanim_mesaji())
    parser.add_argument("ip", default="localhost", help="IP Adress of target")
    parser.add_argument("-m", "--mprocessors", default=1, help="The number of processors to be used for multiprocessing")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-a", "--allports", help="Scan all ports", action="store_true")
    group.add_argument("-k", "--known", help="Scan well known ports (First 2000)", action="store_true")
    group.add_argument("-s", "--specific", help="Scan specific ports", action="store_true")
    parser.add_argument("-p", "--ports", help="Port list")
    parser.add_argument("-q", "--quiet", help="Print only open ports", action="store_true")
    parser.add_argument("-v", "--version", action='version', version='%(prog)s  0.3b')
    args = parser.parse_args()
    
    ip = args.ip
    quiet_flag = args.quiet
    
    if args.allports:
        portList = list(range(65535))
    if args.known:
        portList = list(range(2000))
    if args.specific:
        portList = [int(i) for i in [i.strip() for i in args.ports.split(',')]]   
    p = Pool(int(args.mprocessors))
    for i in split_list_to_lists(portList, int(args.mprocessors)):
        p.map(scanner, i)
        
if __name__ == '__main__':
    start_time = time()
    main()
    print ("Task take %1.2f seconds." % (time() - start_time)) 

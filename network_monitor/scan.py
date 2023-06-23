#!/usr/bin/python3
"""
These modules are essential for the script tp work properly
"""
import os
from sys import argv


def scan():
    """
    This function gets the IP address and scans the address then
    saves the output in the file scanned.txt
    """
    os.system(f"nmap -sT {argv[1]} > scanned.txt")
    """
    this is a prototype after the development of the database
    the file will be uploaded to the database and SMTP will
    be triggered and results will be sent to the client
    """

#!/usr/bin/env python3

import argparse


    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='CLI tool to track your tasks')
    parser.add_argument('action', type=str, help='Provide action add, update, delete')
    
    parser.add_argument('-t', '--text', type=str, help='Items to list')
    parser.add_argument('-r', '--roles', type=str, help='Roles of the user separated by commas')
    parser.add_argument('-m', '--minutes', type=float, default=0, help='Session expiration in minutes')
    parser.add_argument('-d', '--days', type=float, default=0, help='Session expiration in days')
    parser.add_argument('-w', '--weeks', type=float, default=0, help='Session expiration in weeks')
    args = parser.parse_args()

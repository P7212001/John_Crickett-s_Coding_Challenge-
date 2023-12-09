import sys
import argparse

def ccwc(filename, option):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    lines = text.count('\n')
    words = len(text.split())
    chars = len(text)
    bytes = sys.getsizeof(text)
    
    if option == 'c':
        print(f'Bytes: {bytes}, {filename}')
    elif option == 'l':
        print(f'Lines: {lines}, {filename}')
    elif option == 'w':
        print(f'Words: {words}, {filename}')
    elif option == 'm':
        print(f'Characters: {chars}, {filename}')
    else:
        print(f'Lines: {lines}, Words: {words}, Bytes: {bytes}, {filename}')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='the file to analyze')
    parser.add_argument('-c', action='store_true', help='count bytes')
    parser.add_argument('-l', action='store_true', help='count lines')
    parser.add_argument('-w', action='store_true', help='count words')
    parser.add_argument('-m', action='store_true', help='count characters')
    args = parser.parse_args()

    if args.c:
        ccwc(args.filename, 'c')
    elif args.l:
        ccwc(args.filename, 'l')
    elif args.w:
        ccwc(args.filename, 'w')
    elif args.m:
        ccwc(args.filename, 'm')
    else:
        ccwc(args.filename, '')

if __name__ == '__main__':
    main()
